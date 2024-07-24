import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
cars = CarManager()
score = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.move_cars()
    cars.create_cars()

#     Detect the cars

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    #    Detect the success line
    if player.is_at_finish():
        player.goto_start()
        cars.level_up()
        score.increase_levelf()

screen.exitonclick()