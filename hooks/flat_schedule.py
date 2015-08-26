#!/usr/bin/env python

import datetime
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
    for section in tree.xpath('.//div[@class="section"]'):
        day = section.find('./h1').text
        table = section.find('./table')
        if day is not None and table is not None:
            day = parse_date(day)
            yield day, table


def collapse_whitespace(s):
    """Strips surrounding whitespace & repeated spaces from s
    """
    return re.sub(r' ', ' ', s.strip())


def iter_cells(cells):
    """Yields td or th elements, repeating them as necessary for colspan=n
    """
    for cell in cells:
        colspan = int(cell.get('colspan', 1))
        for i in xrange(colspan):
            yield cell


def parse_rooms(table):
    """Yields the rooms used in a single schedule table
    """
    row1 = iter_cells(table.xpath('./thead/tr[1]/th')[1:])
    row2 = iter_cells(table.xpath('./thead/tr[2]/th')[1:])
    for th1, th2 in itertools.izip_longest(row1, row2):
        text1 = collapse_whitespace(th1.text)
        text2 = collapse_whitespace(th2.text) if th2 is not None else ''
        if text2:
            yield '%s (%s)' % (text1, text2)
        else:
            yield text1


def parse_speaker(href):
    """Returns the speaker of a event, parsed from the Markdown abstract
    """
    m = re.match(r'/talks/(?P<slug>[a-z0-9-]+)/', href)
    if not m:
        return None
    try:
        path = 'content/talks/{}.md'.format(m.group('slug'))
    except:
        print repr(href), m.groupdict()
        raise
    try:
        with io.open(path, encoding='utf-8') as f:
            markdown = f.read(1024)
    except IOError:
        return None
    m = re.search(
        r'^### +?(?P<speaker>[\w][^\n]+?)\n',
        markdown,
        re.UNICODE | re.MULTILINE,
        )
    if m:
        return m.group('speaker')


def parse_event(td):
    """Returns the details of an event, parsed from a table cell
    """
    a = td.find('./a')
    elem = a if a is not None else td
    href = elem.get('href')
    if href is not None:
        speaker = parse_speaker(href)
    else:
        speaker = None
    if elem.text is not None:
        title = collapse_whitespace(elem.text)
    else:
        title = None
    return href, title, speaker


def events(table):
    """Yields event dicts parsed from a single schedule table
    """
    rooms = [room for room in parse_rooms(table)]
    trs = [tr for tr in table.xpath('./tbody/tr')
           if tr.find('./td').text != u'\N{NO-BREAK SPACE}']
    times = [parse_time(tr.find('./td').text) for tr in trs]

    for i, (start_time, tr) in enumerate(zip(times, trs)):
        tds = tr.xpath('./td')[1:]
        j = 0
        for td in tds:
            room = rooms[j]
            rowspan = int(td.get('rowspan', 1))
            colspan = int(td.get('colspan', 1))
            try:
                finish_time = times[i+rowspan]
            except IndexError:
                finish_time = None
            href, title, speaker = parse_event(td)
            if title:
                yield {
                    'start': start_time,
                    'finish': finish_time,
                    'href': href,
                    'location': room,
                    'title': title,
                    'speaker': speaker,
                    }
            j += colspan


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


def write_flat_schedule(config):
    schedule_dir = os.path.join(config['output_dir'], 'schedule')
    tab_sched_path = os.path.join(schedule_dir, 'index.html')
    tab_sched_etree = lxml.html.parse(tab_sched_path)

    schedule = parse_tabular_schedule(tab_sched_etree)
    schedule_html = render_schedule(schedule, config['template_dir'])

    schedule_path = os.path.join(schedule_dir, 'flat.html')
    with io.open(schedule_path, 'w', encoding='utf-8') as f:
        f.write(schedule_html)


if __name__ == '__main__':
    # Get the html of the tabular schedule
    sched_rst = io.open('content/schedule.rst', encoding='utf-8').read()
    sched_rst = sched_rst.split('---\n', 1)[1]
    sched_html = docutils.examples.html_body(sched_rst)

    # Parse the html of the tabular schedule 
    sched_etree = lxml.html.fromstring(sched_html)
    schedule = parse_tabular_schedule(sched_etree)

    with io.open('flat_schedule.html', 'w', encoding='utf-8') as f:
        f.write(html)
