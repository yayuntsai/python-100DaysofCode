from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
MOVE_DEGREE = 90

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

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
        self.segments[0].forward(MOVE_DISTANCE)
        self.segments[0].left(MOVE_DEGREE)
