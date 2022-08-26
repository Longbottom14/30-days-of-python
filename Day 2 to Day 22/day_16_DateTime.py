from datetime import datetime
print(dir(datetime))
#Get the current day, month, year, hour, minute and timestamp from datetime module
print('\n 1. Get the current day, month, year, hour, minute and timestamp from datetime module\n')
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print('now: ',now)
print("day: ",day)
print('month: ',month)
print('year: ',year)
print('hour: ',hour)
print('minute: ',minute)
print('timestamp: ',timestamp)

#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print('\n 2.Format the current date using this format: "%m/%d/%Y, %H:%M:%S")\n')
#string for time
t = now.strftime("%m/%d/%Y, %H:%M:%S")
print('Using strftime: ',t)

#Today is 5 December, 2019. Change this time string to time.
print('\n 3.Today is 5 December, 2019. Change this time string to time.\n')
#t = now.strptime()
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print('Using strptime on\' 5 December, 2019 \' : ',date_object)
from datetime import date
#Calculate the time difference between now and new year.
print('\n 4. Calculate the time difference between now and new year.\n')
new_year = date(2023,1,1)
print('difference : ',new_year -date.today())

#Calculate the time difference between 1 January 1970 and now.
print('\n 5. Calculate the time difference between 1 January 1970 and now.\n')
#Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC.
now = datetime.now()
print("Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC.\n",': ',now.timestamp())


