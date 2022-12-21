import random
import string
import sqlite3
import datetime

from Initalize import *

def newPass():
    length = 16
    password = "".join(random.sample(string.ascii_letters + string.digits + string.punctuation, length))
    return password

def display_table(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT name, username, date FROM passMan')
    for name, username, date in cursor.fetchall():
        print(name, username, date)
        
def insert_row(conn, name:str,url:str,user:str,passW:str):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passMan (name,url,username,password,date) VALUES (?,?,?,?,?)",
    (name, url, user, passW, datetime.datetime.today().strftime("%x"))
    )

with sqlite3.connect(db_file) as conn1:
    insert_row(conn1, 'flpoly','something','alagonell1730', newPass() )
    
    print('Before changes:')
    display_table(conn1)

    conn1.execute("DELETE FROM passMan WHERE name = ?;", ['flpoly'])

    print('\nAfter changes in conn1:')
    display_table(conn1)