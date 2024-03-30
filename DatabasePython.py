import sqlite3
con=sqlite3.Connection('busproject')
cur=con.cursor()
'''cur.execute('create table Bus(Bus_ID int(2) primary key,Type varchar(10),Capacity int(2),Fare int(5),Op_ID int(2) foreign key reference Operator(Op_ID),Route_ID int(3) foreign key reference Route(Route_ID))')
cur.execute('create table Operator_ID(Op_ID int(2) primary key,Name varchar(50),Address varchar(50),Email varchar(50),Phone int(10) foreign key reference Booking(Phone))')
cur.execute('create table Route(Route_ID int(2) primary key,SName char(20),SID int(5))')
cur.execute('create table Run(Bus_ID int(2),Date DATE,Seat_Available int(5),Foreign key(Bus_ID) references Bus(Bus_ID))')
cur.execute('create table Booking(Booking_ID int(5) primary key,Phone int(10) primary key,Name_Of_Person varchar(30),Passenger_Detail varchar(50),No_Of_Seats int(5),Bus_ID int(2),Date_Of_Booking DATE(),Boarding_Time TIME(),From char(20),To char(20))')
'''
cur.execute('select * from Run')
res=cur.fetchall()
print(res)