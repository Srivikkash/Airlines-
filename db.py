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


def Check_flight(connection, sd, sde, dt):
    cursor = connection.cursor()
    query = "SELECT flights.Flight_no, seat.seat_remaining FROM flights JOIN seat ON flights.Flight_no = seat.Flight_no WHERE flights.DEPARTURE = '" + \
        sd+"' AND flights.DESTINATION = '"+sde+"' AND seat.Departure_Time = '"+dt+"';"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# login
