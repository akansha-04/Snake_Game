from turtle import Turtle
Alignment="center"
Font=('Arial', 24, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.goto(0, 265)
        self.hideturtle()  # To hide the turtle formed by score
        self.update_score()
    def update_score(self):
        self.write(f"Score: {self.score}", align=Alignment, font=Font)
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game is over", align=Alignment, font=Font)

    def game_score(self):
        self.score+=1
        self.clear()
        self.update_score()



