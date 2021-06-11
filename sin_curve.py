import turtle
import math

window = turtle.Screen()

obj = turtle.Turtle()

for i in range(360):
    obj.goto(i,math.sin(math.radians(i))*100)

turtle.done()