import random
import turtle
import math

window = turtle.Screen()
color = ['red','green','purple','yellow','orange','blue']
obj = turtle.Turtle()
obj.speed(0)
obj.hideturtle()
a=0
b=0
obj.penup()
obj.goto(0,-200)
obj.pendown()
for i in range(200):
    if (obj.xcor()>220 or obj.ycor()>220 or obj.xcor()<-220 or obj.ycor()<-220):
        obj.color(random.choice(color))
    else:
        obj.color('black')
    obj.forward(a)
    obj.left(b)
    a += 3
    b+=1

turtle.done()