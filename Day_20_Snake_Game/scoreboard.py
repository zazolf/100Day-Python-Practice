from turtle import Turtle
from snake import Snake



class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.write(f"score = {self.score}", align = "center", font = ("Arial", 20, "normal"))
        self.hideturtle()
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"score = {self.score}", align = "center", font = ("Arial", 20, "normal"))
        
    def game_over(self):
       self.goto(0,0)
       self.write(f"Game Over", align = "center", font = ("Arial", 20, "normal"))
    


