import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="12345",database="stm")

def check_st(stid):
    sql='select * from sut where stid=%s'
    c=con.cursor(buffered=True)
    data=(stid,)
    c.execute(sql,data)
    r=c.rowcount
    if r==1:
        return True
    else:
        return False

def check_tr(trid):
    sql='select * from tcr where trid=%s'
    c=con.cursor(buffered=True)
    data=(trid,)
    c.execute(sql,data)
    r=c.rowcount
    if r==1:
        return True
    else:
        return False

def add_st():
    print("-->> ADD STUDENT RECORD-->>")
    stid=input("Enter Student ID:")
    if(check_st(stid)):
        print("Student ID exists.")
    else:
        stname=input("Enter Student Name:")
        coursename=input("Enter Student Coursename:")
        address=input("Enter Student Address:")
        ph=input("Enter Student Phone no. :")
        batch=input("Enter Student Batch:")
        batm=input("Enter Batch Timing:")
        coursedur=input("Enter Course Duration:")
        data=(stid,stname,coursename,address,ph,batch,batm,coursedur)
        sql='insert into sut values(%s,%s,%s,%s,%s,%s,%s,%s)'
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("SUCCESSFULLY ADDED STUDENT RECORD")
    print("\n")
    press=input("Press Any Key To Continue\n")
    menu()

def add_tr():
    print("-->> ADD TEACHER RECORD-->>")
    trid=input("Enter Teacher ID:")
    if(check_tr(trid)):
        print("Teacher ID exists.")
    else:
        trname=input("Enter Teacher Name:")
        sub=input("Enter Teacher Subject:")
        address=input("Enter Teacher Address:")
        ph=input("Enter Teacher Phone no. :")
        batch=input("Enter Batch no.:")
        batm=input("Enter Batch Timing:")
        sal= int(input("Enter Teacher Salary:"))
        coursedur=input("Enter Course Duration:")
        data=(trid,trname,sub,address,ph,batch,batm,sal,coursedur)
        sql='insert into tcr values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("SUCCESSFULLY ADDED TEACHER RECORD")
    print("\n")
    press=input("Press Any Key To Continue\n")
    menu()

def display_st():
    print("-->> Display St Record <<--")
    sql = 'select * from sut'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("Student Id: ", i[0])
        print("Student Name: ", i[1])
        print("Student's Course: ", i[2])
        print("student's Address: ", i[3])
        print("Student's Phone no.: ", i[4])
        print("Student's Batch: ", i[5])
        print("Student's Batch Timing: ", i[6])
        print("\n")
    press = input("Press Any key To Continue\n")
    menu()

def display_tr():
    print("-->> Display Teacher Record <<--")
    sql = 'select * from tcr'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("Teacher Id: ", i[0])
        print("Teacher Name: ", i[1])
        print("Teacher's Subject: ", i[2])
        print("Teacher's Address: ", i[3])
        print("Teacher's Phone no.: ", i[4])
        print("Teacher's Batch: ", i[5])
        print("Teacher's Batch Timing: ", i[6])
        print("Teacher's Salary: ", i[7])
        print("\n")
    press = input("Press Any key To Continue\n")
    menu()

def remove_st():
    print("-->> Remove Student Record <<--")
    stid=input("Enter Student ID:")
    if(check_st(stid)):
        sql = 'delete from sut where stid = %s'
        data = (stid,)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Student Removed")
    else:
        print("Please enter correct StudentID")
    print("\n")
    press = input("Press Any key To Continue\n")
    menu()

def remove_tr():
    print("-->> Remove Teacher Record <<--")
    trid=input("Enter Teacher ID:")
    if(check_tr(trid)):
        sql = 'delete from tcr where trid = %s'
        data = (trid,)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Teacher Removed")
    else:
        print("Please enter correct Teacher ID")
    print("\n")
    press = input("Press Any key To Continue\n")
    menu()

def batch_st():
    print("--> Student Batch Record-->")
    stid=input("Enter Student ID:")
    if(check_st(stid)):
        sql='select stid,batch,batm from sut where stid=%s'
        data=(stid),
        c=con.cursor()
        c.execute(sql,data)
        r=c.fetchall()
        for i in r:
            print("Student ID:",i[0])
            print("Student Batch:",i[1])
            print("Student Batch Timing:",i[2])
    else:
        print("Student ID not exists.")
    print("\n")
    press = input("Press Any key To Continue\n")
    menu()

        
def batch_tr():
    print("--> Teacher Batch Record-->")
    trid=input("Enter Teacher ID:")
    if(check_tr(trid)):
        sql='select trid,batch,batm from tcr where trid=%s'
        data=(trid),
        c=con.cursor()
        c.execute(sql,data)
        r=c.fetchall()
        for i in r:
            print("Teacher ID:",i[0])
            print("Teacher Batch:",i[1])
            print("Teacher Batch Timing:",i[2])
    else:
        print("Teacher ID not exists.")
    print("\n")
    press = input("Press Any key To Continue\n")
    menu()

