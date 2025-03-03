from turtle import Turtle

class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto((290,290))
        self.pendown()
        self.color("red")
        self.goto(290,-290)
        self.goto(-290,-290)
        self.goto(-290,290)
        self.goto(290,290)
        pass

