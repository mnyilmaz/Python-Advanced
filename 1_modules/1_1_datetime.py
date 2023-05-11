# BTK Academy
# Advanced Python Programming From Zero
# Lecture 1.1: Datetime Module in Python 
# python 1_1_datetime.py
blank = "----------------------"

from datetime import datetime
import string # only imports datetime
# from datetime import date -> only imports date
# from datetime import time -> only imports time
# import datetime -> imports them all

now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
today = datetime.today()
ctime = datetime.ctime(now)
transfiguration = datetime.strftime(now, "%Y/%B/%d") # Prints Year - Month - Day
# datetime.strftime(now, "%Y") # Prints Year
# datetime.strftime(now, "%B") # Prints Month 
# datetime.strftime(now, "%d") # Prints Day as number
# datetime.strftime(now, "%A") # Prints Day as string
# datetime.strftime(now, "%X") # Prints Hour

print(f"Now: {now}")
print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Hour: {hour}")
print(f"Minute: {minute}")
print(f"Second: {second}")
print(f"Today: {today}")
print(f"Ctime: {ctime}")
print(f"Detailed one: {transfiguration}")
print(blank)

##############################################################################################################

t = "12 December 1995"
day, month, year = t.split()
print(day)
print(month)
print(year)
print(blank)

t = "12 December 1995 Hour 23:21:44"
dt = datetime.strptime(t, "%d %B %Y Hour %H:%M:%S") # 1995-12-12 23:21:44
print(dt)
print(blank)

birthday = datetime(1997, 10, 16, 16,16,00) # CL - 1997-10-16 16:16:00
scnd = datetime.timestamp(birthday) # second
brthdy = datetime.fromtimestamp(scnd) # second to time
ms = datetime.fromtimestamp(0) # milestone of computer history
rslt = now - birthday # time delta object
rslt.days # days
rslt.seconds # seconds
rslt.microseconds # microseconds

print(f"Charles was born on {birthday}") # 1997-10-16 16:16:00
print(f"Second was {scnd}") # 877007760.0
print(f"Milestone date is {ms}") # 1970-01-01 03:00:00
print(rslt) # 9059 days, 7:14:11.431754
print(blank)

##############################################################################################################

from datetime import timedelta

future = now + timedelta(days=26, minutes=3) # usage will be always the same (increasing date by day and time)
past = now - timedelta(days=26, minutes=3) # usage will be always the same (decreasing date by day and time)
print(future)
print(past)
