from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard
from boundary import Boundary
from bigfood import BigFood




screen=Screen()
boundary = Boundary()
snake=Snake()
food=Food()
score=ScoreBoard()


screen.setup(width=600,height=615)
screen.bgcolor("Black")
screen.title("My Snake Game")
screen.tracer(0)


starting_pos=0

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

counter_big_food=0

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect Collision With Food
    if snake.head.distance(food) < 15:
        food.refresh()
        counter_big_food+=1
        snake.extend()
        score.update()

    big_food=None

    # if counter_big_food == 5:
    #     big_food = BigFood()
    #     if snake.head.distance(big_food) < 25:
    #         counter_big_food=0
    #         for i in range(1,3):
    #             snake.extend()
    #         score.update(True)
    #         big_food.hideturtle()
    #         big_food = None
    #Detect Collision With Wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        game_is_on=False
        score.game_over()

    #Detect Collision with body

    for segment in snake.snake[1:-1]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            score.game_over()

screen.exitonclick()