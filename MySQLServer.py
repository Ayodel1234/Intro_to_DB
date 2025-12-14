import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ayopasslog22!"
        )
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        if 'db' in locals() and db.is_connected():
            cursor.close()
            db.close()

if __name__ == "__main__":
    create_database()