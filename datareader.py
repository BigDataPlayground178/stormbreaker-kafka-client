"""
This routines ensure the correct data reading in order to produce
sequential events.
"""

from datetime import datetime
from constants import DATETIME_FORMAT

def readEventSource(path, topic, records):

    with open(path) as dataset:
        # reading dataset entries
        for l in dataset.readlines():
            line = l.split("|")

            # retrieving timestamp
            ts = datetime.strptime(line[0][:- 5], DATETIME_FORMAT).timestamp()

            # preparing and setting event tuple
            record = (topic, line[0], l)
            if (ts in records):
                records[ts].append(record)
            else:
                records[ts] = [record]

def combiningEventSources(sources):
    records = dict()
    
    # combining events 
    for source in sources:
        print("[DATA READER] READING SOURCE", source)
        readEventSource(source[0], source[1], records)

    print("[DATA READER] READ COMPLETE")
    
    # returning tuple (sorted_timestamps, records)
    return sorted(records.keys()), records
            

