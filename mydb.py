# Install MySQL on your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python


import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password123',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE data")

print("👌")




















