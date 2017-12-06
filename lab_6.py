from turtle import *
import random
import math
class Ball(Turtle):
    def __init__(self,radius,color,speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)

ball_1= Ball (50,"blue",1)
ball_1.pu()
ball_1.fd(200)
ball_2= Ball (20,"red",2)
ball_2.pu()

def check_collision(ball_1,ball_2):
    D=math.sqrt(math.pow(ball_1.xcor(),2)-math.pow(ball_2.xcor(),2)+math.pow(ball_1.ycor(),2)-math.pow(ball_2.ycor(),2))
    a=ball_1.radius+ball_2.radius
    if a<D:
        print("no collision")
    else :
        print("boop")
check_collision(ball_1,ball_2)
