#Calender_Module Problem

import datetime

m,d,y= map(int,input().split())
dt_date = datetime.date(y,m,d)

print(dt_date.strftime('%A').upper())

#My reference for this problem: 
#https://www.guru99.com/date-time-and-datetime-classes-in-python.html
#https://www.youtube.com/watch?v=eirjjyP2qcQ&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=17