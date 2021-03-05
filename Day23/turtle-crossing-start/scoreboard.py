from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def lose_game(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def win_game(self):
        self.goto(0, 0)
        self.write("WIN", align="center", font=FONT)
