import sqlite3
con = sqlite3.connect('pfda.db')
cur = con.cursor()

book ={}
book['title'] = input("Enter book title: ")
book['author'] = input("Enter book author: ")
book['ISBN'] = input("Enter book ISBN: ")

data=[book]
sql="insert into book values (:title, :author, :ISBN)"
cur.executemany(sql, data)
con.commit()

for row in cur.execute("select * from book"):
    print(f"row{row}")