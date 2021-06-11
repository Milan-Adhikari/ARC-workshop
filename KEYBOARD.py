import turtle
import winsound

windows = turtle.Screen()

obj = turtle.Turtle()
obj.shape('turtle')
obj.left(90)

def up():
    winsound.PlaySound('pong.wav',winsound.SND_ASYNC)
    y = obj.ycor()
    obj.sety(y+2)

windows.listen()
windows.onkeypress(up,'Up')
turtle.done()