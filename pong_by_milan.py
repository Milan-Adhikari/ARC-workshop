import turtle
import time

delay = 0.5
#screen
win = turtle.Screen()
win.title("Pong By Milan")
win.setup(height=600,width=500)
win.tracer(0)
win.bgcolor("white")

#paddle_a
a = turtle.Turtle()
a.shape("square")
a.penup()
a.speed(0)
a.shapesize(stretch_wid=5,stretch_len=1)
a.color("black")
a.goto(-235,0)

#paddle_b
b = turtle.Turtle()
b.shape("square")
b.penup()
b.speed(8)
b.shapesize(stretch_wid=5,stretch_len=1)
b.color("black")
b.goto(+230,0)

#ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("black")
ball.speed(0)
ball.penup()
ball.goto(0,0)
ball.dy = 0.2
ball.dx = 0.2
move = 1

#score
score_a = 0
score_b = 0
score = turtle.Turtle()
score.penup()
score.hideturtle()
score.speed(0)
score.goto(0,270)
score.write("Score A: {}     Score B: {}".format(score_a,score_b),align="center",font=("arial",15))

#end
end = turtle.Turtle()
end.hideturtle()
end.speed(0)
end.penup()
end.goto(0,-270)
end.write("Press 'e' to End Game", align="center",font=("arial",10))

#functions
def a_up():
    y = a.ycor()
    a.sety(y+35)
def a_down():
    y = a.ycor()
    a.sety(y-35)
def b_up():
    y = b.ycor()
    b.sety(y+35)
def b_down():
    y = b.ycor()
    b.sety(y-35)
def ball_move():
    global move
    move += 1

win.listen()
win.onkeypress(a_up,"w")
win.onkeypress(a_down,"s")
win.onkeypress(b_up,"Up")
win.onkeypress(b_down,"Down")
win.onkeypress(ball_move,"e")

def movement():
            ball.sety(ball.ycor()+ball.dy)
            ball.setx(ball.xcor()+ball.dx)


#main loop
while move == 1:
    win.update()

    movement()

    #boundary
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor()>240:
        ball.goto(0,0)
        time.sleep(delay)
        score_a += 10
        score.clear()
        score.write("Score A: {}     Score B: {}".format(score_a, score_b), align="center", font=("arial", 15))
    if ball.xcor()<-240:
        ball.goto(0,0)
        time.sleep(delay)
        score_b += 10
        score.clear()
        score.write("Score A: {}     Score B: {}".format(score_a, score_b), align="center", font=("arial", 15))
    if ball.xcor() > 220 and ( ball.ycor() < b.ycor()+50 and ball.ycor()> b.ycor()-50):
        ball.setx(220)
        ball.dx *= -1
    if ball.xcor() < -220 and ( ball.ycor() < a.ycor()+50 and ball.ycor()> a.ycor()-50):
        ball.setx(-220)
        ball.dx *= -1



