import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
score=Score()
screen.listen()

turtle.onkey(snake.move_up, "Up")
turtle.onkey(snake.move_right, "Right")
turtle.onkey(snake.move_left, "Left")
turtle.onkey(snake.move_down, "Down")


game_on=True
while game_on==True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision of snake with food
    distance=snake.snake_segment[0].distance(food.xcor(),food.ycor())
    if distance<15:
        food.go_move()
        snake.add_segment()
        score.game_score()
    # Detect collision to the wall
    if snake.snake_segment[0].xcor()>295 or snake.snake_segment[0].xcor()<-295 or snake.snake_segment[0].ycor()>295 or snake.snake_segment[0].ycor()<-295:
        score.game_over()
        game_on=False

    # Detect collision with tail
    for segment in snake.snake_segment[1:]:
        if snake.snake_segment[0].distance(segment.xcor(),segment.ycor())<10:
            score.game_over()
            game_on = False







screen.exitonclick()


