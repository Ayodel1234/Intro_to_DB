import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ayopasslog22!"
        )

        cursor = db.cursor()

        # Create database if it doesn't exist (Strictly avoiding SELECT/SHOW)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        # Print the required success message
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        # Print error message as required
        print(f"Error: {e}")

    finally:
        # Handle closing of the DB connection
        if 'db' in locals() and db.is_connected():
            cursor.close()
            db.close()

if __name__ == "__main__":
    create_database()