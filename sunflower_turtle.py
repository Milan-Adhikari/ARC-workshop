import turtle

bob = turtle.Turtle()
bob.color("#FF0000","#FFFF00")
bob.speed(100)
bob.begin_fill()
for i in range(40):
    bob.forward(150)
    bob.left(170)
    bob.forward(150)
bob.end_fill()

turtle.done()

