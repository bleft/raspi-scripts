# script called from cron
# usage /usr/bin/python test >> output.log
# TODO: get current temp and humid from DTH11

import datetime
now = datetime.datetime.now()
timestring = str(now)
temp = 23.5
humid = 17
now = datetime.date
print(timestring, ";", temp, ";", humid)