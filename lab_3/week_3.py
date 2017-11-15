import turtle

##turtle.forward(100)
##turtle.right(150)
##turtle.forward(100)
##turtle.right(140)
##turtle.forward(100)
##turtle.right(150)
##turtle.forward(100)
##turtle.right(140)
##turtle.forward(90)

############################2

##turtle.left(90)
##turtle.register_shape('dayum',((0,0),(0,50),(50,50),(50,0),(25,-50),(0,0)))
##turtle.shape('dayum')

############################3

turtle.register_shape('clinton2.gif')
turtle.shape('clinton2.gif')
turtle.tracer(1,0)
for I in range (300):
    turtle.pendown()
    turtle.forward(200)
    turtle.right(65)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(70)
    turtle.penup()
    turtle.goto(0,0)
    turtle.right(2)
turtle.goto(200,200)
turtle.write("hillary clinton")
