from tkinter import *

root = Tk()
root.title("Mile to Km Converter")
root.geometry("250x130")
root.resizable(False, False)
root.config(padx=20, pady=20)


def calc():
    m = float(mi_entry.get())
    km = m * 1.609
    ans_lbl.config(text=f"{km}")


mi_entry = Entry(width = 5)
mi_entry.grid(column=1, row=2)

mi_lbl = Label(text = "mile/s")
mi_lbl.grid(column=2, row = 2)

eql_lbl = Label(text = "is equal to")
eql_lbl.grid(column=0, row = 3 )

ans_lbl = Label(text = "0")
ans_lbl.grid(column=1, row=3)

km_lbl = Label(text = "km")
km_lbl.grid(column=2, row =3 )

calc_btn = Button(text="Calculate",width=5, bg="black", fg="black",relief="flat", command = calc)
calc_btn.grid(column=1, row=4)








root.mainloop()