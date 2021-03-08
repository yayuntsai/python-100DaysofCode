from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#7D96DF"

class QuizeIntetface:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title('Quiz App')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        # question block
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some question text",
            width=280,
            font=("Arial", 20, "normal"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_icon = PhotoImage(file="images/true.png")
        false_icon = PhotoImage(file="images/false.png")
        true_button = Button(image=true_icon,
                             highlightthickness=0,
                             width=30,
                             height=30)
        false_button = Button(image=false_icon,
                              highlightthickness=0,
                              width=30,
                              height=30)
        true_button.grid(row=5, column=0)
        false_button.grid(row=5, column=1)

        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

