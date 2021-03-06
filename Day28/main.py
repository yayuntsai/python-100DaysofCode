from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None #timer default to make it a global variables

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    timer_text.config(text="5:00")
    timer_label.config(text="Timer")
    check_mark.config(text="✓", fg="green")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # START AND BREAK CONDITIONS
    # rep = 8th
    if reps % 8 == 0:
        count_down(long_break_sec)
        canvas.itemconfig(timer_label, text="Break", fg="pink")
    # rep = 2nd/4th/6th
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg="pink")
    # rep = 1st/3rd/5th/7th
    else:
        count_down(work_sec)
        timer_label.config(text="Working", fg="green")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    #time format
    global reps, timer
    minute_text = math.floor(count/60)
    sec_text = count % 60

    if sec_text < 10:
        sec_text = f"0{sec_text}"

    canvas.itemconfig(timer_text, text=f"{minute_text}:{sec_text}")
    if count > 0:
        timer = window.after(10, count_down, count-1) #timer count down
    else:
        start_timer()
        mark = ""
        mark_session = math.floor(reps/2)
        for i in range(mark_session):
            mark += "✓"
        check_mark.config(text=mark, fg="green")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)


check_text = "✓"
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)


timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
timer_label = Label(window, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
timer_label.grid(row=0, column=1)

start_button = Button(window, text="Start", activebackground=PINK, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(window, text="Reset", activebackground=PINK, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(window, text=check_text, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_mark.grid(row=4, column=1)


canvas.grid(row=1, column=1)

window.mainloop()