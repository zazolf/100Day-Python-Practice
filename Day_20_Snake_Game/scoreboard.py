from turtle import Turtle
from snake import Snake



class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        with open(".\Day_20_Snake_Game\data.txt") as data:
            self.high_score = int(data.read())
        self.write(f"score = {self.score}", align = "center", font = ("Arial", 20, "normal"))
        self.hideturtle()
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score = {self.score} High score = {self.high_score}", align = "center", font = ("Arial", 20, "normal"))

         
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open (".\Day_20_Snake_Game\data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    
    def game_over(self):
       self.goto(0,0)
       self.reset_score()
       #self.write(f"Game Over", align = "center", font = ("Arial", 20, "normal"))
    


