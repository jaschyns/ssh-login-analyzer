import csv
from datetime import datetime
from collections import namedtuple

LogEntry = namedtuple('LogEntry', ['timestamp', 'user', 'ip', 'status'])

def parse_csv(path):
    """
    Read a CSV of SSH attempts and return a list of LogEntry.
    """
    entries = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ts = datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S')
            entries.append(LogEntry(ts, row['user'], row['ip'], row['status']))
    return entries
