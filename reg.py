from tkinter import *
import db
import tkinter.messagebox as mymessagebox
import booking

# login


def login():
    global UserTxt, PassTxt, root_login
    root_login = Tk()
    root_login.config(bg="beige")
    root_login.title("LOGIN")
    root_login.geometry("500x300")

    Label(root_login, font=("arial", 20, 'bold'),
          text="Login").place(x=225, y=53)

    Label(root_login, font=("arial", 15, 'bold'),
          text="Username : ").place(x=80, y=130)
    UserTxt = Entry(root_login, width=35, font=("bold", 10))
    UserTxt.place(x=240, y=130)
    UserTxt.focus()

    Label(root_login, font=("arial", 15, 'bold'),
          text="Enter Password : ").place(x=68, y=180)
    PassTxt = Entry(root_login, width=35,  font=("bold", 10))
    PassTxt .place(x=240, y=180)
    PassTxt.config(show="*")

    Button(root_login, text="Login", command=ClicktoLogin, width=20, bg='brown',
           fg='white').place(x=100, y=230)
    Button(root_login, text="Registration", command=registration, width=20, bg='brown',
           fg='white').place(x=260, y=230)


def ClicktoLogin():

    user = UserTxt.get()
    passtxt = PassTxt.get()
    myresult = db.login(user, passtxt)
    if myresult != None:
        mymessagebox.showinfo("Success", "Successfully Login")
        root_login.destroy()
        booking.book(user)

    else:
        mymessagebox.showerror("Error", "Invalid User Name And Password")


# registration
def registration():
    root_login.destroy()
    global fullname, Email, varblbl, Age, Password, base
    base = Tk()
    base.geometry('500x500')
    base.title("Registration Form")

    labl_0 = Label(base, text="Registration form", width=20, font=("bold", 20))
    labl_0.place(x=90, y=53)
    labl_0.focus()

    labl_1 = Label(base, text="FullName", width=20, font=("bold", 10))
    labl_1.place(x=80, y=130)
    fullname = Entry(base, width=35, font=("bold", 10))
    fullname.place(x=230, y=130)
    fullname.focus()

    labl_2 = Label(base, text="Email", width=20, font=("bold", 10))
    labl_2.place(x=68, y=180)
    Email = Entry(base, width=35, font=("bold", 10))
    Email.place(x=230, y=180)
    Email.focus()

    labl_3 = Label(base, text="Gender", width=20, font=("bold", 10))
    labl_3.place(x=70, y=230)
    varblbl = IntVar()
    Radiobutton(base, text="Male", padx=5, variable=varblbl,
                value=1).place(x=235, y=230)
    Radiobutton(base, text="Female", padx=20,
                variable=varblbl, value=2).place(x=290, y=230)

    labl_4 = Label(base, text="Age:", width=20, font=("bold", 10))
    labl_4.place(x=70, y=280)
    Age = Entry(base, width=35, font=("bold", 10))
    Age.place(x=230, y=280)
    Age.focus()

    labl_5 = Label(base, text="Password:", width=20, font=("bold", 10))
    labl_5.place(x=70, y=330)
    Password = Entry(base, width=35, font=("bold", 10))
    Password.place(x=230, y=330)
    Password.focus()

    Button(base, text="Submit", command=reg, width=20, bg='brown',
           fg='white').place(x=180, y=380)
    # it will be used for displaying the registration form onto the window
    base.mainloop()


def reg():

    name = fullname.get()
    passkey = Password.get()
    mail = Email.get()
    Gender = varblbl.get()
    age = Age.get()

    if ((name and passkey and mail and Gender and age)):
        db.Registration(name, passkey, mail, Gender, age)

    base.destroy()
    login()
