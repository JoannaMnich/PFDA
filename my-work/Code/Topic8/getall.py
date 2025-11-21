import sqlite3
con=sqlite3.connect("table.db")
cur=con.cursor()

sql= "select * from student"
result =cur.execute(sql)
for now in result.fetchall():
    print(now)