import mysql.connector

database = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'MYsql!',
	)

cursorobject = database.cursor()

cursorobject.execute("CREATE DATABASE dataBase")

print("Done")