import tkinter as tk
from tkinter import *
from prettytable import PrettyTable
import db


def de():
    tno = enter6.get()
    res = db.Cancel_ticket(tno)
    if res:
        root_cancel.destroy()


def cancel():
    global enter6, root_cancel, enter7

    root_cancel = Tk()
    root_cancel.config(bg="beige")
    root_cancel.state("zoomed")
    root_cancel.title("Manage Bookings")

    # Manage
    results = db.manage_fetch()

    # Create PrettyTable
    table = PrettyTable(["Ticket_NO", "User", "Passenger_name", "Email", "Age",
                         "Flight_no", "Departure_Time", "Class", "Fee", "Payment_status"])

    for row in results:
        table.add_row(row)

    # Display PrettyTable in Text widget
    text_widget = Text(root_cancel, font=("Courier", 12),
                       wrap=NONE, height=15, width=130)
    text_widget.insert(END, table.get_string())
    text_widget.config(state=DISABLED)  # Make the Text widget read-only
    text_widget.place(x=40, y=70)

    # Cancel block
    Label(root_cancel, font=("arial", 22, 'bold'),
          text="Cancel Booking/ View Ticket").place(x=410, y=470)
    Label(root_cancel, font=("arial", 15, 'bold'),
          text="Ticket Number: ").place(x=400, y=550)
    enter6 = Entry(root_cancel, width=35)
    enter6.place(x=600, y=550)

    Button(root_cancel, text="View Flight", font=("cursive", 15, 'bold'),
           activebackground="tan", command=view_my_ticket).place(x=430, y=600)

    # Assuming `de` is a function defined elsewhere in your code
    Button(root_cancel, text="Cancel Flight", font=("cursive", 15, 'bold'),
           activebackground="tan", command=de).place(x=580, y=600)

    Button(root_cancel, text="Back", font=("cursive", 15, 'bold'),
           activebackground="tan", command=lambda: root_cancel.destroy()).place(x=750, y=600)

    root_cancel.mainloop()


def view_my_ticket():
    root_view = Tk()
    root_view.config(bg="beige")
    root_view.title("Boarding Pass")
    root_view.geometry("500x300")

    tno = enter6.get()
    results = db.flight_details_on_ticket(tno)

    if results:
        name, flightNO, Dep, Des, time, class_, fees = results[0]

    Label(root_view, font=("arial", 22, 'bold'),
          text="Boarding Pass").place(x=150, y=20)

    Label(root_view, font=("arial", 12),
          text=f"Name: {name}").place(x=50, y=70)
    Label(root_view, font=("arial", 12),
          text=f"Flight Number: {flightNO}").place(x=50, y=100)
    Label(root_view, font=("arial", 12),
          text=f"Departure: {Dep}").place(x=50, y=130)
    Label(root_view, font=("arial", 12),
          text=f"Destination: {Des}").place(x=50, y=160)
    Label(root_view, font=("arial", 12),
          text=f"Departure Time: {time}").place(x=50, y=190)
    Label(root_view, font=("arial", 12),
          text=f"Class: {class_}").place(x=300, y=70)
    Label(root_view, font=("arial", 12),
          text=f"Fee: ₹{fees}").place(x=300, y=100)

    Button(root_view, text="Back", font=("cursive", 15, 'bold'),
           activebackground="tan", command=root_view.destroy).place(x=200, y=240)

    root_view.mainloop()
