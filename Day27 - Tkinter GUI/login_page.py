from email import message
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Login")
window.geometry("370x250")
window.config(padx=30, pady=30)

greet = Label(text="Hello there.", 
            font=("Consolas", 20, "bold")
            )  
greet.pack() 


# label widget
def login():

    get_eml = ent_email.get()
    get_pw = ent_pw.get()
    
    
    if get_eml == "jen@castro.com" and get_pw == "censored":
        return messagebox.showinfo("Login",f"Success! Hello {get_eml}")
    else:
        return messagebox.showinfo("Login","Login failed.")

Label(text="Enter Email:").place(x=40, y=100, anchor = CENTER)
ent_email = Entry()
ent_email.place(x=200, y=100, anchor = CENTER)

Label(text="Enter Password").place(x=50, y=140, anchor = CENTER)
ent_pw = Entry(show="*")
ent_pw.place(x=200, y=140, anchor = CENTER)

login_btn = Button(text="Login", command = login)
login_btn.place(x=200, y=180, anchor = CENTER)
    
  



window.mainloop()