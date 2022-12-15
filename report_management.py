import mysql.connector as sqltor
from tabulate import tabulate


def setup():
    mycon = sqltor.connect(user='root',passwd='root')
    cursor = mycon.cursor()
    cursor.execute('create database project')
    mycon = sqltor.connect(user='root',passwd='root',database='project')
    cursor = mycon.cursor()

    cursor.execute('create table report(roll integer,name varchar(30),maths integer,chemistry integer,physics integer,overall_grade varchar(1))')


try:
    setup()
except Exception as e:
    print(e)

mycon = sqltor.connect(user='root',passwd='root',database='project')
cursor = mycon.cursor()

headers = ['ROLL','NAME','MATHS','CHEMISTRY','PHYSICS','OVERALL_GRADE']
options_list = '''
CHOOSE AN OPTION
-----------------

1) Show all records
2) Add a record
3) delete a record (using roll no.)
4) update a record (using roll no.)
5) Find particular record (using roll no.)

'''
def grading(s):
    if s >= 90:
        return 'A'
    elif s >= 70:
        return 'B'
    elif s >= 50:
        return 'C'
    elif s >= 30:
        return 'D'
    elif s >= 20:
        return 'E'
    else: return 'F'
def showRec():
    cursor.execute('select * from report')
    data = cursor.fetchall()
    print(tabulate(data,headers,tablefmt='fancy_grid'))

    a = int(input('press 1 to continue... '))
    if a == 1: return query(int(input(options_list)))
    else: return
    
def addRec():
    r = int(input('Insert roll no: '))
    n = input('Insert name: ')
    m = int(input('Marks in Maths( /100 ): '))
    c = int(input('Marks in Chemistry( /100 ): '))
    p = int(input('Marks in Physics( /100 ): '))
    g = grading((m+c+p)/3)
    cursor.execute(f'insert into report values({r},\'{n}\',{m},{c},{p},\'{g}\')')
    mycon.commit()

    print('\nrecord successfully added!')
    a = int(input('Press 1 to continue...'))
    if a == 1: return query(int(input(options_list)))
    else: return

def delRec(r):
    cursor.execute(f'delete from report where roll = {r}')
    mycon.commit()

    print('record successfully deleted!')
    a = int(input('Press 1 to continue...'))
    if a == 1: return query(int(input(options_list)))
    else: return

def updateRec(r):
    print('\nCHOOSE THE COLUMN TO UPDATE\n------------------------\n')
    for i in headers[0:5]:
        print(str(headers.index(i)+1)+')',i)
    def option():
        a = int(input('\nenter between 1-5: '))
        if a<1 or a>5:
            return option()
        else: return a
    a = option()
    b = input('enter new value: ')
    try:
        b = int(b)
    except:
        pass
    if isinstance(b,int):
        cursor.execute(f'update report set {headers[a-1]} = {b} where roll = {r}')
    else:
        cursor.execute(f'update report set {headers[a-1]} = \'{b}\' where roll = {r}')

    print('Record successfully updated!')
    a = int(input('\nPress 1 to continue...'))
    if a == 1: return query(int(input(options_list)))
    else: return

def findInfo(r):
    cursor.execute(f'select * from report where roll = {r}')
    data = cursor.fetchall()
    print(tabulate(data,headers,tablefmt='fancy_grid'))

    a = int(input('press 1 to continue... '))
    if a == 1: return query(int(input(options_list)))
    else: return


def query(option):
    if option == 1:
        showRec()
    elif option == 2:
        addRec()
    elif option == 3:
        delRec(int(input('\nenter roll no. you want to delete: ')))
    elif option == 4:
        updateRec(int(input('\nenter roll no. you want to update: ')))
    elif option == 5:
        findInfo(int(input('\nenter roll no. you want to find: ')))

    else: return query(int(input(options_list)))
query(int(input(options_list)))
