from turtle import Screen
from snake import Snake
from food import Food
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0) #Trace the screen and update screen after every events had done

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect the distance between food and snake
    if snake.head.distance(food) < 15:
        print("collide")

screen.exitonclick()