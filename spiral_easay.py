import turtle
import math

window = turtle.Screen()

obj = turtle.Turtle()
obj.speed(0)

for i in range(500):
    obj.forward(i)
    obj.rt(91)

turtle.done()