import turtle
import math

win= turtle.Screen()
win.bgcolor("#FF0033")


bob = turtle.Turtle()
bob.color("black","")
bob.speed(0)

def star(a,b):
    if b<=10:
        return
    else:
        for i in range(5):

            a.forward(b)
            star(bob,b/3)
            a.left(216)

star(bob,300)

turtle.done()

