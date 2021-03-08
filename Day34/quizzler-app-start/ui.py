from tkinter import *
import data
THEME_COLOR = "#375362"

class QuizeIntetface:

    def __init__(self):
        self.window = Tk()
        self.window.title('Quiz App')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
        # question block
        self.question_text = self.canvas.create_text(150, 125, text="Some question text", width=250, font=("Arial", 20, "normal"))
        self.canvas.grid(row=1, column=0, columnspan=2)

        true_icon = PhotoImage(file="images/true.png")
        false_icon = PhotoImage(file="images/false.png")
        true_button = Button(image=true_icon, highlightthickness=0)
        false_button = Button(image=false_icon, highlightthickness=0)
        true_button.grid(row=5, column=0)
        false_button.grid(row=5, column=1)

        self.window.mainloop()

    # canvas = Canvas(width=300, height=300)
    # #canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
    #
    # canvas.grid(row=0, column=0)
    #



