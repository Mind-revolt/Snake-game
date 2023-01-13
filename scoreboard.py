from turtle import Turtle

# Create constants
ALIGNMENT = "center"
FONT = ("Times", 20, "normal")

class ScoreBoard(Turtle):
    """Is a scoreboard on the screen. Used with Turtle module"""
    def __init__(self):
        super().__init__()
        self.number = 0
        self.hideturtle()
        self.goto(x=0, y=270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.number}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.number += 1
        self.update_scoreboard()
