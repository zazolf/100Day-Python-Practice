from turtle import Turtle, Screen
from snake import Snake
import time
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#step 1. create a snake body
snake = Snake()

     

#step 2. move the snake
#def turn_right():
#    turtle.right(90)
#
#def turn_left():
#    turtle.left(90)
#
game_is_on = True
while game_is_on: 
    screen.update()
    time.sleep(0.1)
    snake.move()
    #screen.listen()
    #screen.onkey(key = "Right", fun = turn_right)
    #screen.onkey(key = "Left", fun = turn_left)
screen.exitonclick()


   