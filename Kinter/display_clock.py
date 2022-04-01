from sqlite3 import Timestamp
from tkinter import *
import time

def myTime():
    timeStr = time.strftime('%I:%M:%S %p')
    dateStr = time.strftime('%A')
    
    timeLabel.config(text=timeStr)
    dateLabel.config(text=dateStr)
    dateLabel.after(1000, myTime)
    timeLabel.after(1000, myTime)


myWin = Tk()
myWin.title('Digital Clock Display')
myWin.geometry('600x200')   #width x height

timeLabel = Label(myWin, font=('Arial', 72), fg='white', bg='black')
timeLabel.pack()

dateLabel = Label(myWin, font=('Arial', 50), fg='white', bg='black')
dateLabel.pack()

myTime()

myWin.mainloop()
