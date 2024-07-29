from tkinter import *
from tkinter import messagebox
import tkinter as tk
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="12345",database="employee_2")

root =Tk()
root.title("Employee Management System")
root.geometry("600x480")
root.config(bg="lightgray")

title = Label(text='Employee Management System', font=('Arial', 25),fg="white",bg="black")
title.pack()


# Adding labels and entry fields

empid = Label(root, text="Emp ID:", font=("verdana 15"))
empid.place(x=30, y=60)
empid_entry = Entry(root, font=("verdana 15"))
empid_entry.place(x=150, y=60)
  
empname = Label(root, text="Emp Name:", font=("verdana 15"))
empname.place(x=10, y=100)
empname_entry = Entry(root, font=("verdana 15"))
empname_entry.place(x=150, y=100)
  
post = Label(root, text="Emp Post:", font=("verdana 15"))
post.place(x=10, y=140)
post_entry= Entry(root, font=("verdana 15"))
post_entry.place(x=150, y=140)

salary= Label(root, text="Emp Salary:", font=("verdana 15"))
salary.place(x=10, y=180)
salary_entry= Entry(root, font=("verdana 15"))
salary_entry.place(x=150, y=180)

def Add():
   empid = empid_entry.get()
   empname = empname_entry.get()
   post = post_entry.get()
   salary= salary_entry.get()
  
   if(empid == "" or empname == "" or post == "" or salary==""):
       messagebox.showinfo("ALERT", "Please enter all fields")
   else:
       con = mysql.connector.connect(host="localhost",user="root",password="12345",database="employee_2")
       cursor = con.cursor()
       cursor.execute("insert into employee_2 values('" + empid +"', '"+ empname +"', '" + post +"','"+ salary+"')")
       cursor.execute("commit")
  
       messagebox.showinfo("Status", "Successfully Inserted")
       con.close();

def Update():
   empid = empid_entry.get()
   empname = empname_entry.get()
   post = post_entry.get()
   salary= salary_entry.get()
  
   if(salary=="" or post==""):
       messagebox.showinfo("ALERT", "Please enter fields you want to update!")
   else:
       con = mysql.connector.connect(host="localhost",user="root",password="12345",database="employee_2")
       cursor = con.cursor()
       cursor.execute("update employee_2 set empname='"+empname+"',post='"+post+"',salary='"+salary+"' where empid ='"+empid+"'")
       cursor.execute("commit")
  
       messagebox.showinfo("Status", "Successfully Updated")
       con.close()

def Del():
  
   if(empid_entry.get() == ""):
       messagebox.showinfo("ALERT", "Please enter ID to delete employee data")
   else:
       con = mysql.connector.connect(host="localhost",user="root",password="12345",database="employee_2")
       cursor = con.cursor()
       cursor.execute("delete from employee_2 where empid='"+ empid_entry.get() +"'")
       cursor.execute("commit")
  
       empid_entry.delete(0, 'end')
       empname_entry.delete(0, 'end')
       post_entry.delete(0, 'end')
       salary_entry.delete(0,'end')
       messagebox.showinfo("Status", "Successfully Deleted")
       con.close();

def Select():
  
   if(empid_entry.get() == ""):
       messagebox.showinfo("ALERT","ID is required to select employee data!")
   else:
       con = mysql.connector.connect(host="localhost",user="root",password="12345",database="employee_2")
       cursor = con.cursor()
       cursor.execute("select * from employee_2 where empid= '" + empid_entry.get() +"'")
       rows = cursor.fetchall()
  
       for row in rows:
           empname_entry.insert(0, row[1])
           post_entry.insert(0, row[2])
           salary_entry.insert(0,row[3])
       con.close();

btnadd = Button(root, text="Add", command=Add, font=("verdana 15")).place(x=150, y=300)
btnDelete = Button(root, text="Delete", command=Del, font=("verdana 15")).place(x=240, y=300)
btnUpdate = Button(root, text="Update", command=Update, font=("verdana 15")).place(x=360, y=300)
btnSelect= Button(root, text="Select", command=Select, font=("verdana 15")).place(x=480, y=300)
  

root.mainloop()
