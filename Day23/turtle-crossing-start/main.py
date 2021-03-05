import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_brick()
    car_manager.move_cars()

    # Detect car collision
    for car in car_manager.all_cars:
        if player.distance(car) < 10:
            game_is_on = False
            scoreboard.lose_game()

        elif player.ycor() > 280:
            game_is_on = False
            scoreboard.win_game()


screen.exitonclick()