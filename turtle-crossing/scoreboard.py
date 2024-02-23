from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-240, 270)
        self.level_up()

    def level_up(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
