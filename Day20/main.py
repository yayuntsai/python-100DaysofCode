from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
turtle1 = Turtle()
turtle2 = Turtle()
turtle3 = Turtle()
turtle1.color('white')
turtle1.shape('square')
turtle2.color('white')
turtle2.shape('square')
turtle2.goto((-20,0))
turtle3.color('white')
turtle3.shape('square')
turtle3.goto((-40,0))




screen.exitonclick()