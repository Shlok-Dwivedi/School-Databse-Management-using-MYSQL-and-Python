import mysql.connector as a

# Establish the connection to the database
con = a.connect(host='localhost', user='root', database='db1', password='System')
cursor = con.cursor()

# Create tables if they do not exist
tables = [
    '''CREATE TABLE IF NOT EXISTS student (
        name VARCHAR(20),
        Class INT(2),
        roll_no INT(2),
        address VARCHAR(20),
        admno INT(4) PRIMARY KEY
    );''',
    '''CREATE TABLE IF NOT EXISTS teacher (
        tcode INT(3),
        name VARCHAR(20),
        salary INT(6),
        address VARCHAR(20),
        class INT(3)
    );''',
    '''CREATE TABLE IF NOT EXISTS ClAttendance (
        Class INT(3),
        class_teacher VARCHAR(20),
        strength INT(2),
        date INT(2),
        no_absentees INT(2)
    );''',
    '''CREATE TABLE IF NOT EXISTS TAttendance (
        Name VARCHAR(20),
        date INT(2),
        attendance VARCHAR(3)
    );'''
]

# Execute table creation queries
for table in tables:
    cursor.execute(table)

def main_menu():
    print("Montfort School")
    print("1. Student")
    print("2. Teacher")
    print("3. Class Attendance")
    print("4. Teacher Attendance")
    
    table = int(input("Enter table number: "))
    print("")
    
    if table == 1:
        student_menu()
    elif table == 2:
        teacher_menu()
    elif table == 3:
        class_attendance_menu()
    elif table == 4:
        teacher_attendance_menu()
    else:
        print("Enter a valid choice!!")
        main_menu()

def student_menu():
    while True:
        print("1. Add student")
        print("2. Remove student")
        print("3. Display student details")
        print("4. Exit")
        
        task = int(input("Enter task number: "))
        
        if task == 1:
            AddSt()
        elif task == 2:
            RemoveSt()
        elif task == 3:
            DisplaySt()
        elif task == 4:
            break
        else:
            print("Enter valid choice!")

def teacher_menu():
    while True:
        print("1. Add teacher")
        print("2. Remove teacher")
        print("3. Update Salary")
        print("4. Display teacher details")
        print("5. Exit")
        
        task = int(input("Enter task number: "))
        
        if task == 1:
            AddT()
        elif task == 2:
            RemoveT()
        elif task == 3:
            UpdateSal()
        elif task == 4:
            DisplayT()
        elif task == 5:
            break
        else:
            print("Enter valid choice!")

def class_attendance_menu():
    while True:
        print("1. Class Attendance")
        print("2. Display Class Attendance details")
        print("3. Exit")
        
        task = int(input("Enter task number: "))
        
        if task == 1:
            ClAttd()
        elif task == 2:
            DisplayClAttd()
        elif task == 3:
            break
        else:
            print("Enter valid choice!")

def teacher_attendance_menu():
    while True:
        print("1. Teacher Attendance")
        print("2. Display Teacher Attendance details")
        print("3. Exit")
        
        task = int(input("Enter task number: "))
        
        if task == 1:
            Tattd()
        elif task == 2:
            DisplayTAttd()
        elif task == 3:
            break
        else:
            print("Enter valid choice!")

def AddSt():
    name = input("Student name: ")
    Class = int(input("Class: "))
    roll_no = int(input("Roll no: "))
    address = input("Address: ")
    admno = int(input("Admission no: "))
    
    cursor.execute("INSERT INTO student (name, Class, roll_no, address, admno) VALUES (%s, %s, %s, %s, %s)",
                   (name, Class, roll_no, address, admno))
    con.commit()
    print("Data entered successfully\n")
    
def RemoveSt():
    cl = int(input("Class: "))
    r = int(input("Roll no: "))
    
    cursor.execute("DELETE FROM student WHERE Class = %s AND roll_no = %s", (cl, r))
    con.commit()
    print("Data Updated\n")
    
def DisplaySt():
    cl = int(input("Class: "))
    cursor.execute("SELECT * FROM student WHERE Class = %s", (cl,))
    d = cursor.fetchall()
    
    for i in d:
        print(f"Name: {i[0]}, Class: {i[1]}, Roll no: {i[2]}, Address: {i[3]}\n")
    
def AddT():
    tcode = int(input("TCode: "))
    name = input("Teacher name: ")
    salary = int(input("Salary: "))
    address = input("Address: ")
    Class = int(input("Class: "))
    
    cursor.execute("INSERT INTO teacher (tcode, name, salary, address, class) VALUES (%s, %s, %s, %s, %s)",
                   (tcode, name, salary, address, Class))
    con.commit()
    print("Data entered successfully\n")
    
def RemoveT():
    tcode = int(input("Tcode: "))
    
    cursor.execute("DELETE FROM teacher WHERE tcode = %s", (tcode,))
    con.commit()
    print("Data Updated\n")

def UpdateSal():
    name = input("Teacher name: ")
    tcode = int(input("Tcode: "))
    salary = int(input("Salary: "))
    
    cursor.execute("UPDATE teacher SET salary = %s WHERE name = %s AND tcode = %s", (salary, name, tcode))
    con.commit()
    print("Data Updated\n")

def DisplayT():
    cursor.execute("SELECT * FROM teacher")
    d = cursor.fetchall()
    
    for i in d:
        print(f"Tcode: {i[0]}, Name: {i[1]}, Salary: {i[2]}, Address: {i[3]}, Class: {i[4]}\n")

def ClAttd():
    cl = int(input("Class: "))
    clt = input("Class teacher: ")
    t = int(input("Class strength: "))
    d = int(input("Date: "))
    ab = int(input("No of absentees: "))
    
    cursor.execute("INSERT INTO ClAttendance (Class, class_teacher, strength, date, no_absentees) VALUES (%s, %s, %s, %s, %s)",
                   (cl, clt, t, d, ab))
    con.commit()
    print("Data entered successfully\n")

def DisplayClAttd():
    cursor.execute("SELECT * FROM ClAttendance")
    d = cursor.fetchall()
    
    for i in d:
        print(f"Class: {i[0]}, Class teacher: {i[1]}, Total Students: {i[2]}, Date: {i[3]}, Absentees: {i[4]}\n")

def Tattd():
    n = input("Name: ")
    d = int(input("Date: "))
    a = input("Enter 'p' if present and 'a' if absent: ")
    
    cursor.execute("INSERT INTO TAttendance (Name, date, attendance) VALUES (%s, %s, %s)", (n, d, a))
    con.commit()
    print("Data entered successfully\n")

def DisplayTAttd():
    cursor.execute("SELECT * FROM TAttendance")
    d = cursor.fetchall()
    
    for i in d:
        print(f"Name: {i[0]}, Date: {i[1]}, Attendance: {i[2]}\n")

# Start the program
main_menu()
