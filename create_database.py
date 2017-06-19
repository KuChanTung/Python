import sqlite3 as sql

conn = sql.connect('database.db')
print("Opened database successfully")

with conn:
    cur = conn.cursor()    
    cur.execute("CREATE TABLE Tasks(Uri TEXT, Title TEXT, Description TEXT, Done NUMERIC)")
    cur.execute("INSERT INTO Tasks VALUES('zxcv','Study at home','Emphasizing on Math and English', 1)")
    cur.execute("INSERT INTO Tasks VALUES('asdf','Clean the house','Remember to dump garbage', 1)")
    cur.execute("INSERT INTO Tasks VALUES('qwer','Meet with teacher','By skype', 0)")
    print("Insert records successfully")

'''
Another way
cur = conn.cursor()    
cur.execute("CREATE TABLE Tasks(Uri TEXT, Title TEXT, Description TEXT, Done NUMERIC)")
cur.execute("INSERT INTO Tasks VALUES('zxcv','Study at home','Emphasizing on Math and English', 1)")
cur.execute("INSERT INTO Tasks VALUES('asdf','Clean the house','Remember to dump garbage', 1)")
cur.execute("INSERT INTO Tasks VALUES('qwer','Meet with teacher','By skype', 0)")
conn.commit()
conn.close()
'''