import turtle
from turtle import Screen
from snake import Snack
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snack Game")
screen.tracer(0)

snake = Snack()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()











screen.exitonclick()