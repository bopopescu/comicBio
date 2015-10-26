import mysql.connector
from mysql.connector import Error

def connect():
	try:
		conn = mysql.connector.connect(host='localhost',
									database='python_mysql',
									user='root',
									password='chimpoo')

		if conn.is_connected():
			print "Connected to MySQL database"

	except Error as e:
		print e

	finally:
		conn.close()

if __name__ == '__main__':
	connect()