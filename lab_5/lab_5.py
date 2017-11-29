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

from turtle import *

class Hexagon (Turtle):
    def __init__(self,size,speed,color):
        Turtle.__init__(self)
        self.speed(speed)
        self.color(color)
        self.shapesize(size)
        self.begin_poly()
        for i in range(6):
            self.pu()
            self.rt(60)
            self.fd(100)
        self.end_poly()
        p =self.get_poly()
        register_shape("hexagon",p)
        self.shape("hexagon")
H1= Hexagon(1,10,"red")
H1.fd(200)



