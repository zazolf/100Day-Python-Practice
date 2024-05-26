#import colorgram
#colors = colorgram.extract(r"C:\Users\zolfa\Desktop\Hirst.jpg", 20)
#new_color_list = []
#
#for item in colors:
#    r = item.rgb.r
#    g = item.rgb.g
#    b = item.rgb.b
#    rgb = (r,g,b)
#    new_color_list.append(rgb)
#print(new_color_list)
#
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255) 
tim = Turtle()
tim.speed("fastest")


def horizental_move():
    for i in range(10):
        color = random.choice(color_list)        
        tim.dot(20,color)
        tim.penup()
        tim.forward(50)
        tim.pendown()

def vertical_move():
    tim.penup()
    tim.left(90) 
    tim.forward(50)
    tim.left(90) 
    tim.forward(500) 
    tim.left(180)  

tim.penup()
tim.goto(-200,-200)
tim.pendown()
for i in range(10):

    horizental_move()
    vertical_move()





 
screen.exitonclick()


