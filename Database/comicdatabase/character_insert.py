from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import requests

payload = {
	'api_key' : "9b477c6dec985e48795c42203d8fdb92fa93a2c1",
	'format': "json",
	'limit': 1
}

r_characters = requests.get("http://www.comicvine.com/api/characters", params=payload)
characters = r_characters.json()

payload = {
	'api_key' : "9b477c6dec985e48795c42203d8fdb92fa93a2c1",
	'format': "json",
}

r_character = requests.get(characters['results'][0]['api_detail_url'], params=payload)
character = r_character.json()


def insert_character(char_id, name, realname, gender, origin, image, siteurl, deck):
	query = "INSERT INTO characters(id, name, realname, gender, origin, image, siteurl, deck) " \
			"VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"  

	args = (char_id, name, realname, gender, origin, image, siteurl, deck)

	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)
		
		if cursor.lastrowid:
			print('last insert id', cursor.lastrowid)
		else:
			print('last insert id not found')

		conn.commit()

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def main():
	insert_character(character['results']['id'], str(character['results']['name']), str(character['results']['real_name']), str(character['results']['gender']), str(character['results']['first_appeared_in_issue']['name']), str(character['results']['image']['super_url']), str(character['results']['site_detail_url']), str(character['results']['deck']))

if __name__ == '__main__':
	main()
