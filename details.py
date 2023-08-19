import mysql.connector

mysqldb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Bharath@866',
    database='details',
    port='3306'
)
mysqlcursor = mysqldb.cursor()

def insert(name,age,gender,mail_id):
    try:
        mysqlcursor.execute(
            "insert into student_details(name,age,gender,mail_id)values(%s,%s,%s,%s)",(name,age,gender,mail_id))
        mysqldb.commit()
        print('record inserted')
    except:
        mysqldb.rollback()
    # mysqlcursor.close()


# display table
def view():
    try:
        mysqlcursor.execute("select * from student_details")
        result = mysqlcursor.fetchall()
        mysqldb.commit()
        for i in result:
            print(i)
    except Exception as e:
        print(e)
    # mysqlcursor.close()
def update():
    print('''
    1.name
    2.age
    3.gender
    4.mail
    ''')
    ch=int(input("enter your choice:"))
    if ch==1:
        name=input("enter name :")
        roll_no=int(input("enter roll_no :"))
        mysqlcursor.execute("update student_details set name=%s where roll_no=%s",(name,roll_no))
        mysqldb.commit()
        # mysqlcursor.close()
    elif ch==2:
        age = int(input("enter age :"))
        roll_no = int(input("enter roll_no :"))
        mysqlcursor.execute("update student_details set age=%s where roll_no=%s", (age, roll_no))
        mysqldb.commit()
        # mysqlcursor.close()
    elif ch==3:
        gender = input("enter gender :")
        roll_no = int(input("enter roll_no :"))
        mysqlcursor.execute("update student_details set gender=%s where roll_no=%s", (gender, roll_no))
        mysqldb.commit()
        # mysqlcursor.close()
    elif ch==4:
        mail_id = input("enter mail :")
        roll_no = int(input("enter roll_no :"))
        mysqlcursor.execute("update student_details set mail_id=%s where roll_no=%s", (mail_id, roll_no))
        mysqldb.commit()
        # mysqlcursor.close()
    else:
        print("invalid selection")
# delete record
def delete(roll_no):
    try:
        mysqlcursor.execute("delete from student_details where roll_no=%s",(roll_no,))
        mysqldb.commit()
        print("record deleted successfully")
    except:
        mysqldb.rollback()

    # mysqldb.close()
while True:
    print('''
1.insert
2.view
3.update
4.delete
''')
    choice = int(input("enter any choice:"))
    if choice == 1:
        name=input("Enter name :")
        age=int(input("Enter age :"))
        gender=input("Enter gender :")
        mail_id=input("Enter mail_id :")
        insert(name,age,gender,mail_id)
    elif choice == 2:
        view()
    elif choice == 3:
        update()
    elif choice == 4:
        roll_no = int(input("enter roll_no :"))
        delete(roll_no)
    else:
        quit("i don't understand")

