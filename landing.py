import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import reg

# creating root window
root = tk.Tk()
root.title("Front Page")
root.state("zoomed")
root.config(bg="beige")

# Create a canvas for the background
canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)
# Add a background image (replace 'background_image.png' with your image file)
background_image = tk.PhotoImage(file="bg2.png")
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)


# creating title 1 as button
sch = " DAV Sr Secondary School"
lbl_sch = tk.Button(root, font=("cursive", 17, 'bold'),
                    width=len(sch), bg="wheat", activebackground="peru")
lbl_sch.place(relx=0.359, rely=0.0)
# to display title 1 letter by letter


def animate_label(text, n=0):
    if n < len(text)-1:
        lbl_sch.after(150, animate_label, text, n+1)
    lbl_sch['text'] = text[:n+1]


root.after(150, animate_label, sch)  # calling off the function


# creating title 2 as a button
csc = "Computer Science Project"
lbl_csc = tk.Button(root, font=("Helvetica", 14, 'bold'),
                    width=len(csc), bg="wheat", activebackground="tan")
# to display title 2 letter by letter


def animate_label_csc(text, n=0):
    if n < len(text)-1:
        lbl_csc.after(150, animate_label_csc, text, n+1)
    lbl_csc['text'] = text[:n+1]


root.after(150, animate_label_csc, csc)  # calling off the function
# placing title 2 in the particular coordinates
lbl_csc.place(relx=0.38, rely=0.08)


# creating title 3 as button
pr = "Airline Reservation"
lbl_pr = tk.Button(root, font=("fantasy", 18, 'bold'),
                   width=len(pr), bg="wheat", activebackground="peru")
# placing title 3 in the particular coordinates
lbl_pr.place(relx=0.381, rely=0.15)
# to display title 3 letter by letter


def animate_label_pr(text, n=0):
    if n < len(text)-1:
        lbl_pr.after(150, animate_label_pr, text, n+1)
    lbl_pr['text'] = text[:n+1]


root.after(150, animate_label_pr, pr)  # calling off the function


# creating title 4 as a button
btn_dn = tk.Button(root, text="DONE BY : ", bg="wheat", font=(
    "serif", 14, 'bold'), activebackground="tan")
# placing title 4 in the particular coordinates
btn_dn.place(relx=0.8, rely=0.7)


# creating title 5 as a label
n1 = "Kanishka Rane D"
lbl_n1 = tk.Label(root, font=("arial", 13, 'bold'), width=len(pr), bg="wheat")
# placing title 5 in the particular coordinates
lbl_n1.place(relx=0.8, rely=0.8)
# to display title 5 letter by letter


def animate_label_n1(text, n=0):
    if n < len(text)-1:
        lbl_n1.after(150, animate_label_n1, text, n+1)
    lbl_n1['text'] = text[:n+1]


root.after(150, animate_label_n1, n1)  # calling off the function


# creating title 6 as a label
n2 = "K.Sri Elakya"
lbl_n2 = tk.Label(root, font=("arial", 13, 'bold'), width=len(pr), bg="wheat")
# placing title 6 in the particular coordinates
lbl_n2.place(relx=0.8, rely=0.85)
# to display title 6 letter by letter


def animate_label_n2(text, n=0):
    if n < len(text)-1:
        lbl_n2.after(150, animate_label_n2, text, n+1)
    lbl_n2['text'] = text[:n+1]


root.after(150, animate_label_n2, n2)  # calling off the function

# signup


def signup():
    root.destroy()
    reg.login()


cont = tk.Button(root, text="CONTINUE", bg="wheat", font=(
    "serif", 14, 'bold'), activebackground="tan", command=signup)
cont.place(relx=0.1, rely=0.85)

root.mainloop()
