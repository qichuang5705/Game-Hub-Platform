import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',     
            user='root',           
            password='yourpassword',  
            database='yourdatabase'   
        )
        
        if connection.is_connected():
            print("Connected!")

            db_info = connection.get_server_info()
            print("Information:", db_info)

        return connection

    except Error as e:
        print("Error:", e)
        return None


