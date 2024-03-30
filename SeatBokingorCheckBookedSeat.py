from tkinter import *
from DatabasePython import cur, con
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=3,padx=w//2.5)
def seatbooking():
    root.destroy()
    import Enterjourneydetails
def checkbookedseat():
    root.destroy()
    import CheckYourBooking
def admin():
    root.destroy()
    import AddNewDetailToDataBase
Label(root,text='Online Bus Booking System',fg='red',bg='light Blue',font='arial 30 bold').grid(row=1,column=1,pady=40)
Button(root,text='Seat Booking',bg='green',font='arial 20 bold',command=seatbooking).grid(row=2,column=0,pady=50)
Button(root,text='Check Booked Seat',bg='green',font='arial 20 bold',command=checkbookedseat).grid(row=2,column=1,pady=50)
Button(root,text='Add Bus Details',bg='dark green',font='arial 20 bold',command=admin).grid(row=2,column=2,pady=50)
Label(root,text='For Admin Only',fg='red',font='arial 20 bold').grid(row=3,column=2)
root.mainloop()