##########################################1

##from turtle import *
##
##class Square (Turtle):
##    def __init__(self,size):
##        Turtle.__init__(self)
##
##        self.shapesize(size)
##        self.shape("square")
##        
##S1= Square(10)

##########################################2

##from turtle import *
##
##class Hexagon(Turtle):
##    def __init__(self
import turtle
s=turtle.Screen()
p=turtle.Turtle()

def happymouth(p,x,y):
    p.setheading(-60)
    jump(p,x-60.62,y+65)
    p.circle(70,120)

def eyes(p,x,y):
    jump(p,x+35,y+120)
    p.dot(25)
    jump(p,x-35,y+120)
    p.dot(25)

def jump(p,x,y):
    p.up()
    p.goto(x,y)
    p.down()


def emoticon(p,x,y):
    p=turtle.Turtle()
    s=turtle.Screen()
    p.pensize(3)
    p.setheading(0)
    jump(p,x,y)
    p.circle(100)
    eyes(p,x,y)
    happymouth(p,x,y)
    jump(p,x,y)
