from os import system
import win32api 
from datetime import datetime

week_days = ("Mon","Tue","Wed","Thur","Fri","Sat","Sun")

now = datetime.now()
year = now.year
month = now.month

win32api.SetSystemTime(year,month,3,1,2,30,3,100)
n = 28 # feb = 28

for i in range(n):
    #input("press enter"
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    sec = now.second
    week_day = now.weekday()
    win32api.SetSystemTime(year,month,week_day,day+1,0,0,0,0)
    print("Day : ",week_days[datetime.now().weekday()])
    system("py repair_brain_gui_2.0.pyw")