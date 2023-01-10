#TIME DELTA PROBLEM:

import datetime

a =  int(input())

for i in range(a):
    ts_1 = input().strip()
    ts_2 = input().strip()
    t_format = "%a %d %b %Y %H:%M:%S %z"
    tsec_1 = datetime.datetime.strptime(ts_1,t_format)
    tsec_2 = datetime.datetime.strptime(ts_2,t_format)
    print(int(abs(tsec_1-tsec_2).total_seconds()))



#My reference for this problem: 
#https://www.guru99.com/date-time-and-datetime-classes-in-python.html
#https://www.youtube.com/watch?v=eirjjyP2qcQ&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=17