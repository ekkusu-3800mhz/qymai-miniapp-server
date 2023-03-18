from dotenv import load_dotenv
import MySQLdb
import os


load_dotenv()

DB_HOST = os.environ.get('MYSQL_HOST')
DB_PORT = int(os.environ.get('MYSQL_PORT', 3306))
DB_USER = os.environ.get('MYSQL_USER')
DB_PASSWORD = os.environ.get('MYSQL_PASSWORD')
DB_NAME = os.environ.get('MYSQL_DB_NAME')



dbc = MySQLdb.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)
cursor = dbc.cursor()

cursor.execute("UPDATE app_cabinet SET `playerCount` = 0, `playerCountUpdateTime` = NOW() WHERE `enablePlayerCount` = 1")
dbc.commit()

dbc.close()
