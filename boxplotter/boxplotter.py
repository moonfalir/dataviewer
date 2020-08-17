import matplotlib.pyplot as plt
import sys
import os
import json
import numpy

if len(sys.argv) < 2:
    print("Usage: python3 boxplotter.py <qlogfile>")

filename = sys.argv[1]
if not os.path.isfile(filename):
    print("qlogfile does not exist")

print(filename)
qlogfile = open(filename, 'r')
qlog = json.load(qlogfile)

trace = qlog["traces"][0]["events"]

rtts = []
rttvars = []
qlogtunit = "ms"
event_fields = [x.lower() for x in qlog["traces"][0]["event_fields"]]
# get time unit
if "configuration" in qlog["traces"][0] and "time_units" in qlog["traces"][0]["configuration"]:
    qlogtunit = qlog["traces"][0]["configuration"]["time_units"]
try:
    event_type_id = event_fields.index("event_type")
except ValueError as e:
    event_type_id = event_fields.index("event")
data_id = event_fields.index("data")

# loop through events to find CWND values
for event in trace:
    if event[event_type_id] == "metrics_updated":
        if "rtt_variance" in event[data_id]:
            val = float(event[data_id]["rtt_variance"])
            if qlogtunit == "us":
                val = val / 1000
            rttvars.append(val)
        if "latest_rtt" in event[data_id]:
            val2 = float(event[data_id]["latest_rtt"])
            if qlogtunit == "us":
                val2 = val2 / 1000
            rtts.append(val2)


fig = plt.figure()
# Create an axes instance
ax = fig.add_subplot(111)
# Create the boxplot
bp = ax.boxplot(rtts)
#print(numpy.mean(rtts), numpy.var(rtts))
plt.show()