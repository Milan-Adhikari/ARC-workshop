import turtle

window = turtle.Screen()

obj = turtle.Turtle()
obj.left(90)
obj.penup()

def movement():
    obj.sety(obj.ycor()+4)
    obj.setx(obj.xcor()+3)

while True:
    movement()

turtle.done()