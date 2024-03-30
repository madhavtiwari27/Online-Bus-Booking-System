from tkinter import *

from DatabasePython import cur, con

root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
home=PhotoImage(file='home.png')
bus=PhotoImage(file='.\\Bus_for_project.png')
fr1=Frame(root)
fr1.grid(row=0,column=0,columnspan=10)
fr2=Frame(root)
fr2.grid(row=1,column=0,columnspan=10)
fr3=Frame(root)
fr3.grid(row=2,column=0,columnspan=10)
Label(fr1,image=bus).grid(row=0,column=1,padx=w//2.5)
Label(fr2,text='Online Bus Booking System',fg='red',bg='light Blue',font='arial 30 bold').grid(row=1,column=1,pady=w//40)
Label(fr2,text='Add Bus Operator Details',fg='green',font='arial 20 bold').grid(row=2,column=1,pady=w//40)
Label(fr3,text='Operator id',font='arial 20 bold').grid(row=3,column=0,padx=5)
x=Entry(fr3)
x.grid(row=3,column=1,padx=5)
Label(fr3,text='Name',font='arial 20 bold').grid(row=3,column=2,padx=5)
y=Entry(fr3)
y.grid(row=3,column=3,padx=5)
Label(fr3,text='Address',font='arial 20 bold').grid(row=3,column=4,padx=5)
z=Entry(fr3)
z.grid(row=3,column=5,padx=5)
Label(fr3,text='Phone',font='arial 20 bold').grid(row=3,column=6,padx=5)
a=Entry(fr3)
a.grid(row=3,column=7,padx=5)
Label(fr3,text='Email',font='arial 20 bold').grid(row=3,column=8,padx=5)
b=Entry(fr3)
b.grid(row=3,column=9,padx=5)
def addinfo():
    Label(fr3,text=int(x.get())).grid(row=4,column=2)
    Label(fr3,text=str(y.get())).grid(row=4, column=3)
    Label(fr3,text=z.get()).grid(row=4, column=4)
    Label(fr3,text=int(a.get())).grid(row=4, column=5)
    Label(fr3,text=b.get()).grid(row=4, column=6)
    operatorid = x.get()
    name = y.get()
    address = z.get()
    phone = a.get()
    email = b.get()
    cur.execute('insert into Operator_ID(Op_ID,Name,Address,Phone,Email) values(?,?,?,?,?)',(operatorid,name,address,phone,email))
    con.commit()
def home2():
    root.destroy()
    import AddNewDetailToDataBase
def edit():
    operatorid = x.get()
    name = y.get()
    address = z.get()
    phone = a.get()
    email = b.get()
    cur.execute('update operator_id set Name=?,Address=?,Phone=?,Email=? where op_id=?',(name, address, phone, email,operatorid))
    con.commit()
Button(fr3,text='Add',font='arial 15 bold',bg='green',command=addinfo).grid(row=3,column=10,padx=5)
Button(fr3,text='Edit',font='arial 15 bold',bg='green',command=edit).grid(row=3,column=11,padx=5)
Button(fr3,image=home,command=home2).grid(row=5,column=8,pady=50)
root.mainloop()