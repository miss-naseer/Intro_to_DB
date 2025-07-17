import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',       # or '127.0.0.1'
            user='root',            # replace with your username
            password='MYsql54321@'  # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Always close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Run the function
create_database()
