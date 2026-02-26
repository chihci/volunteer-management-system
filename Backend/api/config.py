import os
from dotenv import load_dotenv


# Load in env
basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path)

#mysql://root:lZRScfwFIEsFrOfQyBGFWKlQboxBhdMN@interchange.proxy.rlwy.net:46935/railway
# config.py
#class Config:
#    MYSQL_HOST = 'localhost'
#    MYSQL_USER = 'root'
#    MYSQL_PASSWORD = os.getenv("database_password")
#    MYSQL_DB = 'volunteermgnt'

class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB = os.getenv("MYSQL_DB")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))

class TestConfig(Config):
    MYSQL_HOST = 'mydemoserver-quickstart.mysql.database.azure.com'
    MYSQL_USER = 'mydemouser'
    MYSQL_PASSWORD = os.getenv("database_password")
    MYSQL_DB = 'test_db'