from dataclasses import fields
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import ImageTk, Image

root = Tk()
root.title("Panda World")
root.geometry("500x400")
root.resizable(False, False)
root.config(padx=30, pady=40)


l0 = Label(text = "Create New Account",font=("Consolas", 20, "bold"),anchor = CENTER)
l0.pack()

variable = StringVar(root)

l1 = Label(text = "Full Name* ")
l1.place(x=90,y=60)
e1 = Entry()
e1.place(x=180,y=60)

l2 = Label(text = "Email Addr*  ")
l2.place(x=90,y=90)
e2 = Entry()
e2.place(x=180,y=90)

pw = Label(text = "Password* ")
pw.place(x=90,y=120)
pw = Entry(show = "*")
pw.place(x=180,y=120)

l3 = Label(text = "Gender  ")
l3.place(x=90,y=150)
var = IntVar()
Radiobutton(text="Male", variable=var, value=1).place(x=300,y=150)
Radiobutton(text="Female", variable=var, value=2).place(x=200,y=150)

l4 = Label(text = "State  ")
l4.place(x=90,y=180)
drop4 = OptionMenu(root, variable,"Washington", "California", "Oregon", "Hawaii")
drop4.place(x=180,y=180, width = 100)

l5 = Label(text = "Date of Birth  ")
l5.place(x=90,y=210)

cal = DateEntry(width=12, background='black', foreground='orange', borderwidth=2)
cal.pack(padx=15, pady=15)
cal.place(x=180, y=210)



def reg():
    check_counter=0

    if e1.get() == "":
        return messagebox.showinfo("Submit", "Name is required.")
    else:
        check_counter += 1
    
    if e2.get() == "":
        return messagebox.showinfo("Submit", "Email is required.")
    else:
        
        check_counter += 1
        
    if pw.get() == "" or len(pw.get()) < 8:
        return messagebox.showinfo("Submit", "Atleast 8-char password is required.")
    else:
        check_counter += 1

    if check_counter == 3:
        messagebox.showinfo("Submit","Registration Complete.")
                                   
        new_window = Toplevel(root)
        new_window.geometry("300x200")
        new_window.resizable(False, False)
        Label(new_window, text=(f"Hey, Welcome!"), font=("Arial", 17, "bold")).pack(pady=30)
        Button(text="Play Game?")

reg_btn = Button(text="Submit",width=10, bg="black", fg="black",relief="flat", command = reg)   
reg_btn.place(x=220, y=300, anchor = CENTER)





root.mainloop()