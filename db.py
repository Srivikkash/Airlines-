from tkinter import *
import tkinter.messagebox as mymessagebox
import mysql.connector
from mysql.connector import Error

# init db


def create_connection():
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

# get Flight No


def Check_flight(sd, sde):
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT flights.Flight_no, seat.seat_remaining, seat.Departure_Time FROM flights JOIN seat ON flights.Flight_no = seat.Flight_no WHERE flights.DEPARTURE = '" + \
        sd+"' AND flights.DESTINATION = '"+sde+"';"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# Registration


def Registration(name, passkey, mail, Gender, age):
    try:
        connection = create_connection()
        mycursor = connection.cursor()
        sql = "INSERT INTO login VALUES (%s, %s,%s,%s,%s)"
        val = (name, passkey, mail, Gender, age)
        mycursor.execute(sql, val)
        connection.commit()
        print(mycursor.rowcount, "record inserted.")
        mymessagebox.showinfo("Success", "Successfully Registered")

    except Exception as e:
        mymessagebox.showinfo("Error", "Registered Failed Try Again!!!")
        connection.rollback()
    return None

# login


def login(User_Txt, PassTxt):
    global UserTxt
    UserTxt = User_Txt
    connection = create_connection()
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM login where uname = '" +
                     UserTxt + "' and password = '" + PassTxt + "';")
    myresult = mycursor.fetchone()

    return myresult


def manage_fetch():

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT Ticket_NO, Passenger_name, email, age, Flight_no, Departure_Time, Class, Fee, Payment_status FROM booking where User=\"" + UserTxt+"\";")
    results = cursor.fetchall()
    return results


def Cancel_ticket(tno):
    tno1 = str(tno)
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("select Flight_no from booking where Ticket_NO="+tno1+";")
    results = cursor.fetchall()
    Flight_no = results[0][0]
    confirmation = mymessagebox.askokcancel(
        "Confirmation", "Do you want to Cancel ticket"+tno1+"?")
    if confirmation:
        cursor.execute("delete from booking where Ticket_NO="+tno1+";")
        cursor.execute("delete from addons where Ticket_NO="+tno1+";")

# update seat count
        sql_ticket = "select seat_filled,seat_remaining from seat where Flight_no=\""+Flight_no+"\";"
        cursor.execute(sql_ticket)
        seat = cursor.fetchall()

        seat_filled = str(seat[0][0] - 1)
        seat_remaining = str(seat[0][1]+1)

        cursor.execute("update seat set seat_filled="+seat_filled +
                       ",seat_remaining="+seat_remaining+" where Flight_no =\""+Flight_no+"\";")
        connection.commit()

        mymessagebox.showinfo("Information", "TICKET CANCELLED")
        mymessagebox.showinfo(
            "Refund", "60% refund has been credited to your account")
        return True
    else:
        return False

# fees


def fees(flight):

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "Select CHARGES from flights where FLIGHT_NO =\""+flight+"\";")
    results = cursor.fetchall()
    return results
# Booking insertion


def Booking_insert(User, Passenger_name, email, age,
                   Flight_no, Departure_Time, class1, fee, Payment_status):

    connection = create_connection()
    mycursor = connection.cursor()
    sql_ticket = "select seat_filled,seat_remaining from seat where Flight_no=\""+Flight_no+"\";"
    mycursor.execute(sql_ticket)
    seat = mycursor.fetchall()

    seat_filled = str(seat[0][0] + 1)
    seat_remaining = str(seat[0][1]-1)

    try:

        sql = "INSERT INTO booking (`User`, `Passenger_name`, `email`, `age`,`Flight_no`, `Departure_Time`, `class`, `fee`, `Payment_status`) \
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (User, Passenger_name, email, age,
               Flight_no, Departure_Time, class1, fee, Payment_status)
        mycursor.execute(sql, val)

        connection.commit()
        mycursor.execute("update seat set seat_filled= %s,seat_remaining=%s where Flight_no = %s;",
                         (seat_filled, seat_remaining, Flight_no))

        connection.commit()
        print(mycursor.rowcount, "record inserted.")
        mymessagebox.showinfo("Success", "Ticket Successfully Booked")
    except Exception as e:
        print(e)
        mymessagebox.showinfo("Error", "Booking Failed Try Again!!!")
        connection.rollback()
    return None


def addon_insert(Food, Need_assis, Drink):
    try:

        connection = create_connection()
        mycursor = connection.cursor()

        sql_ticket = "select Ticket_NO from booking order by Ticket_NO desc limit 1;"
        mycursor.execute(sql_ticket)
        Ticket_NO_addon = mycursor.fetchall()
        sql = "INSERT INTO addons (`Ticket_NO`,`Food`, `Need_assis`, `Drink`) VALUES (%s,%s,%s,%s);"
        val = (Ticket_NO_addon[0][0], Food, Need_assis, Drink)
        mycursor.execute(sql, val)
        connection.commit()
        print(mycursor.rowcount, "record inserted addons.")

    except Exception as e:
        print(e)
        mymessagebox.showinfo("Error", "Booking Failed Try Again!!!")
        connection.rollback()
    return None
