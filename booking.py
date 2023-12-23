import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import db
import reg
import manage
from prettytable import PrettyTable

# import listFlights


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

    Button(root_book, text="Search Flights", font=("cursive", 18,
                                                   'bold'), bg="wheat", activebackground="tan", command=search).place(relx=0.20, rely=0.4)
    Button(root_book, text="Manage Booking", font=("cursive", 18,
                                                   'bold'), bg="wheat", activebackground="tan", command=manage.cancel).place(relx=0.40, rely=0.6)
    Button(root_book, text="View All Flights", font=("cursive", 18, 'bold'),
           bg="wheat", activebackground="tan", command=view_all_flights).place(relx=0.60, rely=0.4)

    Button(root_book, text="Logout", font=(
        "cursive", 15, 'bold'), bg="wheat", activebackground="tan", command=back_log).place(relx=0.77, rely=0.05)

    root_book.mainloop()


def back_log():
    root_book.destroy()
    reg.login()


def customize_listbox(listbox):
    # Customize the appearance of the listbox
    listbox.configure(font=("Arial", 18), bg="Beige", selectbackground="orange",
                      selectforeground="white", bd=0, highlightthickness=0)


def create_flight_listbox(root):
    # Create a Listbox
    flight_listbox = Listbox(roots, font=(
        "arial", 16), selectmode=SINGLE, width=55, borderwidth=1, relief="solid")
    flight_listbox.place(relx=0.2, rely=0.400)

    # Customize the appearance of the Listbox
    customize_listbox(flight_listbox)

    return flight_listbox


# list all flight details

def view_all_flights():

    # Create a new Tkinter window for viewing all flights
    root_view = tk.Tk()
    root_view.title("All Flights")
    root_view.state('zoomed')
    root_view.config(bg="beige")

    # Display flight information using PrettyTable
    headers = ["S.no", "Airline Name", "Flight_no", "Departure",
               "Destination", "Seats Remaining", "Departure Time"]
    table = PrettyTable(headers)

    try:
        all_flights = db.get_all_flights()
        for flight in all_flights:
            table.add_row([flight[0], flight[1], flight[2],
                          flight[3], flight[4], flight[5], flight[6]])
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

    # Print PrettyTable output
    table_str = table.get_string()
    flight_listbox = Listbox(root_view, font=("Courier", 16), width=len(
        table_str.splitlines()[0]) + 2, height=26, borderwidth=1, relief="solid")
    flight_listbox.pack(pady=20)

    for line in table_str.splitlines():
        flight_listbox.insert(tk.END, line)

    Button(root_view, text="Back", font=(
        "cursive", 15, 'bold'), bg="wheat", activebackground="tan", command=lambda: root_view.destroy()).place(relx=0.8, rely=0.93)
    Label(root_view, font=("arial", 13, 'bold'),
          text="*Note:Scroll Down To view more").place(relx=0.5, rely=0.93)

    root_view.mainloop()


