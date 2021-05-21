import mysql.connector

#conexion
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
    
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python ")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)

#crear tablas
