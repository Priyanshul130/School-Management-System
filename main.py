# DEVELOPED BY <PRIYANSHUL SHARMA>
# WEBPAGE Priyanshul.is-a.dev

import mysql.connector as pymysql
passwrd = None
db = None  
C = None

def base_check():
    check = 0
    db = pymysql.connect(host="localhost", user="root", password=passwrd)
    cursor = db.cursor()
    cursor.execute('SHOW DATABASES')
    result = cursor.fetchall()
    for r in result:
        for i in r:
            if i == 'school_management':
                cursor.execute('USE school_management')
                check = 1
    if check != 1:
        create_database()


def table_check():
    db = pymysql.connect(host="localhost", user="root", password=passwrd)
    cursor = db.cursor()
    cursor.execute('SHOW DATABASES')
    result = cursor.fetchall()
    for r in result:
        for i in r:
            if i == 'school_management':
                cursor.execute('USE school_management')
                cursor.execute('SHOW TABLES')
                result = cursor.fetchall()
                if len(result) <= 3:
                    create_tables()
                else:
                    print('      Booting systems...')

def create_database():
    try:
        db = pymysql.connect(host="localhost", user="root", password=passwrd)
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS school_management")
        db.commit()
        db.close()
        print("Database 'school_management' created successfully.")
    except pymysql.Error as e:
        print(f"Error creating database: {str(e)}")

