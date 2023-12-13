import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import db


def cancel():
    global root_cancel
    root_cancel = Tk()
    root_cancel.config(bg="beige")
    root_cancel.state("zoomed")
    root_cancel.title("CANCEL")
    Label(root_cancel, font=("arial", 20, 'bold'),
          text="Cancel Booking").place(relx=0.45, rely=0.1)
    Label(root_cancel, font=("arial", 15, 'bold'),
          text="Enter Name of passenger").place(relx=0.35, rely=0.2)
    enter6 = Entry(root_cancel, width=35)
    enter6.place(relx=0.6, rely=0.2)
    Label(root_cancel, font=("arial", 15, 'bold'),
          text="Choose class").place(relx=0.35, rely=0.3)
    w2 = ttk.Combobox(root_cancel, height=10, width=30,
                      values=["BusinessClass", "Economy"])
    w2.place(relx=0.55, rely=0.3)
    Label(root_cancel, font=("arial", 15, 'bold'),
          text="Enter flight number").place(relx=0.35, rely=0.4)
    w3 = Entry(root_cancel, width=30)
    w3.place(relx=0.55, rely=0.4)

    btn_c = Button(root_cancel, text="Cancel Flight", font=(
        "cursive", 22, 'bold'), activebackground="tan", command=cancel1)
    btn_c.place(relx=0.45, rely=0.5)

    root_cancel.mainloop()


def cancel1():
    root_cancel.destroy()
    messagebox.showinfo(
        "Success", "You have cancelled your flight")
    messagebox.showinfo(
        "Refund", "60%% refund has been credited to your account")
