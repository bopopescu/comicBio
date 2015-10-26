from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import requests

payload = {
	'api_key' : "9b477c6dec985e48795c42203d8fdb92fa93a2c1",
	'format': "json",
	'limit': 100
}

r_characters = requests.get("http://www.comicvine.com/api/characters", params=payload)
characters = r_characters.json()

payload = {
	'api_key' : "9b477c6dec985e48795c42203d8fdb92fa93a2c1",
	'format': "json",
}

character = []
for i in range(len(characters['results'])): 
	r_character = requests.get(characters['results'][i]['api_detail_url'], params=payload)
	character.append(r_character.json())

def insert_characters(character_info):
	query = "INSERT INTO characters(id, name, realname, gender, origin, image, siteurl, deck) " \
			"VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"  

	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.executemany(query, character_info)

		conn.commit()

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def insert_aliases(aliase_info):
	query = "INSERT INTO aliases(character_id, name) " \
			"VALUES(%s, %s)"  

	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.executemany(query, aliase_info)

		conn.commit()

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def insert_powers(power_info):
	query = "INSERT INTO powers(character_id, name) " \
			"VALUES(%s, %s)"  

	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.executemany(query, power_info)

		conn.commit()

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def main():
	character_info = []
	for i in range(0,100):
		# characters table
		# if i not in [33,34,50,55,65,66,69,95,96,98,99]:  #66 gives ERROR: UnicodeEncodeError: 'ascii' codec can't encode character u'\xf9' in position 21: ordinal not in range(128)
			# character_info.append((character[i]['results']['id'], str(character[i]['results']['name']), str(character[i]['results']['real_name']), str(character[i]['results']['gender']), str(character[i]['results']['first_appeared_in_issue']['name']), str(character[i]['results']['image']['super_url']), str(character[i]['results']['site_detail_url']), str(character[i]['results']['deck'])))
		
		if character[i]['results']['powers']:
			for j in range(len(character[i]['results']['powers'])):
				character_info.append((character[i]['results']['id'], str(character[i]['results']['powers'][j]['name'])))
		
		# aliases table
		# item = []		
		# if character[i]['results']['aliases']:
			# item = character[i]['results']['aliases'].split('\n')
		# for j in range(len(item)):
			# character_info.append((character[i]['results']['id'], str(item[j])))

	# insert_characters(character_info)
	# insert_aliases(character_info)
	insert_powers(character_info)
	print "Done!!! INSERTING" 

if __name__ == '__main__':
	main()

