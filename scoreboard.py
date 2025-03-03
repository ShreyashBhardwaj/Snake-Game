from turtle import Turtle

ALIGNMENT='center'
FONT=("Courier",12,"normal")

FONT_OVER= ("Courier",24,"bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(290)
        self.write(f"Score: {self.current_score}",False,ALIGNMENT,FONT)

    def update(self,normal=False):
        self.clear()
        if normal:
            self.current_score+=10
        else:
            self.current_score+=1
        self.write(f"Score: {self.current_score}",False,ALIGNMENT,FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT,font=FONT_OVER)