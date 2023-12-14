import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import db
import manage

connection = db.create_connection()


def book(name):
    global root_book, flight_t, flight_f, flight_d
    root_book = tk.Tk()
    root_book.config(bg="beige")
    root_book.state("zoomed")
    Label(root_book, text="Welcome "+name+" To Our Airline Reservation Center!", font=(
        "arial", 30, 'bold')).place(relx=0.1, rely=0.150)
    Label(root_book, font=("arial", 20, 'bold'),
          text="FROM").place(relx=0.1, rely=0.3)
    flight_f = ttk.Combobox(root_book, height=20, width=50, values=[
        "bengaluru", "chennai", "mumbai", "goa", "pune", "new delhi", "lucknow", "aurangabad", "ahemdabad", "srinagar", "hyderabad", "agra", "ahmedabad", "bangkok", "bhopal"])
    flight_f.place(relx=0.2, rely=0.3)
    Label(root_book, font=("arial", 20, 'bold'),
          text="TO").place(relx=0.5, rely=0.3)
    flight_t = ttk.Combobox(root_book, height=20, width=50, values=[
                            "bengaluru", "chandigarh", "chennai", "delhi", "goa", "harayana", "hyderabad", "jaipur", "kolkata", "lucknow", "mumbai", "pune", "surat"])
    flight_t.place(relx=0.55, rely=0.3)

    Label(root_book, font=("arial", 20, 'bold'),
          text="Departure Time : ").place(relx=0.1, rely=0.5)

    flight_d = ttk.Combobox(root_book, height=20, width=30, values=[
                            "13:05", "15:00", "18:00", "20:45", "00:15", "03:15", "7:13", "10:45"])
    flight_d.place(relx=0.3, rely=0.5)

    Button(root_book, text="Search Flights", font=("cursive", 18,
                                                   'bold'), bg="wheat", activebackground="tan", command=search).place(relx=0.25, rely=0.8)
    Button(root_book, text="Manage Booking", font=("cursive", 18,
                                                   'bold'), bg="wheat", activebackground="red", command=manage.cancel).place(relx=0.45, rely=0.8)

    root_book.mainloop()


def search():

    global sd, sde, dt, roots, lbl, lbl_1
    sd = flight_f.get()
    sde = flight_t.get()
    dt = flight_d.get()

    roots = Tk()
    roots.config(bg="beige")
    roots.state("zoomed")
    roots.title("BOOK")
    Label(roots, text="Book Your Flight!", font=(
        "arial", 30, 'bold')).place(relx=0.35, rely=0.100)

    Label(roots, text="From", font=(
        "arial", 30, 'bold')).place(relx=0.2, rely=0.230)
    Label(roots, text=sd, font=(
        "arial", 30, 'bold')).place(relx=0.6, rely=0.230)

    Label(roots, text="To", font=(
        "arial", 30, 'bold')).place(relx=0.2, rely=0.310)
    Label(roots, text=sde, font=(
        "arial", 30, 'bold')).place(relx=0.6, rely=0.310)

    Label(roots, text="Depature Time", font=(
        "arial", 30, 'bold')).place(relx=0.2, rely=0.390)
    Label(roots, text=dt, font=(
        "arial", 30, 'bold')).place(relx=0.6, rely=0.390)

    Flights_availabe = db.Check_flight(connection, sd, sde, dt)
    # Creating separate lists for origins and destinations
    if (Flights_availabe):
        lbl = Label(roots, font=("arial", 30, 'bold'), text="Flight Available")
        lbl.place(relx=0.1, rely=0.500)

        lbl_0 = Label(roots, font=("arial", 30, 'bold'),
                      text=Flights_availabe[0][0])
        lbl_0.place(relx=0.4, rely=0.500)

        lbl_1 = Label(roots, font=("arial", 30, 'bold'), text="Seat Count")
        lbl_1.place(relx=0.6, rely=0.500)

        lbl_2 = Label(roots, font=("arial", 30, 'bold'),
                      text=Flights_availabe[0][1])
        lbl_2.place(relx=0.8, rely=0.500)

        Button(roots, text="Book a Ticket", font=("cursive", 18,
                                                  'bold'), bg="wheat", activebackground="red", command=plus).place(relx=0.45, rely=0.8)

    else:
        lbl = Label(roots, font=("arial", 15, 'bold'),
                    text="Flight Not Available")
        lbl.place(relx=0.2, rely=0.470)


