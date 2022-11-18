from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,right_paddle=True):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=4,stretch_len=1)
        self.color('red')
        self.penup()
        self.right_paddle = right_paddle
        self.create_paddle()

    def create_paddle(self):
        if self.right_paddle:
            self.goto(350,0)
        else:
            self.goto(-350,0)

    def up(self):
        self.goto(self.xcor(),self.ycor()+20)

    def down(self):
        self.goto(self.xcor(),self.ycor()-20)


