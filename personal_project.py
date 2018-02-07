import turtle
import random
import math
import time
from ball import Ball



###############################################

def __init__(self, states = 2):
    self.window = turtle.Screen()
    #self.window.screensize(1920,1080)
    self.turtles = []
    self.window = turtle.Screen()
    self.window.screensize(sizex, sizey)
    self.window.setup(width=1.0, height=1.0, startx=None, starty=None)




###############################################
#new_ball = Ball(4,4,40,40,40,'blue')
turtle.tracer(0)
turtle.hideturtle()
SCREEN_WIDTH= int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT= int(turtle.getcanvas().winfo_width()/2)
##
score = turtle.Turtle()
score.hideturtle()
score.pu()
score.goto(-650,300)
ts = turtle.getscreen()
ts.bgpic("lol123.gif")

RUNNING = True
SLEEP = 0.06
turtle.register_shape("pac_man.gif")
MY_BALL = Ball(-650,300,0,0,190,"black","circle")

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
BALLS= []

for i in range (NUMBER_OF_BALLS):
    x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS , SCREEN_WIDTH -MAXIMUM_BALL_RADIUS)

    y=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT -MAXIMUM_BALL_RADIUS)

    dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)

    dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

    while dx == 0 or dy == 0:
        dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
        dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

    r=random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)

    color=(random.random(),random.random(),random.random())

    ball=Ball(x,y,dx,dy,r,color,"circle")
    BALLS.append(ball)

def move_all_balls():
    for value in BALLS:
        value.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    ######################

def collide(ball_a,ball_b):
    D = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(), 2) + math.pow(ball_a.ycor()-ball_b.ycor(),2))
    sum_r = ball_a.r+ball_b.r
    if ball_a == ball_b:
        return False
    if(D+10<=sum_r):
        return True
    return False
##########################NOTE>
##
##########################NOTE2


def checks_all_balls_collision():
    for ball_a in BALLS:
        for ball_b in BALLS:
            if(collide(ball_a, ball_b)):
                # We have a collision. Get random attribs
                x_cor=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS , SCREEN_WIDTH -MAXIMUM_BALL_RADIUS)

                y_cor=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT -MAXIMUM_BALL_RADIUS)

                new_r=random.randint(MINIMUM_BALL_RADIUS  , MAXIMUM_BALL_RADIUS)

                new_color=(random.random(),random.random(),random.random())
                dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
                while(dy==0):
                   dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
                while(dx==0):
                   dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)

                if(ball_a.r>ball_b.r):
                    ball_a.r+=1
                    ball_a.shapesize(ball_a.r/10)

                    ball_b.goto(x_cor, y_cor)
                    ball_b.dx=dx
                    ball_b.dy=dy
                    ball_b.color(new_color)
                    ball_b.r = new_r
                    ball_b.shapesize(new_r/10)

                else:
                    ball_b.r+=1
                    ball_b.shapesize(ball_b.r/10)

                    ball_a.goto(x_cor, y_cor)
                    ball_a.dx=dx
                    ball_a.dy=dy
                    ball_a.color(new_color)
                    ball_a.r = new_r
                    ball_a.shapesize(new_r/10)



def check_myball_collision():
    for ball in BALLS:
        if collide(MY_BALL,ball)==True:
            print("Collision: "+str(collide(MY_BALL, ball)))
            my_r=MY_BALL.r
            ur_r=ball.r 
            
            X=random.randint(round(-SCREEN_WIDTH)+MAXIMUM_BALL_RADIUS, round(SCREEN_WIDTH) - MAXIMUM_BALL_RADIUS)
            Y=random.randint(round(-SCREEN_HEIGHT)+MAXIMUM_BALL_RADIUS,round(SCREEN_HEIGHT) - MAXIMUM_BALL_RADIUS) 

            dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
            while(dx==0):
                dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)

            dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
            while(dy==0):
                dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)

            Radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
            
            new_color=(random.random(), random.random(), random.random())

            if(MY_BALL.r<ball.r):
                print("MY ball: "+ str(MY_BALL.r))
                print("Other: "+str(ball.r))
                return False
            else:
                score.clear()
                score.write("your radius is:"+str(MY_BALL.r),font=("Arial",20,"normal"))
                if (MY_BALL.r<=200-1):
                    MY_BALL.r+=1
                    MY_BALL.shapesize(MY_BALL.r/10)

                if (MY_BALL.r >=200):
                    score.clear()
                    score.write("YOU HAVE REACHED MAXIMUMM POWERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",font=("Arial",20,"normal"))

                ball.goto(X,Y)
                ball.dx=dx
                ball.dy=dy
                ball.color(new_color)
                ball.r = Radius
                ball.shapesize(Radius/10)


    return True

def movearound(event):
    X= event.x - SCREEN_WIDTH
    Y= SCREEN_HEIGHT - event.y
    MY_BALL.goto(X,Y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.getscreen().listen()


while RUNNING==True:
    if SCREEN_WIDTH!=turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT!=turtle.getcanvas().winfo_height()/2:
        SCREEN_WIDTH=int(turtle.getcanvas().winfo_width()/2) 
        SCREEN_HEIGHT=int(turtle.getcanvas().winfo_height()/2)
    move_all_balls()


    checks_all_balls_collision()

    MY_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)

    RUNNING=check_myball_collision()

    turtle.getscreen().update()

    time.sleep(SLEEP)

    # print(RUNNING)

turtle.mainloop()
