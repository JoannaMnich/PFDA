import sqlite3
con = sqlite3.connect('pfda.db')
cur = con.cursor()

result = cur.execute("select * from book")
print(result.fetchone())

sql ="""
    INSERT INTO book VALUES 
    ('Harry Pothead', 'J.K. Really', '112344'),
    ('Harry potter does something profound', 'JK Rowling', '12344')
"""
cur.execute(sql)
con.commit()
result=cur.execute("select * from book")
print(result.fetchone())
con.close()