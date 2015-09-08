#!/usr/bin/env python

import datetime
import errno
import io
import itertools
import os
import re

import docutils.examples
import jinja2
import lxml.html
#import yaml


def parse_date(s):
    """Returns a datetime.date, from a date in the tabular schedule

    >>> parse_date('Friday 18th September 2015')
    datetime.date(2015, 9, 18)
    """
    m = re.match(r"""
        (?P<dayname>    [A-Za-z]+)
        \s
        (?P<day>        [0-9]+)
        [a-z]{0,2} # Discard any suffix, e.g. th, st
        \s
        (?P<monthname>  [A-Za-z]+)
        \s
        (?P<year>       [0-9]+)
        """,
        s, re.VERBOSE,
        )
    s = '{day} {monthname} {year}'.format(**m.groupdict())
    return datetime.datetime.strptime(s, '%d %B %Y').date()


def parse_time(s):
    """Returns a datetime.time, from an event time in the tabular schedule
    """
    return datetime.datetime.strptime(s, '%H:%M').time()


def parse_days(tree):
    """Yields (day, table) for each day covered by the tabular schedule
    """
    for section in tree.xpath('''
            //div[@class="section"
                  and (starts-with(@id, "friday")
                       or starts-with(@id, "saturday")
                       or starts-with(@id, "sunday")
                       or starts-with(@id, "monday")
                       )
                  ]'''):
        day = parse_date(section[0].text)
        for table in section.xpath('.//table'):
            yield day, table


def collapse_whitespace(s):
    """Strips surrounding & repeated whitespace from s
    """
    return re.sub(r'\s+', ' ', s.strip())


def repeat_none(value, times):
    for i in xrange(times):
        yield None


def colspan_cells(cells, fillfunc=itertools.repeat):
    """Yields td or th elements, repeating them as necessary for colspan=n
    """
    for cell in cells:
        yield cell
        colspan = int(cell.get('colspan', 1))
        for item in fillfunc(cell, colspan-1):
            yield item


def rowspan_cells(cells, rowspans, fillfunc=itertools.repeat):
    """Yields td or th elements, repeating them as necessary for colspan=n
    & rowspan=n.
    """
    cells = iter(cells)
    col = 0
    while True:
        try:
            ttl, cell = rowspans.pop(col)
            for item in fillfunc(cell, 1):
                yield item
        except KeyError:
            cell = next(cells)
            ttl = int(cell.get('rowspan', 1))
            yield cell
        ttl -= 1
        if ttl > 0:
            rowspans[col] = (ttl, cell)
        colspan = int(cell.get('colspan', 1))
        for item in fillfunc(cell, colspan-1):
            yield item
        col += colspan


def parse_rooms(table):
    """Yields the rooms used in a single schedule table
    """
    row1 = colspan_cells(table.xpath('./thead/tr[1]/th')[1:])
    row2 = colspan_cells(table.xpath('./thead/tr[2]/th')[1:])
    for th1, th2 in itertools.izip_longest(row1, row2):
        text1 = collapse_whitespace(th1.text)
        text2 = collapse_whitespace(th2.text) if th2 is not None else ''
        if text2:
            yield '%s (%s)' % (text1, text2)
        else:
            yield text1


def parse_event_href(href):
    m = re.match(r'''
        /(?P<type>demo|panel|sprint|talk|workshop)s
        /(?P<slug>[a-z0-9-]+)
        /
        ''',
        href,
        re.VERBOSE)
    if m:
        return m.groupdict()
    return {}


def parse_abstract(href):
    """Returns info about an event, parsed from the Markdown abstract
    """
    info = parse_event_href(href)
    if not info:
        return info
    path = 'content/{type}s/{slug}.md'.format(**info)
    with io.open(path, encoding='utf-8') as f:
            markdown = f.read(1024)

    m = re.search(r'^### +?(?P<speaker>[\w][^\n]+?)\n',
                  markdown, re.UNICODE | re.MULTILINE)
    if m:
        info.update(m.groupdict())

    m = re.search(r'^### +?\[(?P<speaker>[\w][^\]]+?)\]',
                  markdown, re.UNICODE | re.MULTILINE)
    if m:
        info.update(m.groupdict())
    return info


def parse_event_title(title, default_room):
    """Parse an event title that may contain extra room information

    >>> parse_event_title('Foo', 'Broom closet')
    ('Foo', 'Broom closet')
    >>> parse_event_title('Foo (in the Atrium)', 'Broom closet')
    ('Foo', 'Atrium')
    >>> parse_event_title('Foo (in The Atrium)', 'Broom closet')
    ('Foo', 'The Atrium')
    """
    title = collapse_whitespace(title)

    m = re.match(r'(?P<title>.+) \((?:in the|in) (?P<room>[^)]+)\)',
                 title, re.UNICODE)
    if m:
        return m.group('title'), m.group('room')

    if re.match(r'(?:registration[ /&]+)?breakfast', title, re.IGNORECASE):
        return title, 'Cafeteria'

    return title, default_room


def parse_event(td, default_room=None):
    """Returns the details of an event, parsed from a table cell
    """
    anchors = list(td.xpath('a'))
    href = anchors[0].get('href') if len(anchors) == 1 else None
    abstract_info = parse_abstract(href) if href is not None else {}
    speaker = abstract_info.get('speaker')
    type_ = abstract_info.get('type')
    title, room = parse_event_title(td.text_content(), default_room)
    return href, title, room, speaker, type_


