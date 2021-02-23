from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('yellow')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()  # 不會畫軌跡
        self.speed('fastest')
        rand_x = random.randint(-280, 280)  # 不讓食物落在x邊界上
        rand_y = random.randint(-280, 280)  # 不讓食物落在y邊界上
        self.goto(rand_x, rand_y)

