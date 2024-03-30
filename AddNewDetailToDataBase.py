from tkinter import *
from DatabasePython import cur, con
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
fr1=Frame(root)
fr1.grid(row=0,column=0,columnspan=10)
fr2=Frame(root)
fr2.grid(row=1,column=0,columnspan=10)
fr3=Frame(root)
fr3.grid(row=3,column=0,columnspan=10)
Label(fr1,image=bus).grid(row=0,column=0,padx=w//2.4)
def addoperator():
    root.destroy()
    import AddBusOperatorDetails
def addbusdetails():
    root.destroy()
    import AddBusDetails
def addbusroutedeatials():
    root.destroy()
    import AddBusRouteDetails
def addbusrunningdetails():
    root.destroy()
    import AddBusRunningDetails
Label(fr2,text='Online Bus Booking System',fg='red',bg='light Blue',font='arial 30 bold').grid(row=1,column=1)
Label(fr2,text='Add New Details To DataBase',fg='green',font='arial 20 bold').grid(row=2,column=1,pady=w//30)
Button(fr3,text= "New operator",bg="light green",font="arial 20 bold",command=addoperator).grid(row=3,column=0,padx=50)
Button(fr3,text= "New Bus",bg="orange red",font="arial 20 bold",command=addbusdetails).grid(row=3,column=1,padx=50)
Button(fr3,text= "New Route",bg="light blue",font="arial 20 bold",command=addbusroutedeatials).grid(row=3,column=2,padx=50)
Button(fr3,text= "New Run",bg="Indian Red",font="arial 20 bold",command=addbusrunningdetails).grid(row=3,column=3,padx=50)
root.mainloop()