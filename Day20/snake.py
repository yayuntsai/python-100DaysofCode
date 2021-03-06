from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0), (-100, 0), (-120, 0), (-140, 0), (-160, 0)]
MOVE_DISTANCE = 20
MOVE_DEGREE = 0
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Make snake
        for position in STARTING_POSITION:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()  # remove white line of trajectory

            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # (start, end , step)
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # 一起移動的距離

    def right(self):
        if self.head.heading() != LEFT:  # 設定不可直接反方向運行
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:  # 設定不可直接反方向運行
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:  # 設定不可直接反方向運行
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:  # 設定不可直接反方向運行
            self.head.setheading(DOWN)