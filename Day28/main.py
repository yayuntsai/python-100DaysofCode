from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

check_text = "✓"
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
timer_label = Label(window, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
timer_label.grid(row=0, column=1)
start_button = Button(window, text="Start", activebackground=PINK, highlightthickness=0)
start_button.grid(row=2, column=0)
reset_button = Button(window, text="Reset", activebackground=PINK, highlightthickness=0)
reset_button.grid(row=2, column=2)
check_mark = Label(window, text=check_text, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_mark.grid(row=4, column=1)

canvas.grid(row=1, column=1)

window.mainloop()