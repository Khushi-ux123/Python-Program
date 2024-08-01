from tkinter import *
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="12345",database="employee_2")
import time

def clickok():
    con=mysql.connector.connect(host="localhost",user="root",password="12345",database="student")
    c=con.cursor()
    num=e.get()
    num=int(num)
    try:
        c.execute(f'Delete from exam_record where Roll_no={num}')
        con.commit()
        con.close()
        l2=Label(deletewin,fg="red",text="Deleted Successfully",font=("Helvetica",10)).place(x=6,y=115)
    

        # l2=Label(deletewin,fg="red",text="No Such Record Found",font=("Helvetica",10)).place(x=6,y=115)        

    finally:
        deletewin.after(3000,lambda:deletewin.destroy())       
def recdelete():
    global deletewin
    deletewin=Toplevel(root)
    global e
    e=Entry(deletewin,font=("Helvetica",12))
    e.place(x=5,y=40)
    l=Label(deletewin,font=("Helvetica",12),text="Please Enter Roll No",fg="purple").place(x=5,y=10)
    global button
    button=Button(deletewin,text="OK",command=lambda:clickok(),font=("Helvetica",10),bg="lightpink",fg="purple",borderwidth=0).place(x=100,y=150)
    
def yesclk():
    con=mysql.connector.connect(host="localhost",user="root",password="12345",database="student")
    c=con.cursor()
    c.execute("DELETE FROM exam_record")
    newwind.destroy()
    con.commit()
    con.close()
def clearall():
    global newwind
    newwind=Toplevel(root)
    newwind.geometry('200x200')
    yesbtn=Button(newwind,font=("Helvetica",12),text="Yes",borderwidth=0,bg="lightpink",fg="purple",command=yesclk).place(x=7,y=160)
    nobtn=Button(newwind,font=("Helvetica",12),text="No",borderwidth=0,bg="lightpink",fg="purple",command=lambda:newwind.destroy()).place(x=160,y=160)
    label1=Label(newwind,font=("Arial",15),text="Are You Sure?",fg="purple").place(x=15,y=25)

def clicksubmit():
    con=mysql.connector.connect(host="localhost",user="root",password="12345",database="student")
    c=con.cursor()

    Name=name.get()
    Roll_no=roll_no.get()
    Maths=maths.get()
    Physics=physics.get()
    Chemistry=chemistry.get()
    Gender=""
    gen=var.get()
    if(gen==1):
        Gender+="Male"
    else:
        Gender+="Female"
    c.execute("INSERT INTO exam_record values('" + Name +"', '"+ Roll_no +"', '" + Gender +"','"+ Maths+"','"+ Physics+"','"+Chemistry+"')")
    con.commit()
    con.close()
    
root=Tk()
root.geometry('1000x500')
root.title('Exam Records')
var=IntVar()
con=mysql.connector.connect(host="localhost",user="root",password="12345",database="student")
c=con.cursor()
# Creating Labels
header=Label(root,font=("Arial",15),fg="purple",text="Exam Records").place(x=210,y=30)
name_label=Label(root,font=("Helvetica",12),fg="purple",text="Name").place(x=69,y=120)
gender=Label(root,font=("Helvetica",12),fg="purple",text="Gender").place(x=69,y=164)
roll=Label(root,font=("Helvetica",12),fg="purple",text="Roll Number").place(x=69,y=208)
mathsl=Label(root,font=("Helvetica",12),fg="purple",text="Mathematics").place(x=69,y=250)
Physicsl=Label(root,font=("Helvetica",12),fg="purple",text="Physics").place(x=69,y=290)
Chemistryl=Label(root,font=("Helvetica",12),text="Chemistry",fg="purple").place(x=69,y=330)

