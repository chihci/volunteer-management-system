    # test_db_connection.py
import mysql.connector
from mysql.connector import Error
from config import Config

def test_connection():
    try:
        # Use your current Config class
        connection = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"✅ Connected to MySQL Server version {db_info}")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"✅ Connected to database: {record[0]}")

    except Error as e:
        print(f"❌ Error while connecting to MySQL: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("🔒 MySQL connection is closed")

if __name__ == "__main__":
    test_connection()