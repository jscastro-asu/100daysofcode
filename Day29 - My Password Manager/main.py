from tkinter import *
from random import *
from tkinter import messagebox
import string
import pyperclip
characters = string.ascii_letters + string.punctuation  + string.digits

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    password_textbox.delete(1,END)
    password_var =  "".join(choice(characters) for x in range(randint(8, 16)))
    password_textbox.insert(0, password_var)
    pyperclip.copy(password_var)
    randompw_button.config(text="Copied to Clipboard")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():
    my_file = open("data.txt", "a")
    my_file.write(website_var.get() + " | ")
    my_file.write(email_var.get() + " | ")
    my_file.write(password_var.get() + "\n")
 
    website_var.set("")
    my_file.close()
    
    website_textbox.delete(0, END)
    password_textbox.delete(0, END)
    return messagebox.showinfo("Add","Secret Saved.")
   
# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("JEN PASSWORD MANAGER")
root.config(pady=60, padx=60)
root.geometry=("500x500")
root.resizable = False

website_var = StringVar()
email_var = StringVar()
password_var = StringVar()

canvas = Canvas(width=300, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text = "Website:", font=("Tahoma", 13, "normal"))
website_label.grid(row=1, column=0)
website_textbox = Entry(textvariable = website_var, width=35)
website_textbox.grid(row=1, column=1, sticky='w', columnspan=2)
website_textbox.focus()

username_label = Label(text = "Email/Username:", font=("Tahoma", 13, "normal"))
username_label.grid(row=2, column=0)
username_textbox = Entry(textvariable = email_var, width=35)
username_textbox.grid(row=2, column=1, sticky='w')
username_textbox.insert(0, "jen@castro.com")

password_label = Label(text = "Password:", font=("Tahoma", 13, "normal"))
password_label.grid(row=3, column=0, )
password_textbox = Entry(textvariable = password_var, show = "*", width=21)
password_textbox.grid(row=3, column=1, sticky='w')

randompw_button = Button(text="Generate Password", font=("Tahoma", 13, "normal"), command=lambda:password_gen())
randompw_button.grid(row=3, column=1, sticky="e")
   

add_button = Button(text="Add", width=36, font=("Tahoma", 13, "normal"), command=lambda:save_entry())
add_button.grid(row=4, column=1, sticky = 'w', columnspan=2)


root.mainloop()