def search():
    global Departure_place, Destination_place, roots, flight_listbox, flight_details

    Depature_place = flight_f.get()
    Destination_place = flight_t.get()

    roots = Tk()
    roots.config(bg="beige")
    roots.state("zoomed")
    roots.title("BOOK")

    Label(roots, text="Book Your Flight!", font=(
        "arial", 30, 'bold')).place(relx=0.35, rely=0.100)

    Label(roots, text="From", font=("arial", 30, 'bold')).place(
        relx=0.2, rely=0.230)
    Label(roots, text=Depature_place, font=(
        "arial", 30, 'bold')).place(relx=0.6, rely=0.230)

    Label(roots, text="To", font=("arial", 30, 'bold')).place(
        relx=0.2, rely=0.310)
    Label(roots, text=Destination_place, font=(
        "arial", 30, 'bold')).place(relx=0.6, rely=0.310)

    check_flight = db.Check_flight(Depature_place, Destination_place)

    flight_listbox = Listbox(roots, font=(
        "Courier", 20), selectmode=SINGLE, width=40)
    flight_listbox.place(relx=0.2, rely=0.52)

    flight_details = {}

    if not check_flight:
        lbl = Label(roots, font=("arial", 15, 'bold'),
                    text="Flight Not Available Or Seats Occupied")
        lbl.place(relx=0.2, rely=0.470)
    else:

        lbl = Label(roots, font=("arial", 15, 'bold'), text="Flight No")
        lbl.place(relx=0.2, rely=0.470)

        lbl = Label(roots, font=("arial", 15, 'bold'), text="Seats Remaining")
        lbl.place(relx=0.3, rely=0.470)

        lbl = Label(roots, font=("arial", 15, 'bold'), text="Departure Time")
        lbl.place(relx=0.45, rely=0.470)

        # header = f"{'Flight No':<15}{'Seats Remaining':<20}{'Departure Time':<25}"
        # flight_listbox.insert(0, header)
        for i, Flight_list in enumerate(check_flight):
            flight_info = f"{Flight_list[0]:<15}{
                Flight_list[1]:<10}{Flight_list[2]:<23}"
            flight_listbox.insert(i, flight_info)
            flight_details[i] = [Flight_list[0],
                                 Flight_list[1], Flight_list[2]]

        Button(roots, text="Select Flight", font=("cursive", 18, 'bold'),
               bg="wheat", activebackground="tan", command=select_flight).place(relx=0.4, rely=0.9)

    roots.mainloop()


def select_flight():
    selected_index = flight_listbox.curselection()
    if selected_index:
        selected_flight_details = flight_details[selected_index[0]]
        flight_no, seats_remaining, departure_time = selected_flight_details
        print("Selected Flight:")
        print("Flight No:", flight_no)
        print("Seats Remaining:", seats_remaining)
        print("Departure Time:", departure_time)
        plus(flight_no, departure_time)
    else:
        messagebox.showinfo("Selection Error", "Please select a flight.")


def plus(flight_no, departure_time):
    global rootp, Passenger_name, email, class1, age, Flight_no, Departure_Time

    Flight_no = flight_no
    Departure_Time = departure_time
    rootp = Tk()
    rootp.geometry('800x450')
    rootp.config(bg="beige")
    rootp.title("Passenger Information")
    Label(rootp, text="Passenger Information", font=(
        "arial", 30, 'bold')).place(relx=0.2, rely=0)

    Label(rootp, font=("arial", 15, 'bold'),
          text="Passenger Name : ").place(relx=0.1, rely=0.2)
    Passenger_name = Entry(rootp, width=35)
    Passenger_name.place(relx=0.5, rely=0.2)

    Label(rootp, font=("arial", 15, 'bold'),
          text="Enter Your Email address : ").place(relx=0.1, rely=0.3)
    email = Entry(rootp, width=35)
    email.place(relx=0.5, rely=0.3)

    Label(rootp, font=("arial", 15, 'bold'),
          text="Choose class").place(relx=0.1, rely=0.4)
    class1 = ttk.Combobox(rootp, height=10, width=30, values=[
        "BusinessClass", "Economy"])
    class1.place(relx=0.5, rely=0.4)

    Label(rootp, font=("arial", 15, 'bold'),
          text="Enter Age:").place(relx=0.1, rely=0.5)
    age = Entry(rootp, width=35)
    age.place(relx=0.5, rely=0.5)
    btn = Button(rootp, font=("cursive", 18, 'bold'),
                 text="Addon preference", command=addon)
    btn.place(relx=0.4, rely=0.6)

    rootp.mainloop()


