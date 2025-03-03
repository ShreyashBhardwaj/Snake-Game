from turtle import Turtle
import random

class BigFood(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color("Red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x=random.randint(a=-280,b=280)
        random_y=random.randint(a=-280,b=280)
        self.goto(random_x,random_y)
