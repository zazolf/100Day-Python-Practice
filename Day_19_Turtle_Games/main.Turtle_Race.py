from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color_list = ["red","blue","orange","yellow","purple","green"]
y = 150
turtle_list = []
for item in color_list:
    turtle = Turtle(shape="turtle")
    turtle.color(item)
    turtle.penup()
    turtle.goto(-200,y)
    y -= 50
    turtle_list.append(turtle)
print(turtle_list)

race_is_on = True
turtle.speed("fast")

while race_is_on:

    for item in turtle_list:
        if item.xcor() < 230:
            random_distance = random.randint(1,15)
            item.forward(random_distance)
            
        else:
            race_is_on = False
            winner = item.color()[0]
            if winner == user_bet.lower():
                print("you won!")
            else:
                print(f"you lost. the winner was {winner}")


screen.exitonclick()