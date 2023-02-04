import datetime
import pytz

date = datetime.datetime.now()
print(f"Local Timezone - ", date.strftime("%d/%m/%Y, %H:%M:%S"))

# Timezone of Newyork
#print(pytz.all_timezones)
tz_NY = pytz.timezone("America/New_York")
date_NY = datetime.datetime.now(tz_NY)
print(f"NewYork Timezone - ", date_NY.strftime("%d/%m/%Y, %H:%M:%S"))


tz_JA = pytz.timezone("Japan")
date_JA = datetime.datetime.now(tz_JA)
print(f"Japan Timezone - ", date_JA.strftime("%d/%m/%Y, %H:%M:%S"))


# date = datetime.datetime.now()
# print(date)
#
# time = date.strftime("%H-%M-%S")
# print(time)
# print(date.strftime("%m/%d/%Y, %H:%M:%S"))
# print(date.strftime("%d/%m/%Y, %H:%M:%S"))

# get the current date and time
# date = datetime.datetime.now()
#date = datetime.date.today()
# print(date)
#
# print(f"Current Year, ", date.year)
# print(f"Current Month, ", date.month)
# print(f"Current Day, ", date.day)

# print(dir(datetime))