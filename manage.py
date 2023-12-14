import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import db

connection = db.create_connection()


def cancel():
    global root_cancel
    root_cancel = Tk()
    root_cancel.config(bg="beige")
    root_cancel.state("zoomed")
    root_cancel.title("Manage")

    # manage

    cursor = connection.cursor()
    cursor.execute("SELECT  Ticket_NO , User , Passenger_name , email , PhNo , Flight_no , Departure_date , Class , Fee , Payment_status , booking_sts  FROM  booking  ")
    results = cursor.fetchall()

    # Create a Treeview widget
    tree = ttk.Treeview(root_cancel)
    tree["columns"] = ("Ticket_NO ", "User ", "Passenger_name ", "email ", "PhNo ",
                       "Flight_no ", "Departure_date ", "Class ", "Fee ", "Payment_status ", "booking_sts ")

    # Add column headers
    columns = ["Ticket_NO ", "User ", "Passenger_name ", "email ", "PhNo ", "Flight_no ",
               "Departure_date ", "Class ", "Fee ", "Payment_status ", "booking_sts "]
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor=tk.CENTER)  # Adjust width as needed

    # Populate the Treeview with data

    # Add custom colors to alternating rows
    for i, ro in enumerate(results):
        if i % 2 == 0:
            tree.tag_configure('evenrow', background='#f0f0f0')
            tree.insert('', 'end', values=ro, tags=('evenrow',))
        else:
            tree.insert('', 'end', values=ro)
    # Pack the Treeview widget

    # Pack the Treeview widget
    tree.pack(expand=True, fill="both")
    tree.pack()

    Label(root_cancel, font=("arial", 15, 'bold'),
          text="Ticket Number : ").place(x=350, y=550)
    enter6 = Entry(root_cancel, width=35)
    enter6.place(x=600, y=550)

    def de():
        tno = enter6.get()
        Delete = "delete from booking where Ticket_NO="+tno
        cursor.execute(Delete)
        messagebox.showinfo("Information", "TICKET CANCELLED")
        root_cancel.destroy()
        messagebox.showinfo("Success", "You have cancelled your flight")
        messagebox.showinfo(
            "Refund", "60%% refund has been credited to your account")
    btn_c = Button(root_cancel, text="Cancel Flight", font=(
        "cursive", 22, 'bold'), activebackground="tan", command=de)
    btn_c.place(x=600, y=600)

    root_cancel.mainloop()
