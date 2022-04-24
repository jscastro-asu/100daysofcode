from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
main_timer = None

root = Tk()
root.title("JEN POMODORO")
root.config(padx = 100, pady =50, bg=YELLOW)

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    root.after_cancel(main_timer)
    timer.config(text="Timer")
    canvas.itemconfig(timer_text, text=("00:00"))
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN
    
    if reps % 2 == 0:
        countdown(short_break)
        timer.config(text = "Short Break",font=(FONT_NAME, 45, "bold"), fg = PINK)
    elif reps % 8 == 0:
        countdown(long_break)
        timer.config(text = "Long Break", font=(FONT_NAME, 45, "bold"), fg = RED)
    else:
        countdown(work)
        timer.config(text = "Work Time",font=(FONT_NAME, 45, "bold"), fg = GREEN)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count): 
    global main_timer
    count_min = math.floor(count / 60) 
    count_sec = count % 60
    # Dynamic typing allows for changing the data type of a variable
    # Just by assigning it to a different kind of value
    # When dynamic typing is not used then

    if count_sec < 10:
        count_sec = (f"0{count_sec}")
    
    canvas.itemconfig(timer_text, text=(f"{count_min}:{count_sec}"))
    if count > 0:
        # call countdown again after 1000ms (1s), use after instead
        main_timer = root.after(1000, countdown, count-1)
    else:
        start_timer()
        #for every 2 reps completed, then it shows check
        marks = ""
        # avoid float
        work_sesh = math.floor(reps/2) 
        for w in range(work_sesh):
            marks += "✔"
        check.config(text=marks)
        
        
# ---------------------------- UI SETUP ------------------------------- #
# face of the app
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 135, text="00:00", fill = "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

# the 00:00 start time
timer = Label(text="Timer",font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=1,row=0)

# when 25 minutes has completed, it appends check mark
check = Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME, 35, "bold"))
check.grid(column=1, row=4)

# triggers timer to begin
start_btn = Button(text="Start",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"), command = start_timer)
start_btn.grid(column=0,row=5)

# start over timer
reset_btn = Button(text="Reset", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"), command = reset_timer)
reset_btn.grid(column=3,row=5)

root.mainloop()
    
