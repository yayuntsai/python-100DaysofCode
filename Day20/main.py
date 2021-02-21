from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0) #Trace the screen and update screen after every events had done

segments = []
starting_position = [(0,0), (-20,0), (-40,0)]

for position in starting_position:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup() # remove white line of trajectory
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg in segments:
        seg.forward(20)

