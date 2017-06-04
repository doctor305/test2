# -*- coding: utf-8 -*-

from Tkinter import *
##from time import sleep
import os



def shutdown():
    try:
        if e_h.get()=='':
            h = 0
        else:
            h = int(e_h.get())
        if e_m.get()=='':
            m = 0
        else:
            m = int(e_m.get())
        s = 60*m+3600*h
        os.system('shutdown -a')
        os.system('shutdown -s -t %d' %s )
        m1  = s/60
        canvas.delete('text')
        canvas.create_text(290,100,text="%d 分钟后自动关机" %m1,\
                           font='楷体 -30 bold',fill='yellow',tags='text')
    except:
        canvas.delete('text')
        canvas.create_text(290,100,text="输入有误，请输入合法的数字！",\
                           font='楷体 -30 bold',fill='yellow',tags='text')
    
    

def noshutdown():
    os.system('shutdown -a')
    canvas.delete('text')
    canvas.create_text(290,100,text="自动关机已取消！",\
                       font='楷体 -30 bold',fill='yellow',tags='text')



windows = Tk()
windows.maxsize(600,300)
windows.minsize(600,300)
windows.title("自动关机")

frame1 = Frame(windows,relief=GROOVE,borderwidth=10)
frame2 = Frame(windows,borderwidth=5)
frame3 = Frame(windows,borderwidth=5)

canvas = Canvas(frame1,bg='blue',width=580,height=200)
e_h = Entry(frame2)
lab_h = Label(frame2,text='小时')
e_m = Entry(frame2)
e_h.insert(0,0)
e_m.insert(0,0)
lab_m = Label(frame2,text='分钟后自动关机')
button1 = Button(frame3,text='自动关机',command=shutdown)
button2 = Button(frame3,text='取消关机',command=noshutdown)

frame1.pack()
frame2.pack()
frame3.pack()
canvas.pack()
e_h.pack(side=LEFT)
lab_h.pack(side=LEFT)
e_m.pack(side=LEFT)
lab_m.pack(side=RIGHT)

button1.pack(side=LEFT)
button2.pack()

windows.mainloop()
