'''
import sqlite3
connection=sqlite3.connect('test.db')
cursor=connection.cursor()
cursor.execute('create TABLE student (id VARCHAR(50) PRIMARY KEY,NAME VARCHAR(20))')
cursor.execute('INSERT into student VALUES ("123","lmy")')
cursor.execute('INSERT into student VALUES ("000","lr")')
cursor.execute('SELECT  * FROM student')
value=cursor.fetchall()
print(value)
cursor.close()
connection.close()
'''

import mysql.connector
conn = mysql.connector.connect(user='root', password='123456', database='test')
cursor=conn.cursor()
cursor.execute('INSERT into student VALUES ("000","hehe")')
cursor.execute('SELECT  * FROM student')
value=cursor.fetchall()
print(value)
cursor.close()
conn.close()



