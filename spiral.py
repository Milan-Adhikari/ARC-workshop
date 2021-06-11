import turtle
import random
window = turtle.Screen()
obj = turtle.Turtle()
obj.speed(0)
obj.hideturtle()
obj.width(1.1)
def square():
    obj.forward(200)
    obj.left(90)
    obj.forward(200)
    obj.left(90)
    obj.forward(200)
    obj.left(90)
    obj.forward(200)
    obj.left(90)
for i in range(150):
    square()
    obj.rt(4)
turtle.done()