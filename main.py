from time import strftime
from tkinter import *
from pygame import mixer

import time
import datetime

root = Tk()
root.title('Edem Robin')


def setalarm():
    alarmtime = f"{hrs.get()}:{mins.get()}:{secs.get()}"
    print(alarmtime)
    if(alarmtime!="::"):
        alarmclock(alarmtime)

def alarmclock(alartime):
    while True:
        time.sleep(1)
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now == alartime:
            Wakeup = Label(root, font=('arial', 20, 'bold'), text="Wakeup! Wakeup",
                           bg="DodgerBlue2", fg="White").grid(row=6, columnspan=3)
            print(Wakeup)
            mixer.init()
            mixer.music.load(r'./best_wakeup_alarm.mp3')
            mixer.music.play()
            break
hrs= StringVar()
mins = StringVar()
secs = StringVar()

greet = Label(root,font=('arial',20,'bold'),text="Time to take a nap").grid(row=1,columnspan=3)
hrsbt = Entry(root,textvariable=hrs,width=5,font=('arial',20,'bold'))
hrsbt.grid(row=2,column=1)

minsbtn = Entry(root,textvariable=mins,width=5,font=('arial',20,'bold'))
minsbtn.grid(row=2,column=2)

secsbtn = Entry(root,textvariable=secs,width=5,font=('arial',20,'bold'))
secsbtn.grid(row=2,column=3)

setbtn = Button(root, text="set alarm", command=setalarm, bg="DodgerBlue2",fg="white", font=('arial', 20, 'bold')).grid(row=4, columnspan=3)

timeleft = Label(root,font=('arial',20,'bold'))
timeleft.grid()
mainloop()
