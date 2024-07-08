from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
import os

print("Current working directory:", os.getcwd())


screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


#step 1. create a snake body
snake = Snake()
food = Food()
score = Score()

#step 2. move the snake

screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Right", fun = snake.right)
screen.onkey(key = "Left", fun = snake.left)

game_is_on = True
while game_is_on: 
    screen.update()    
    time.sleep(0.1)
    snake.move() 
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extension()
    #detect collision with walls
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() >280:
        game_is_on = False
        score.game_over()
        #score.reset_score()
    #detect collision with tail
    for segment in snake.turtle_list[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
            score.reset_score()

    
    

screen.exitonclick()


   