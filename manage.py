import tkinter as tk
from tkinter import *
from tkinter import ttk
import db


def on_treeview_scroll(*args):
    tree.xview(*args)


def de():
    tno = enter6.get()
    res = db.Cancel_ticket(tno)
    if res:
        root_cancel.destroy()


def cancel():
    global enter6, root_cancel, tree
    root_cancel = Tk()
    root_cancel.config(bg="beige")
    root_cancel.state("zoomed")
    root_cancel.title("Manage Bookings")

    # manage
    results = db.manage_fetch()

    # Create a Treeview widget
    tree = ttk.Treeview(root_cancel, height=5)
    tree["columns"] = ("Ticket_NO", "Passenger_name", "email", "age",
                       "Flight_no", "Departure_Time", "Class", "Fee", "Payment_status")

    # Add column headers
    columns = ["Ticket_NO", "Passenger_name", "email", "age",
               "Flight_no", "Departure_Time", "Class", "Fee", "Payment_status"]

    for i, col in enumerate(columns):
        # Explicitly set the width for each column
        tree.column(i, width=150, anchor=tk.CENTER)
        tree.heading(i, text=col, anchor=tk.CENTER)

    # Add custom colors to alternating rows
    for i, ro in enumerate(results):
        tag = 'evenrow' if i % 2 == 0 else 'oddrow'
        tree.tag_configure(tag, background='#ffb6c1' if tag ==
                           'evenrow' else '#ADD8E6')
        tree.insert('', 'end', values=ro, tags=(tag,))

    # Create horizontal scrollbar
    hsb = ttk.Scrollbar(root_cancel, orient="horizontal",
                        command=on_treeview_scroll)
    hsb.place(x=220, y=352, width=899)

    # Set the scrollbar to control the x-axis of the Treeview
    tree.configure(xscrollcommand=hsb.set)

    # Pack the Treeview widget
    tree.place(x=220, y=70, width=900, height=300)

    # cancel block
    Label(root_cancel, font=("arial", 22, 'bold'),
          text="Cancel Booking").place(x=610, y=470)
    Label(root_cancel, font=("arial", 15, 'bold'),
          text="Ticket Number : ").place(x=350, y=550)
    enter6 = Entry(root_cancel, width=35)
    enter6.place(x=600, y=550)

    btn_c = Button(root_cancel, text="Cancel Flight", font=(
        "cursive", 15, 'bold'), activebackground="tan", command=de)
    btn_c.place(x=600, y=600)

    root_cancel.mainloop()
