COORDINATES = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
from turtle import Turtle
class Snake :

    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]  # Adding the head attribute


    def create_snake(self):
        
        for i in COORDINATES:
            self.add_segment(i)
        

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.turtle_list.append(new_segment)  

    def extension(self):
        self.add_segment(self.turtle_list[-1].position())     

    def move(self):
        
        for num in range(len(self.turtle_list)-1, 0,-1):
            new_x = self.turtle_list[num -1].xcor()
            new_y = self.turtle_list[num -1].ycor()
            self.turtle_list[num].goto(new_x, new_y)
        self.turtle_list[0].forward(20)
    
    def right(self):
        if self.turtle_list[0].heading() != LEFT:
            self.turtle_list[0].setheading(RIGHT)
        
        

    def left(self):
        if self.turtle_list[0].heading() != RIGHT:
            self.turtle_list[0].setheading(LEFT)
        

    def up(self):
        if self.turtle_list[0].heading() != DOWN:
            self.turtle_list[0].setheading(UP)
        
    
    def down(self):
        if self.turtle_list[0].heading() != UP:
            self.turtle_list[0].setheading(DOWN)

   
        


