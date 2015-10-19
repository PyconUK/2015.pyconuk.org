#! /usr/bin/env python

"""Hook to generate a csv file for upload to guidebook.com."""

import codecs
import csv
import cStringIO
import io
import os

from flat_schedule import (mkdirs,
                           read_html_tabular_schedule)


# These are the event types that seem to have descriptions in
# markdown files. We use these descriptions to fill the description
# field in the csv file
EVENT_TYPES = {'demo', 'workshop', 'talk', 'panel'}


class UnicodeWriter(object):

    # https://docs.python.org/2.7/library/csv.html#writer-objects

    def __init__(self, f, dialect=csv.excel, encoding='utf-8', **kwds):
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode('utf-8') for s in row])
        data = self.queue.getvalue()
        data = data.decode('utf-8')
        data = self.encoder.encode(data)
        self.stream.write(data)
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


def write_csv_schedule(schedule, config):
    schedule_dir = os.path.join(config['output_dir'], 'schedule', 'csv')
    schedule_path = os.path.join(schedule_dir, 'schedule.csv')

    headings = ['Don\'t change any of these headers!', 'Session Title', 'Date',
                'Time Start', 'Time End', 'Room/Location',
                'Schedule Track (Optional)', 'Description (Optional)']

    mkdirs(schedule_dir)
    with io.open(schedule_path, 'wb') as csvfile:
        writer = UnicodeWriter(csvfile)
        writer.writerow(headings)
        for talk in schedule:
                writer.writerow(make_row(talk, config))


def make_row(talk, config):
    row = ['']          # First column is always empty.
    row.append(talk['title'])
    # Although yyyy-mm-dd seems to work, guidebook recommend mm-dd-yyyy.
    row.append(talk['start'].strftime('%m-%d-%Y'))
    row.append(talk['start'].strftime('%H:%M'))
    try:
        finish_time = talk['finish'].strftime('%H:%M')
    except AttributeError:
        finish_time = '23:59'
    row.append(finish_time)
    row.append(talk['location'])
    row.append('')      # Track column
    row.append(extract_description(talk, config))
    return row


def extract_description(talk, config):
    if talk['type'] in EVENT_TYPES:
        path = os.path.join(config['content_dir'], talk['href'].strip('/') + '.md')
        with open(path) as f:
            text = f.read().decode('utf-8')
        # Remove metadata if present.
        idx = text.find('###')
        if idx != -1:
            return text[idx+3:].strip()
        return text
    return ''


def create_csv_schedule(config):
    schedule = read_html_tabular_schedule(config)
    write_csv_schedule(schedule, config)


if __name__ == '__main__':
    config = {
            'template_dir': 'templates',
            'output_dir': 'output',
            'content_dir': 'content'
    }
    schedule = read_html_tabular_schedule(config)
    write_csv_schedule(schedule, config)
