#importing mysql connector
import mysql.connector
#making connection
con=mysql.connector.connect(host="localhost",user="root",password="12345",database="employee_2")
def check_employee(empid):
    sql='select * from employee_2 where empid=%s'
    c=con.cursor(buffered=True)
    data=(empid,)
    c.execute(sql,data)
    r=c.rowcount
    if r==1:
        return True
    else:
        return False

def add_employee():
    print("-->> ADD EMPLOYEE RECORD-->>")
    empid=input("Enter Employee ID:")
    if(check_employee(empid)):
        print("EmployeeID exists.")
    else:
        empname=input("Enter Employee Name:")
        post=input("Enter Employee Post:")
        salary=int(input("Enter Empoyee Salary:"))
        data=(empid,empname,post,salary)
        sql='insert into employee_2 values(%s,%s,%s,%s)'
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("SUCCESSFULLY ADDED EMPLOYEE RECORD")
    print("\n")
    press=input("Press Any Key To Continue\n")
    menu()

def display_employee():
    print("-->> Display Employee Record <<--")
    sql = 'select * from employee_2'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("Employee Id: ", i[0])
        print("Employee Name: ", i[1])
        print("Employee Post: ", i[2])
        print("Employee Salary: ", i[3])
        print("\n")
    press = input("Press Any key To Continue\n")
    menu()

def remove_employee():
    print("-->> Remove Employee Record <<--")
    empid=input("Enter Employee ID:")
    if(check_employee(empid)):
        sql = 'delete from employee_2 where empid = %s'
        data = (empid,)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Employee Removed")
    else:
        print("Please enter correct EmployeeID")
    print("\n")
    press = input("Press Any key To Continue\n")
    menu()

def search_employee():
    print("-->> Search Employee Record <<--")
    empid = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if(check_employee(empid)):
        sql = 'select * from employee_2 where empid = %s'
        data = (empid,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Post: ", i[2])
            print("Employee Salary: ", i[3])
    else:
            print("Employee Record Not exists\nTry Again")
            press = input("Press Any Key To Continue..")
            menu()
   
        
def menu ():
    print("************************************")
    print("-->> EMPLOYEE MANAGEMENT SYSTEM <<--")
    print("************************************")
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Remove Employee Record")
    print("-->> CHOICE OPTIONS: [1/2/3/4]<<--")
    ch= int (input("Enter Your Choice:"))
    if ch==1:
        return add_employee()
    elif ch==2:
        return display_employee()
    elif ch==3:
        return remove_employee()
    elif ch==4:
        return search_employee()
    
    else:
        print("Wrong Input,Try Again")
                
menu()
