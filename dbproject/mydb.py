import mysql.connector

database = mysql.connector.connect(
	host = 'your_host_name',
	user = 'your_user_name',
	passwd = 'your_password',
	)

cursorobject = database.cursor()

cursorobject.execute("CREATE DATABASE dataBase")

print("Done")