def plus():

    global count, rootp

    count[0] += 1
    cost = 20000 * count[0]
    lbl['text'] = count[0]
    lbl_1['text'] = "rs " + str(cost)
    rootp = Tk()
    rootp.title("Information")
    rootp.state("zoomed")
    lbl_2 = Label(rootp, text="Name : ")
    lbl_2.pack()
    e1 = Entry(rootp, width=35)
    e1.pack()
    lbl_2 = Label(rootp, text="Name : ")
    lbl_2.place(relx=0.1, rely=0.1)
    e1 = Entry(rootp, width=35)
    e1.place(relx=0.2, rely=0.1)
    Label(
        rootp, text="Enter mobile number/email address : ").place(relx=0.1, rely=0.2)
    e2 = Entry(rootp, width=35)
    e2.place(relx=0.2, rely=0.2)
    Label(rootp, font=("arial", 15, 'bold'),
          text="Choose class").place(relx=0.1, rely=0.3)
    w4 = ttk.Combobox(rootp, height=10, width=30, values=[
        "BusinessClass", "Economy"])
    w4.place(relx=0.2, rely=0.3)
    Label(rootp, text="Enter Age:").place(relx=0.1, rely=0.4)
    e3 = Entry(rootp, width=35)
    e3.place(relx=0.2, rely=0.4)


def submit():
    rootp.destroy()
    btn = Button(rootp, text="submit", command=submit)
    btn.pack()
    rootp.mainloop()
    bb = Button(roots, font=("cursive", 20, 'bold'), bg="wheat",
                activebackground="tan", text="+", command=plus)
    bb.place(relx=0.87, rely=0.87)


def addon():
    global root_add
    root_add = Tk()
    root_add.title("ADD ONS")
    root_add.config(bg="beige")
    root_add.state("zoomed")
    Label(root_add, font=("arial", 20, 'bold'),
          text="Add Ons").place(relx=0.45, rely=0.1)
    Label(root_add, font=("arial", 12),
          text="Food Preference").place(relx=0.1, rely=0.2)
    w5 = ttk.Combobox(root_add, height=10, width=30,
                      values=["Veg", "NonVeg"])
    w5.place(relx=0.3, rely=0.2)
    Label(root_add, font=("arial", 16, 'bold'),
          text="Veg : Veg Curry and Chapathi/White Rice").place(relx=0.2, rely=0.3)
    Label(root_add, text="Non Veg: Chicken Curry with fried rice/chicken rice ",
          font=("arial", 16, 'bold')).place(relx=0.2, rely=0.4)
    Label(root_add, font=("arial", 12),
          text="Need Special Assistance :").place(relx=0.1, rely=0.5)
    w6 = ttk.Combobox(root_add, height=10, width=30,
                      values=["Yes", "No"])
    w6.place(relx=0.3, rely=0.5)
    Label(root_add, font=("arial", 12),
          text="Any Drink Needed :").place(relx=0.1, rely=0.6)
    w7 = ttk.Combobox(root_add, height=10, width=30,
                      values=["Yes", "No"])
    w7.place(relx=0.3, rely=0.6)
    Label(root_add, font=("arial", 12),
          text="Pick up/drop needed :").place(relx=0.1, rely=0.7)
    w8 = ttk.Combobox(root_add, height=10, width=30,
                      values=["Yes", "No"])
    w8.place(relx=0.3, rely=0.7)
    Label(root_add, font=("arial", 14), text="Cabin baggage\n7kgs\nCheck in baggage\n15kgs\n").place(
        relx=0.6, rely=0.55)


def pay():
    root_pay = Tk()
    root_pay.title("Pay")
    root_pay.config(bg="beige")
    root_pay.state("zoomed")
    l_2 = Label(root_pay, font=("arial", 14),
                text=" Card Holder Name : ")
    l_2.place(relx=0.1, rely=0.1)
    en1 = Entry(root_pay, width=35)
    en1.place(relx=0.3, rely=0.1)
    Label(root_pay, font=("arial", 14),
          text="Enter Card Number : ").place(relx=0.1, rely=0.2)
    en2 = Entry(root_pay, width=35)
    en2.place(relx=0.3, rely=0.2)
    Label(root_pay, font=("arial", 14),
          text="Enter Expiry Date").place(relx=0.1, rely=0.3)
    en3 = Entry(root_pay, width=35)
    en3.place(relx=0.25, rely=0.3)
    Label(root_pay, font=("arial", 14),
          text="Enter CVV:").place(relx=0.1, rely=0.4)
    e4 = Entry(root_pay, width=35)
    e4.place(relx=0.2, rely=0.4)

    def complete():
        roots.destroy()
        root_add.destroy()
        root_pay.destroy()
        messagebox.showinfo(
            "Success", "You have Booked your flight")

    bpay = Button(root_pay, font=("cursive", 20, 'bold'), bg="wheat",
                  activebackground="tan", text="Continue Payment", command=complete)
    bpay.place(relx=0.3, rely=0.5)
    root_pay.mainloop()

    bf = Button(root_pay, font=("cursive", 20, 'bold'), bg="wheat",
                activebackground="tan", text="Continue Payment", command=pay)
    bf.place(relx=0.3, rely=0.8)

    root_add.mainloop()

    bp = Button(roots, font=("cursive", 20, 'bold'), bg="wheat",
                activebackground="tan", text="See Add Ons", command=addon)
    bp.place(relx=0.28, rely=0.7)
    roots.mainloop()
