
from sqlite3.dbapi2 import Cursor, SQLITE_ATTACH
from tkinter import *
from tkinter import  messagebox
import sqlite3

conn = sqlite3.connect('my_db.db')
c = conn.cursor()


def login():
    user = str(username_login_entry.get())
    psw = str(password_login_entry.get())
   
    statement = """SELECT * FROM login_details """
    c.execute(statement)
    data = c.fetchone()
   
    if data[0] == user and data[1] == psw:
        messagebox.showinfo("Success","Login Successfull!")
        main_screen.destroy()
        import page2
    else:
        messagebox.showinfo("Invalid Credential!","Enter valid details")
    
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x300")
    main_screen.title("UpTime")
    Label(text="Welcome to Talouns!",fg = "#022a5d",width="300", height="1", font=("Calibri 36 bold")).pack()
    Label(text="").pack()
    Label(text="Enter your Credentials to Login:",fg = "#022a5d",font =("Calibri 12")).pack()

    global username_login_entry
    global password_login_entry
 
    Label(main_screen, text="Username:",fg = "#022a5d", height="1", font=("Calibri 15 bold")).pack()
    username_login_entry = Entry(main_screen)
    username_login_entry.pack()
    Label(main_screen, text="").pack()
    Label(main_screen, text="Password:",fg = "#022a5d", height="1", font=("Calibri 15 bold")).pack()
    password_login_entry = Entry(main_screen, show= '*')
    password_login_entry.pack()

    Label(main_screen, text="").pack()
    
    Button(text="Click to Login",fg = "#022a5d", font=("Calibri 15 bold"),height="1", width="14", command = login).pack()
    Label(text="").pack()

    main_screen.mainloop()
 
main_account_screen()