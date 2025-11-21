import sqlite3

con=sqlite3.connect("table.db") 
cur=con.cursor()

sql = "CREATE TABLE student (name, course, gender)"
cur.execute(sql)    
con.close()
