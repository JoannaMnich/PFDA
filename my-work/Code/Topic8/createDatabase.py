import mysql.connector
from mysql.connector import Error

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
     )

mycursor = db.cursor()
mycursor.execute("CREATE database wsaa")
mycursor.close()
db.close()