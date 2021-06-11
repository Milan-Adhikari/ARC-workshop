import turtle
import math
import random

windows = turtle.Screen()
windows.tracer(1)
color = ['red','green','purple','yellow','orange','blue']
star = turtle.Turtle()
star.speed(0)

for i in range(50):
    star.color(random.choice(color))
    star.circle(50)
    star.rt(5)

turtle.done()