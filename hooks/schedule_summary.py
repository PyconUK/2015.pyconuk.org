#! /usr/bin/env python

"""Hook to generate a CSV file summarising the schedule so that we can easily
see which sessions have changed and who needs to be notified.

There's a lot of copying and pasting from Kev's guidebook.py.
"""

import codecs
import csv
import io
import os

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO
    

from flat_schedule import mkdirs, read_html_tabular_schedule


EVENT_TYPES = {'demo', 'workshop', 'talk', 'panel'}


class UnicodeWriter(object):

    # https://docs.python.org/2.7/library/csv.html#writer-objects

    def __init__(self, f, dialect=csv.excel, encoding='utf-8', **kwds):
        self.queue = StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode('utf-8') for s in row])
        data = self.queue.getvalue()
        data = self.encoder.encode(data)
        self.stream.write(data)
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


def write_summary_schedule(schedule, config):
    schedule_dir = os.path.join(config['output_dir'], 'schedule', 'summary')
    schedule_path = os.path.join(schedule_dir, 'summary.csv')

    mkdirs(schedule_dir)

    headings = ['Title', 'Speaker', 'Date', 'Time', 'Room']

    with io.open(schedule_path, 'wb') as csvfile:
        writer = UnicodeWriter(csvfile)
        writer.writerow(headings)
        for talk in schedule:
                writer.writerow(make_row(talk, config))


def make_row(talk, config):
    title = talk['title']
    speaker = extract_speaker(talk, config)
    date = talk['start'].strftime('%Y-%m-%d')
    time = talk['start'].strftime('%H:%M')
    room = talk['location']

    return [title, speaker, date, time, room]


def extract_speaker(talk, config):
    if talk['type'] in EVENT_TYPES:
        path = os.path.join(config['content_dir'], talk['href'].strip('/') + '.md')
        with open(path) as f:
            for line in f:
                if line[:4] == '### ':
                    return line[4:].strip()
    return ''


def create_summary_schedule(config):
    schedule = read_html_tabular_schedule(config)
    write_summary_schedule(schedule, config)


if __name__ == '__main__':
    config = {
            'template_dir': 'templates',
            'output_dir': 'output',
            'content_dir': 'content'
    }
    create_summary_schedule(config)
