from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.create_brick()

    def create_brick(self):
        new_car = Turtle('square')
        new_car.penup()  # 不會畫軌跡
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        rand_y = random.randint(-250, 250)  # 不讓食物落在y邊界上
        new_car.goto(300, rand_y)
        self.all_cars.append(new_car)