def create_tables():
    try:
        db = pymysql.connect(host="localhost", user="root", password=passwrd, database="school_management")
        cursor = db.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                STUDENT_ID INT PRIMARY KEY,
                NAME VARCHAR(255),
                DOB DATE,
                CLASS VARCHAR(50)
            )
        """)
    


        cursor.execute("""
            CREATE TABLE IF NOT EXISTS teachers (
                TEACHER_ID INT PRIMARY KEY,
                NAME VARCHAR(255),
                SUBJECT VARCHAR(255),
                PHONE_NO VARCHAR(15)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS classes (
                CLASS_ID INT PRIMARY KEY,
                CLASS_NAME VARCHAR(255),
                SCHEDULE VARCHAR(255)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS grades (
                GRADE_ID INT AUTO_INCREMENT PRIMARY KEY,
                STUDENT_ID INT,
                CLASS_ID INT,
                GRADE VARCHAR(5),
                FOREIGN KEY (STUDENT_ID) REFERENCES students(STUDENT_ID),
                FOREIGN KEY (CLASS_ID) REFERENCES classes(CLASS_ID)
            )
        """)
        
        db.commit()
        db.close()
        print("Tables 'students', 'teachers', 'classes', and 'grades' created successfully.")
    except pymysql.Error as e:
        print(f"Error creating tables: {str(e)}")

def add_student():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    student_class = input("Enter Class: ")
    data = (student_id, name, dob, student_class)
    sql = "INSERT INTO students (STUDENT_ID, NAME, DOB, CLASS) VALUES (%s, %s, %s, %s)"
    try:
        C.execute(sql, data)
        db.commit()
        print('Student added successfully...')
    except pymysql.Error as e:
        print(f"Error adding student: {str(e)}")

def view_students():
    C.execute("SELECT * FROM students")
    result = C.fetchall()
    for r in result:
        print(r)

def update_student():
    student_id = int(input("Enter Student ID to update: "))
    field = input("Enter field to update [NAME, DOB, CLASS]: ")
    new_value = input(f"Enter new value for {field}: ")
    if field == 'DOB':
        new_value = new_value  # Keep as string for date format
    sql = f"UPDATE students SET {field} = %s WHERE STUDENT_ID = %s"
    try:
        C.execute(sql, (new_value, student_id))
        db.commit()
        print('Student updated successfully...')
    except pymysql.Error as e:
        print(f"Error updating student: {str(e)}")

def delete_student():
    student_id = int(input("Enter Student ID to delete: "))
    sql = "DELETE FROM students WHERE STUDENT_ID = %s"
    try:
        C.execute(sql, (student_id,))
        db.commit()
        print('Student deleted successfully...')
    except pymysql.Error as e:
        print(f"Error deleting student: {str(e)}")

def add_teacher():
    teacher_id = int(input("Enter Teacher ID: "))
    name = input("Enter Teacher Name: ")
    subject = input("Enter Subject: ")
    phone_no = input("Enter Phone Number: ")
    data = (teacher_id, name, subject, phone_no)
    sql = "INSERT INTO teachers (TEACHER_ID, NAME, SUBJECT, PHONE_NO) VALUES (%s, %s, %s, %s)"
    try:
        C.execute(sql, data)
        db.commit()
        print('Teacher added successfully...')
    except pymysql.Error as e:
        print(f"Error adding teacher: {str(e)}")

def view_teachers():
    C.execute("SELECT * FROM teachers")
    result = C.fetchall()
    for r in result:
        print(r)

def update_teacher():
    teacher_id = int(input("Enter Teacher ID to update: "))
    field = input("Enter field to update [NAME, SUBJECT, PHONE_NO]: ")
    new_value = input(f"Enter new value for {field}: ")
    sql = f"UPDATE teachers SET {field} = %s WHERE TEACHER_ID = %s"
    try:
        C.execute(sql, (new_value, teacher_id))
        db.commit()
        print('Teacher updated successfully...')
    except pymysql.Error as e:
        print(f"Error updating teacher: {str(e)}")

def delete_teacher():
    teacher_id = int(input("Enter Teacher ID to delete: "))
    sql = "DELETE FROM teachers WHERE TEACHER_ID = %s"
    try:
        C.execute(sql, (teacher_id,))
        db.commit()
        print('Teacher deleted successfully...')
    except pymysql.Error as e:
        print(f"Error deleting teacher: {str(e)}")

def add_class():
    class_id = int(input("Enter Class ID: "))
    class_name = input("Enter Class Name: ")
    schedule = input("Enter Schedule: ")
    data = (class_id, class_name, schedule)
    sql = "INSERT INTO classes (CLASS_ID, CLASS_NAME, SCHEDULE) VALUES (%s, %s, %s)"
    try:
        C.execute(sql, data)
        db.commit()
        print('Class added successfully...')
    except pymysql.Error as e:
        print(f"Error adding class: {str(e)}")

def view_classes():
    C.execute("SELECT * FROM classes")
    result = C.fetchall()
    for r in result:
        print(r)

def update_class():
    class_id = int(input("Enter Class ID to update: "))
    field = input("Enter field to update [CLASS_NAME, SCHEDULE]: ")
    new_value = input(f"Enter new value for {field}: ")
    sql = f"UPDATE classes SET {field} = %s WHERE CLASS_ID = %s"
    try:
        C.execute(sql, (new_value, class_id))
        db.commit()
        print('Class updated successfully...')
    except pymysql.Error as e:
        print(f"Error updating class: {str(e)}")

def delete_class():
    class_id = int(input("Enter Class ID to delete: "))
    sql = "DELETE FROM classes WHERE CLASS_ID = %s"
    try:
        C.execute(sql, (class_id,))
        db.commit()
        print('Class deleted successfully...')
    except pymysql.Error as e:
        print(f"Error deleting class: {str(e)}")

def add_grade():
    student_id = int(input("Enter Student ID: "))
    class_id = int(input("Enter Class ID: "))
    grade = input("Enter Grade: ")
    data = (student_id, class_id, grade)
    sql = "INSERT INTO grades (STUDENT_ID, CLASS_ID, GRADE) VALUES (%s, %s, %s)"
    try:
        C.execute(sql, data)
        db.commit()
        print('Grade added successfully...')
    except pymysql.Error as e:
        print(f"Error adding grade: {str(e)}")

def view_grades():
    C.execute("SELECT * FROM grades")
    result = C.fetchall()
    for r in result:
        print(r)

def main():
    global passwrd
    passwrd = input("Enter password for MySQL: ")

    base_check()
    table_check()
    
    global db, C
    db = pymysql.connect(host="localhost", user="root", password=passwrd, database="school_management")
    C = db.cursor()
    
    while True:
        log = input("For Admin: A, Exit: X ::: ")
        if log.upper() == "A":
            while True:
                menu = input('''Add Student: AS, View Students: VS, Update Student: US, Delete Student: DS, Add Teacher: AT, View Teachers: VT, Update Teacher: UT, Delete Teacher: DT, Add Class: AC, View Classes: VC, Update Class: UC, Delete Class: DC, Add Grade: AG, View Grades: VG, Exit: X ::: ''')
                if menu.upper() == 'AS':
                    add_student()
                elif menu.upper() == 'VS':
                    view_students()
                elif menu.upper() == 'US':
                    update_student()
                elif menu.upper() == 'DS':
                    delete_student()
                elif menu.upper() == 'AT':
                    add_teacher()
                elif menu.upper() == 'VT':
                    view_teachers()
                elif menu.upper() == 'UT':
                    update_teacher()
                elif menu.upper() == 'DT':
                    delete_teacher()
                elif menu.upper() == 'AC':
                    add_class()
                elif menu.upper() == 'VC':
                    view_classes()
                elif menu.upper() == 'UC':
                    update_class()
                elif menu.upper() == 'DC':
                    delete_class()
                elif menu.upper() == 'AG':
                    add_grade()
                elif menu.upper() == 'VG':
                    view_grades()
                elif menu.upper() == 'X':
                    break
                else:
                    print("Wrong Input")
                    
        elif log.upper() == "X":
            break
        else:
            print("Wrong Input")


if __name__ == "__main__":
    main()