def addon():
    global root_add, fee, Food, Need_assis, Drink
    root_add = Tk()
    root_add.title("ADD ONS")
    root_add.geometry('800x450')
    root_add.config(bg="beige")

    Label(root_add, font=("arial", 20, 'bold'),
          text="Add Ons").place(relx=0.42, rely=0.1)

    Label(root_add, font=("arial", 15, 'bold'),
          text="Food Preference").place(relx=0.1, rely=0.2)
    Food = ttk.Combobox(root_add, height=10, width=30,
                        values=["Veg", "NonVeg"])
    Food.place(relx=0.45, rely=0.2)

    Label(root_add, font=("arial", 15, 'bold'),
          text="Need Special Assistance :").place(relx=0.1, rely=0.3)
    Need_assis = ttk.Combobox(root_add, height=10, width=30,
                              values=["Yes", "No"])
    Need_assis.place(relx=0.45, rely=0.3)

    Label(root_add, font=("arial", 15, 'bold'),
          text="Any Drink Needed :").place(relx=0.1, rely=0.4)
    Drink = ttk.Combobox(root_add, height=10, width=30,
                         values=["Yes", "No"])
    Drink.place(relx=0.45, rely=0.4)

    bf = Button(root_add, font=("cursive", 20, 'bold'), bg="wheat",
                activebackground="tan", text="Continue Payment", command=pay)
    bf.place(relx=0.3, rely=0.6)

    Label(root_add, font=("arial", 13, 'bold'),
          text="*Note:").place(relx=0.46, rely=0.78)
    Label(root_add, font=("arial", 13, 'bold'),
          text="Veg : Veg Curry and Chapathi/White Rice").place(relx=0.47, rely=0.84)
    Label(root_add, text="Non Veg: Chicken Curry with fried rice/chicken rice ",
          font=("arial", 13, 'bold')).place(relx=0.47, rely=0.9)

    root_add.mainloop()


def pay():
    global root_pay, Payment_status, fee

    Payment_status = 'Pending'
    root_pay = Tk()
    root_pay.title("Pay")
    root_pay.geometry('800x650')
    root_pay.config(bg="beige")

    Label(root_pay, font=("arial", 23, 'bold'),
          text="Payment Details").place(relx=0.32, rely=0.05)

    l_2 = Label(root_pay, font=("arial", 14),
                text=" Card Holder Name : ")
    l_2.place(relx=0.1, rely=0.2)
    en1 = Entry(root_pay, width=35)
    en1.place(relx=0.6, rely=0.2)
    Label(root_pay, font=("arial", 14),
          text="Enter Card Number : ").place(relx=0.1, rely=0.3)
    en2 = Entry(root_pay, width=35)
    en2.place(relx=0.6, rely=0.3)
    Label(root_pay, font=("arial", 14),
          text="Enter Expiry Date").place(relx=0.1, rely=0.4)
    en3 = Entry(root_pay, width=35)
    en3.place(relx=0.6, rely=0.4)
    Label(root_pay, font=("arial", 14),
          text="Enter CVV:").place(relx=0.1, rely=0.5)
    en4 = Entry(root_pay, width=35)
    en4.place(relx=0.6, rely=0.5)

    Label(root_pay, font=("arial", 20),
          text=" Total Amount To Pay :").place(relx=0.1, rely=0.6)
    fees_res = db.fees(Flight_no)
    fees = fees_res[0][0]
    if class1.get() == "BusinessClass":
        fee = fees + 2000
    else:
        fee = fees

    Label(root_pay, font=("arial", 20),
          text=fee).place(relx=0.5, rely=0.6)

    if (en1 and en2 and en3 and en4):
        Payment_status = 'Successful'
        bpay = Button(root_pay, font=("cursive", 20, 'bold'), bg="wheat",
                      activebackground="tan", text="Continue Payment", command=submit)
        bpay.place(relx=0.3, rely=0.8)

    root_pay.mainloop()
    roots.mainloop()


def submit():
    print(Flight_no)
    confirmation = messagebox.askokcancel(
        "Confirmation", "Do you want to Confirm ?")
    Food1 = Food.get()
    Need_assis1 = Need_assis.get()
    Drink1 = Drink.get()

    if confirmation:

        db.Booking_insert(User, Passenger_name.get(), email.get(), age.get(),
                          Flight_no, Departure_Time, class1.get(), fee, Payment_status)
        db.addon_insert(Food1, Need_assis1, Drink1)

        rootp.destroy()
        root_add.destroy()
        roots.destroy()
        root_pay.destroy()
