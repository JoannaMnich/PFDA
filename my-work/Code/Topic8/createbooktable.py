import sqlite3
con = sqlite3.connect('pfda.db')
cur = con.cursor()

cur.execute("CREATE TABLE book(title, author, ISBN)")
con.close()