def course_tr():
    print("--> Teacher's Course Record-->")
    trid=input("Enter Teacher ID:")
    if(check_tr(trid)):
        sql='select trid,sub,coursedur from tcr where trid=%s'
        data=(trid),
        c=con.cursor()
        c.execute(sql,data)
        r=c.fetchall()
        for i in r:
            print("Teacher ID:",i[0])
            print("Teacher subject:",i[1])
            print("Teacher Course Duration:",i[2])
    else:
        print("Teacher ID not exists.")
    print("\n")
    press = input("Press Any key To Continue\n")
    menu()

def course_st():
    print("--> Student's Course Record-->")
    stid=input("Enter Student ID:")
    if(check_st(stid)):
        sql='select stid,coursename,coursedur from sut where stid=%s'
        data=(stid),
        c=con.cursor()
        c.execute(sql,data)
        r=c.fetchall()
        for i in r:
            print("Student ID:",i[0])
            print("Student's course:",i[1])
            print("Student's Course Duration:",i[2])
    else:
        print("Student ID not exists.")

    print("\n")
    press = input("Press Any key To Continue\n")
    menu()


def search_st_batch():
    print("-->> Search Student with batch,course Record <<--")
    stid = input("Enter Student Id: ")
    if(check_st(stid)):
        sql = 'select sut.stid,sut.stname,sut.coursename,sut.coursedur,sut.batch,sut.batm from  sut where sut.stid=%s;'
        data = (stid,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("Student Id: ", i[0])
            print("Student Name: ", i[1])
            print("Course Name: ", i[2])
            print("Course Duration: ", i[3])
            print("Student's Batch:",i[4])
            print("Batch Time:",i[5])
    else:
            print("Student Record Not exists\nTry Again")
            press = input("Press Any Key To Continue..")
            menu()

def search_tr_batch():
    print("-->> Search Teacher with course ,batch Record <<--")
    trid = input("Enter Teacher Id: ")
    if(check_tr(trid)):
        sql = 'select tcr.trid,tcr.trname,tcr.sub,tcr.coursedur,tcr.batch,tcr.batm from  tcr where tcr.trid=%s;'
        data = (trid,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("Teacher Id: ", i[0])
            print("Teacher Name: ", i[1])
            print("Course Name: ", i[2])
            print("Course Duration: ", i[3])
            print("Teacher's Batch:",i[4])
            print("Batch Time:",i[5])
    else:
            print("Teacher Record Not exists\nTry Again")
            press = input("Press Any Key To Continue..")
            menu()

def search_st_pd():
    print("-->> Search Student Record <<--")
    stid = input("Enter Student Id: ")
    if(check_st(stid)):
        sql = 'select * from sut where stid = %s'
        data = (stid,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("Student Id: ", i[0])
            print("Student Name: ", i[1])
            print("Student's Course: ", i[2])
            print("student's Address: ", i[3])
            print("Student's Phone no.: ", i[4])
    else:
        print("Student Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
   
def search_tr_pd():
    print("-->> Search Teacher Record <<--")
    trid = input("Enter Teacher Id: ")
    if(check_tr(trid)):
        sql = 'select * from tcr where trid = %s'
        data = (trid,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("Teacher Id: ", i[0])
            print("Teacher Name: ", i[1])
            print("Teacher's Subject: ", i[2])
            print("Teacher's Address: ", i[3])
            print("Teacher's Phone no.: ", i[4])
            print("Teacher's Salary: ", i[5])
            
    else:
            print("Teacher Record Not exists\nTry Again")
            press = input("Press Any Key To Continue..")
            menu()
   
        
def menu ():
    print("***************************************************")
    print("-->> WELCOME TO THE STUDENT TEACHER MANAGEMENT <<--")
    print("***************************************************")
    print("1. Add Student")
    print("2. Display Student Record")
    print("3. Remove Student Record")
    print("4. Add Teacher")
    print("5. Display Teacher Record")
    print("6. Remove Teacher Record")
    print("7. Student With Batch ,Course Details")
    print("8. Teacher With Batch ,Course Details")
    print("9. Student Personal Details")
    print("10. Teacher Personal Details")
    print("11. Student Batch Details")
    print("12. Student Course Details")
    print("13. Teacher Batch Details")
    print("14. Teacher Course Details")
    print("-->> CHOICE OPTIONS: [1/2/3/4/5/6/7/8/9/10/11/12/13/14]<<--")
    ch= int(input("Enter Your Choice:"))
    if ch==1:
        return add_st()
    elif ch==2:
        return display_st()
    elif ch==3:
        return remove_st()
    elif ch==4:
        return add_tr()
    elif ch==5:
        return display_tr()
    elif ch==6:
        return remove_tr()
    elif ch==7:
        return search_st_batch()
    elif ch==8:
        return search_tr_batch()
    elif ch==9:
        return search_st_pd()
    elif ch==10:
        return search_tr_pd()
    elif ch==11:
        return batch_st()
    elif ch==12:
        return course_st()
    elif ch==13:
        return batch_tr()
    elif ch==14:
        return course_tr()
    
    else:
        print("Wrong Input,Try Again")


def pswd():
    p=input("ENTER PASSWORD:")
    if p=="school":
        menu()
    else:
        print("WRONG PASSWORD")
        pswd()
pswd()
menu()

