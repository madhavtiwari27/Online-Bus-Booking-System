from tkinter import *
from tkinter.messagebox import *
from DatabasePython import cur, con
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
fr1=Frame(root)
fr1.grid(row=0,column=0,columnspan=10)
fr2=Frame(root)
fr2.grid(row=1,column=0,columnspan=10)
Label(fr1,image=bus).grid(row=0,column=0,padx=w//2.5)
Label(fr2,text='Online Bus Booking System',fg='red',bg='light Blue',font='arial 30 bold').grid(row=1,column=0,pady=40,padx=1)
Label(fr2,text='Bus Ticket',font='arial 15 bold').grid(row=2,column=0,padx=2.5)
showinfo('info','Seat Booked.......')
fr=Frame(root,relief='groove',bd=3)
fr.grid(row=4,column=0,columnspan=50,padx=(w/15,0))
Label(fr,text='Passengers :',font='Arial 10 bold').grid(row=3,column=1)
Label(fr,text='Gender :',font='Arial 10 bold').grid(row=3,column=4)
Label(fr,text='No of seats:',font='Arial 10 bold').grid(row=4,column=1)
Label(fr,text='Phone:',font='Arial 10 bold').grid(row=4,column=4)
Label(fr,text='Age :',font='Arial 10 bold').grid(row=5,column=1)
Label(fr,text='Fare Rs :',font='Arial 10 bold').grid(row=5,column=4)
Label(fr,text='Booking Ref :',font='Arial 10 bold').grid(row=6,column=1)
Label(fr,text='Bus Detail :',font='Arial 10 bold').grid(row=6,column=4)
Label(fr,text='Travel on :',font='Arial 10 bold').grid(row=7,column=1)
Label(fr,text='Booked On :',font='Arial 10 bold').grid(row=7,column=4)
Label(fr,text='No of Seats:',font='Arial 10 bold').grid(row=8,column=1)
Label(fr,text='Boarding point :',font='Arial 10 bold').grid(row=8,column=4)
Label(fr,text='* Total amount of Rs 1000.00/- to be paid at the time of boarding',font='Arial 8').grid(row=9,columnspan=100,pady=10)
root.mainloop()