from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    turtle = Turtle()
    turtle.setheading(90) # 設定turtle朝向哪一邊

    turtle.shape("turtle")

    def __init__(self):
        pass

    def up(self):
        self.foward(0, -270)

