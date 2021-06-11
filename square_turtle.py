import turtle
#variables
WIDTH = 600
HEIGHT = 500
# window
windows = turtle.Screen()
windows.setup(WIDTH,HEIGHT)
# object
object = turtle.Turtle()
object.speed(3)
object.goto(0,0)
object.color('red','cyan')
object.begin_fill()
for i in range(4):
    object.left(90)
    object.forward(100)
object.end_fill()

turtle.done()