def stringify_children(node):
    # http://stackoverflow.com/a/28173933/293340
    parts = ([node.text]
             + list(itertools.chain(*([lxml.html.tostring(c, with_tail=False),
                                       c.tail] for c in node.getchildren())
                                      ))
             + [node.tail])
    # filter removes possible Nones in texts and tails
    return ''.join(part for part in parts if part is not None)


def events(table):
    """Yields event dicts parsed from a single schedule table
    """
    rooms = [room for room in parse_rooms(table)]
    trs = [tr for tr in table.xpath('./tbody/tr')
           if tr.find('./td').text != u'\N{NO-BREAK SPACE}']
    times = [parse_time(tr.find('./td').text) for tr in trs]

    rowspans = {}

    for i, (start_time, tr) in enumerate(zip(times, trs)):
        tds = tr.xpath('./td')[1:]

        for j, td in enumerate(rowspan_cells(tds, rowspans, fillfunc=repeat_none)):
            if td is None:
                continue
            rowspan = int(td.get('rowspan', 1))
            try:
                finish_time = times[i+rowspan]
            except IndexError:
                finish_time = None
            href, title, room, speaker, type_ = parse_event(td, rooms[j])
            rawhtml = stringify_children(td)
            event = {
                'start': start_time,
                'finish': finish_time,
                'href': href,
                'location': room,
                'title': title,
                'speaker': speaker,
                'type': type_,
                'rawhtml': rawhtml,
                }
            yield event


def parse_tabular_schedule(tree):
    """Yields event dicts, parsed from the tabular schedule
    """
    for day, table in parse_days(tree):
        for event in events(table):
            event['day'] = day
            event['start'] = datetime.datetime.combine(day, event['start'])

            if event['finish'] is not None:
                event['finish'] = datetime.datetime.combine(day, event['finish'])
                event['duration'] = event['finish'] - event['start']
            yield event


def days_hours_minutes_seconds(td):
    """Returns a tuple for the number of (days, hours, minutes, seconds) in a
    `datetime.timedelta`.

    >>> days_hours_minutes_seconds(datetime.timedelta(seconds=5400))
    (0, 1, 30, 0)
    """
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return (td.days, hours, minutes, seconds)


def format_duration(duration, sep=' ', units='dhms', default='0s'):
    """Returns a minimal string, representing a `datetime.timedelta`

    >>> format_duration(datetime.timedelta(seconds=5400))
    '1h 30m'
    """
    qtys = days_hours_minutes_seconds(duration)
    result = ('%i%s' % (qty, unit) for qty, unit in zip(qtys, units) if qty)
    return sep.join(result) or default


def ordinal_suffix(i, default='th'):
    """Returns the appropriate suffix for an integer i
    """
    suffixes = {1:'st', 2:'nd', 3:'rd',
                11:'th', 12:'th', 13:'th'}
    if i in suffixes:
        return suffixes[i]
    elif i % 100 in suffixes:
        return suffixes[i % 100]
    elif i % 10 in suffixes:
        return suffixes[i % 10]
    return default


def format_day_id(day):
    """Returns a string matching the id made from schedule.rst by docutils

    >>> format_day_id(datetime.datetime(2015, 9, 18))
    'friday-18th-september-2015'
    """
    date_format = '%A-%d{suffix}-%B-%Y'.format(suffix=ordinal_suffix(day.day))
    return day.strftime(date_format).lower()


def render_schedule(schedule, template_dir):
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_dir),
        autoescape=True,
        lstrip_blocks=True,
        trim_blocks=True,
        )
    env.filters.update({
        'ordinal_suffix': ordinal_suffix,
        'days_hours_minutes_seconds': days_hours_minutes_seconds,
        'format_day_id': format_day_id,
        'format_duration': format_duration,
        })

    templ = env.get_template('flat_schedule.html')
    html = templ.render({
        'page': {
            'title': 'Schedule',
            'slug': 'schedule',
            'body_class_hack': 'talks',
            },
        'schedule': schedule,
        })
    return html


def read_html_tabular_schedule(config):
    """Returns a list of events, from a Tabular HTML schedule
    """
    tab_sched_dir = os.path.join(config['output_dir'], 'schedule', 'tabular')
    tab_sched_path = os.path.join(tab_sched_dir, 'index.html')
    tab_sched_etree = lxml.html.parse(tab_sched_path)

    return list(parse_tabular_schedule(tab_sched_etree))


def read_rst_tabular_schedule(config):
    """Returns a list of events, from a Tabular reStructuredText schedule
    """
    tab_sched_rst = io.open('content/schedule.rst', encoding='utf-8').read()
    tab_sched_rst = tab_sched_rst.split('---\n', 1)[1]
    tab_sched_html = docutils.examples.html_body(tab_sched_rst)
    tab_sched_etree = lxml.html.fromstring(tab_sched_html)

    return list(parse_tabular_schedule(tab_sched_etree))


def mkdirs(path):
    try:
        os.mkdir(path)
    except os.error as exc:
        if exc.errno != errno.EEXIST:
            raise


def write_flat_schedule(schedule, config):
    schedule_html = render_schedule(schedule, config['template_dir'])
    schedule_dir = os.path.join(config['output_dir'], 'schedule')
    schedule_path = os.path.join(schedule_dir, 'index.html')

    mkdirs(schedule_dir)
    with io.open(schedule_path, 'w', encoding='utf-8') as f:
        f.write(schedule_html)


def create_flat_schedule(config):
    schedule = read_html_tabular_schedule(config)
    write_flat_schedule(schedule, config)


if __name__ == '__main__':
    config = {'template_dir': 'templates', 'output_dir': 'output'}
    schedule = read_rst_tabular_schedule(config)
    write_flat_schedule(schedule, config)
