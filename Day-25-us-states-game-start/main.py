import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")
image = "./Day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
# def get_mouse_click_coord(x,y):
#     print(x,y)
    
# turtle.onscreenclick(get_mouse_click_coord)
# turtle.mainloop()
guessed_states=[]
while len(guessed_states) <50:
    answer = screen.textinput(title="Guess the State", prompt=" what's the next state?")
    data = pandas.read_csv("./Day-25-us-states-game-start/50_states.csv")
   
    user_answer = answer.title()
    if user_answer in data["state"].values:
        guessed_states.append(user_answer)
        x_value = int(data[data["state"]== user_answer].x)
        y_value = int(data[data["state"]== user_answer].y)
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(x_value, y_value)
        writer.pendown()
        writer.write(user_answer, align="center", font=("Arial", 8, "normal"))
    
    elif user_answer.title() == "Exit":
        missing_states = []
        for state in data["state"].to_list():
            if state not in guessed_states:
                missing_states.append(state)
        break

df = pandas.DataFrame(missing_states)
df.to_csv("./Day-25-us-states-game-start/missed_states.csv")

#screen.exitonclick()

