import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import db
import manage


def book(name):
    global root_book, flight_t, flight_f, flight_d, User
    User = name
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

    global Depature_place, Destination_place, Departure_Time, roots, Flight_no
    Depature_place = flight_f.get()
    Destination_place = flight_t.get()
    Departure_Time = flight_d.get()

    roots = Tk()
    roots.config(bg="beige")
    roots.state("zoomed")
    roots.title("BOOK")
    Label(roots, text="Book Your Flight!", font=(
        "arial", 30, 'bold')).place(relx=0.35, rely=0.100)

    Label(roots, text="From", font=(
        "arial", 30, 'bold')).place(relx=0.2, rely=0.230)
    Label(roots, text=Depature_place, font=(
        "arial", 30, 'bold')).place(relx=0.6, rely=0.230)

    Label(roots, text="To", font=(
        "arial", 30, 'bold')).place(relx=0.2, rely=0.310)
    Label(roots, text=Destination_place, font=(
        "arial", 30, 'bold')).place(relx=0.6, rely=0.310)

    Label(roots, text="Depature Time", font=(
        "arial", 30, 'bold')).place(relx=0.2, rely=0.390)
    Label(roots, text=Departure_Time,  font=(
        "arial", 30, 'bold')).place(relx=0.6, rely=0.390)

    check_flight = db.Check_flight(
        Depature_place, Destination_place, Departure_Time)
    if (check_flight):
        Flight_no = check_flight[0][0]
    else:
        Flight_no = False
    # Creating separate lists for origins and destinations
    if (Flight_no and (check_flight[0][1] <= 30 and check_flight[0][1] > 0)):
        lbl = Label(roots, font=("arial", 30, 'bold'), text="Flight Available")
        lbl.place(relx=0.1, rely=0.500)

        lbl_0 = Label(roots, font=("arial", 30, 'bold'),
                      text=Flight_no)
        lbl_0.place(relx=0.35, rely=0.500)

        lbl_1 = Label(roots, font=("arial", 30, 'bold'), text="Seat Count")
        lbl_1.place(relx=0.6, rely=0.500)

        lbl_2 = Label(roots, font=("arial", 30, 'bold'),
                      text=check_flight[0][1])
        lbl_2.place(relx=0.8, rely=0.500)

        Button(roots, text="Book a Ticket", font=("cursive", 18,
                                                  'bold'), bg="wheat", activebackground="red", command=plus).place(relx=0.45, rely=0.8)

    else:
        lbl = Label(roots, font=("arial", 15, 'bold'),
                    text="Flight Not Available Or Seats Occupied")
        lbl.place(relx=0.2, rely=0.470)


def plus():

    global rootp, Passenger_name, email, class1, age
    rootp = Tk()
    rootp.title("Passenger Information")
    rootp.state("zoomed")

    Label(rootp, text="Passenger Name : ").place(relx=0.1, rely=0.1)
    Passenger_name = Entry(rootp, width=35)
    Passenger_name.place(relx=0.2, rely=0.1)

    Label(rootp, text="Enter Your Email address : ").place(relx=0.1, rely=0.2)
    email = Entry(rootp, width=35)
    email.place(relx=0.2, rely=0.2)

    Label(rootp, font=("arial", 15, 'bold'),
          text="Choose class").place(relx=0.1, rely=0.3)
    class1 = ttk.Combobox(rootp, height=10, width=30, values=[
        "BusinessClass", "Economy"])
    class1.place(relx=0.2, rely=0.3)

    Label(rootp, text="Enter Age:").place(relx=0.1, rely=0.4)
    age = Entry(rootp, width=35)
    age.place(relx=0.2, rely=0.4)

    btn = Button(rootp, text="Add Your Addon preference", command=addon)
    btn.pack()

    rootp.mainloop()


def addon():
    global root_add, fee, Food, Need_assis, Drink
    root_add = Tk()
    root_add.title("ADD ONS")
    root_add.config(bg="beige")
    root_add.state("zoomed")

    Label(root_add, font=("arial", 20, 'bold'),
          text="Add Ons").place(relx=0.45, rely=0.1)

    Label(root_add, font=("arial", 12),
          text="Food Preference").place(relx=0.1, rely=0.2)
    Food = ttk.Combobox(root_add, height=10, width=30,
                        values=["Veg", "NonVeg"])
    Food.place(relx=0.3, rely=0.2)
    Label(root_add, font=("arial", 16, 'bold'),
          text="Veg : Veg Curry and Chapathi/White Rice").place(relx=0.2, rely=0.3)
    Label(root_add, text="Non Veg: Chicken Curry with fried rice/chicken rice ",
          font=("arial", 16, 'bold')).place(relx=0.2, rely=0.4)

    Label(root_add, font=("arial", 12),
          text="Need Special Assistance :").place(relx=0.1, rely=0.5)
    Need_assis = ttk.Combobox(root_add, height=10, width=30,
                              values=["Yes", "No"])
    Need_assis.place(relx=0.3, rely=0.5)

    Label(root_add, font=("arial", 12),
          text="Any Drink Needed :").place(relx=0.1, rely=0.6)
    Drink = ttk.Combobox(root_add, height=10, width=30,
                         values=["Yes", "No"])
    Drink.place(relx=0.3, rely=0.6)

    bf = Button(root_add, font=("cursive", 20, 'bold'), bg="wheat",
                activebackground="tan", text="Continue Payment", command=pay)
    bf.place(relx=0.3, rely=0.8)

    root_add.mainloop()


def pay():
    global root_pay, Payment_status, fee

    Payment_status = 'Pending'
    root_pay = Tk()
    root_pay.title("Pay")
    root_pay.config(bg="beige")
    root_pay.state("zoomed")

    Label(root_pay, font=("arial", 20),
          text=" Total Amount To Pay :").place(relx=0.1, rely=0.7)
    fees_res = db.fees(Flight_no)
    fees = fees_res[0][0]
    if class1.get() == "BusinessClass":
        fee = fees + 2000
    else:
        fee = fees

    Label(root_pay, font=("arial", 20),
          text=fee).place(relx=0.3, rely=0.1)

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
    en4 = Entry(root_pay, width=35)
    en4.place(relx=0.2, rely=0.4)

    if (en1 and en2 and en3 and en4):
        Payment_status = 'Successful'
        bpay = Button(root_pay, font=("cursive", 20, 'bold'), bg="wheat",
                      activebackground="tan", text="Continue Payment", command=submit)
        bpay.place(relx=0.3, rely=0.5)

    root_pay.mainloop()
    roots.mainloop()


def submit():
    confirmation = messagebox.askokcancel(
        "Confirmation", "Do you want to Confirm ?")
    Food1 = Food.get()
    Need_assis1 = Need_assis.get()
    Drink1 = Drink.get()

    if confirmation:

        db.Booking_insert(User, Passenger_name.get(), email.get(), age.get(),
                          Flight_no, Departure_Time, class1.get(), fee, Payment_status)
        db.addon_insert(Food1, Need_assis1, Drink1)

        root_add.destroy()
        roots.destroy()
        root_pay.destroy()
