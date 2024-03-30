from tkinter import *

from DatabasePython import cur, con
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.//Bus_for_project.png')
fr1=Frame(root)
fr1.grid(row=0,column=0,columnspan=5)
fr2=Frame(root)
fr2.grid(row=1,column=0,columnspan=9)
fr3=Frame(root)
fr3.grid(row=5,column=0,columnspan=9)
Label(fr1,image=bus).grid(row=0,column=0,padx=w//2.4)
Label(fr2,text='Online Bus Booking System',fg='red',bg='light Blue',font='arial 30 bold').grid(row=1,column=1,padx=50)
Label(fr2,text='Enter Journey Details',fg='green',bg='light green',font='arial 25 bold').grid(row=2,column=1,pady=50)
Label(fr3,text='Enter Your Mobile No:',font='arail 10 bold').grid(row=3,column=1,padx=5)
x=Entry(fr3,width=33)
x.grid(row=3,column=2)
Button(fr3,text='Check Booking').grid(row=3,column=3,padx=50)
root.mainloop()