import mysql.connector
from mysql.connector import Error

# init db


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='Localhost',
            user='root',
            password='',
            database='airlines'
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# get Departure, Destination datas


def Check_flight(connection):
    cursor = connection.cursor()
    query = "SELECT DISTINCT Departure, Destination FROM flights"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# login
