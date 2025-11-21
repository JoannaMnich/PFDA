import sqlite3

con=sqlite3.connect("table.db") 
cur=con.cursor()

sql = "select * from student"
result = cur.execute(sql)
print(f"first row: {result.fetchone()}")

sql = "insert into student values('joe','DA', 'Male')"
cur.execute(sql)
con.commit()

sql = "select * from student"
result = cur.execute(sql)
print(f"all rows: {result.fetchall()}")


con.close()