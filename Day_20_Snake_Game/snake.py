COORDINATES = [(0,0), (-20,0), (-40,0)]
from turtle import Turtle
class Snake :

    def __init__(self):
        self.turtle_list = []
        self.create_snake()

    def create_snake(self):
        
        for i in COORDINATES:
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(i)
            self.turtle_list.append(turtle)

    def move(self):
        
        for num in range(len(self.turtle_list)-1, 0,-1):
            new_x = self.turtle_list[num -1].xcor()
            new_y = self.turtle_list[num -1].ycor()
            self.turtle_list[num].goto(new_x, new_y)
        self.turtle_list[0].forward(20)


