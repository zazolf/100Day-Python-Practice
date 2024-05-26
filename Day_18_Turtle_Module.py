#Challenge 2 >> Draw a Dashed Line
from turtle import Turtle, Screen
tim = Turtle()
#for i in range(10):

    #tim.forward(10)
 #   tim.penup()
 #   tim.forward(10)  # Move forward without drawing
 #   tim.pendown()

#screen = Screen()
#screen.exitonclick()

#Challenge 3 >> Draw some shapes
#
import random
#side_list = [3,4,5,6,7,8,9,10]
#for n in side_list:

    #for i in range(n):
        #tim.forward(100)
        #tim.right(360/n)


#Challenge 4 >> Draw a random line 
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim.pensize(2)
tim.speed("fastest")
#for i in range(50):
  #color = random.choice(colours)
  #tim.color(color)
  #angle = [0,90,180,270]
  #tim.forward(20)
  #tim.setheading(random.choice(angle))


#Challenge 5 >> Draw a circle pattern

def circle_shape(angle):
    for i in range(int(360/angle)):
        color = random.choice(colours)
        tim.color(color)
        tim.circle(100)
        tim.left(angle)
circle_shape(10)
    