# Creating Entry Boxes
global Name,rbutton1,rbutton2,Roll_no,Maths,Physics,Chemistry
name=Entry(root,font=("Helvetica",12),width=27,bg="lightblue")
rbutton1=Radiobutton(root,font=("Helvetica",12),fg="red",variable=var,value=1,text="Male")
rbutton2=Radiobutton(root,font=("Helvetica",12),fg="green",variable=var,value=2,text="Female")
roll_no=Entry(root,font=("Helvetica",12),width=27,bg="lightblue")
maths=Entry(root,font=("Helvetica",12),width=27,bg="lightblue")
physics=Entry(root,font=("Helvetica",12),width=27,bg="lightblue")
chemistry=Entry(root,font=("Helvetica",12),width=27,bg="lightblue")
# Placing Widgets
name.place(x=170,y=122)
rbutton1.place(x=170,y=164)
rbutton2.place(x=250,y=164)
roll_no.place(x=170,y=207)
maths.place(x=170,y=249)
physics.place(x=170,y=289)
chemistry.place(x=170,y=329)
# Create a Submit Button , Delete Record , Clear Data Base
submit=Button(root,font=("Arial",15),fg="white",bg="purple",text="Submit",borderwidth=0,command=lambda:clicksubmit()).place(x=242,y=369)
con.commit()
con.close()
delete=Button(root,font=("Helvetica",12),bg="green",fg="white",text="Delete A Record",borderwidth=0,command=recdelete).place(x=220,y=410)
frame=Frame(root,bg="lightpink",width=500,height=500).place(x=500,y=0)
clearEntry=Button(root,font=("Helvetica",12),text="Clear Database",bg="red",fg="white",borderwidth=0,command=clearall).place(x=223,y=450)
# Frame Buttons
def mathres():
    newwind=Toplevel(root)
    lab_header1=Label(newwind,text="Name",font=("Helvetica",10),fg="purple",bg="lightpink").place(x=2,y=0)
    lab_header2=Label(newwind,text="Roll Number",font=("Helvetica",10),fg="purple",bg="lightpink").place(x=152,y=0)
    lab_header3=Label(newwind,text="Marks Obtained",font=("Helvetica",10),fg="purple",bg="lightpink").place(x=302,y=0)
    newwind.geometry('400x400')
    con=mysql.connector.connect(host="localhost",user="root",password="12345",database="student")
    cursor=con.cursor()
    cursor.execute("SELECT Name,Roll_no,Maths FROM exam_record ORDER BY Maths desc")
    rows = cursor.fetchall()
    x1=2 
    y1=30
    for row in rows:
        Name=row[0]
        Roll_no=row[1]
        Math=row[2]
        lab1=Label(newwind,font=("Helvetica",10),fg="purple",bg="lightpink",highlightcolor="purple",text=Name).place(x=x1,y=y1)
        lab2=Label(newwind,font=("Helvetica",10),fg="purple",bg="lightpink",highlightcolor="purple",text=str(Roll_no)).place(x=x1+150,y=y1)
        lab3=Label(newwind,font=("Helvetica",10),fg="purple",bg="lightpink",highlightcolor="purple",text=str(Math)).place(x=x1+300,y=y1)
        y1+=30

def chemres():
    newwind=Toplevel(root)
    lab_header1=Label(newwind,text="Name",font=("Helvetica",10),fg="purple",bg="lightpink").place(x=2,y=0)
    lab_header2=Label(newwind,text="Roll Number",font=("Helvetica",10),fg="purple",bg="lightpink").place(x=152,y=0)
    lab_header3=Label(newwind,text="Marks Obtained",font=("Helvetica",10),fg="purple",bg="lightpink").place(x=302,y=0)
    newwind.geometry('400x400')
    con=mysql.connector.connect(host="localhost",user="root",password="12345",database="student")
    cursor=con.cursor()
    cursor.execute("SELECT Name,Roll_no,Chemistry FROM exam_record ORDER BY Chemistry desc")
    rows = cursor.fetchall()
    x1=2 
    y1=30
    for row in rows:
        Name=row[0]
        Roll_no=row[1]
        Chemistry=row[2]
        lab1=Label(newwind,font=("Helvetica",10),fg="purple",bg="lightpink",highlightcolor="purple",text=Name).place(x=x1,y=y1)
        lab2=Label(newwind,font=("Helvetica",10),fg="purple",bg="lightpink",highlightcolor="purple",text=str(Roll_no)).place(x=x1+150,y=y1)
        lab3=Label(newwind,font=("Helvetica",10),fg="purple",bg="lightpink",highlightcolor="purple",text=str(Chemistry)).place(x=x1+300,y=y1)
        y1+=30
 
def phyres():
    newwind=Toplevel(root)
    lab_header1=Label(newwind,text="Name",font=("Helvetica",10),fg="purple",bg="lightpink").place(x=2,y=0)
    lab_header2=Label(newwind,text="Roll Number",font=("Helvetica",10),fg="purple",bg="lightpink").place(x=152,y=0)
    lab_header3=Label(newwind,text="Marks Obtained",font=("Helvetica",10),fg="purple",bg="lightpink").place(x=302,y=0)
    newwind.geometry('400x400')
    con=mysql.connector.connect(host="localhost",user="root",password="12345",database="student")
    cursor=con.cursor()
    cursor.execute("SELECT Name,Roll_no,Physics FROM exam_record ORDER BY Physics desc")
    rows = cursor.fetchall()
    x1=2 
    y1=30
    for row in rows:
        Name=row[0]
        Roll_no=row[1]
        Physics=row[2]
        lab1=Label(newwind,font=("Helvetica",10),fg="purple",bg="lightpink",highlightcolor="purple",text=Name).place(x=x1,y=y1)
        lab2=Label(newwind,font=("Helvetica",10),fg="purple",bg="lightpink",highlightcolor="purple",text=str(Roll_no)).place(x=x1+150,y=y1)
        lab3=Label(newwind,font=("Helvetica",10),fg="purple",bg="lightpink",highlightcolor="purple",text=str(Physics)).place(x=x1+300,y=y1)
        y1+=30

button1=Button(frame,text="Display Maths Results",bg="purple",fg="white",font=("Helvetica",15),command=lambda:mathres(),borderwidth=0).place(x=500,y=50)
button2=Button(frame,text="Display Physics Results",bg="purple",fg="white",font=("Helvetica",15),command=phyres,borderwidth=0).place(x=500,y=95)
button3=Button(frame,text="Display Chemistry Results",bg="purple",fg="white",font=("Helvetica",15),borderwidth=0,command=chemres).place(x=500,y=140)

root.mainloop()
