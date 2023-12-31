
import turtle

#screen set up
wind = turtle.Screen()
wind.title("ping pong by spouki")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)
#game objects

    #madrabe1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.penup()
madrab1.goto(-350,0)
madrab1.shapesize(stretch_wid=5,stretch_len=1)

    #madrabe2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.penup()
madrab2.goto(350,0)
madrab2.shapesize(stretch_wid=5,stretch_len=1)

    #ball
ball = turtle.Turtle()
ball.speed(10)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.15
ball.dy = -0.15

    #score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player 1: 0 player 2: 0 ",align="center", font=("Courier",24,"normal"))




#functions
def madrab1_up():
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)

def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)    

#keyboard 
wind.listen()
wind.onkeypress(madrab1_up, "z")
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")


#game loop
while True:
    wind.update()

    #move ball
    ball.setx( ball.xcor() + ball.dx)
    ball.sety( ball.ycor() + ball.dy)

    #border check

    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1 

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("player 1: {} player 2: {} ".format(score1,score2) ,align="center", font=("Courier",24,"normal"))    

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("player 1: {} player 2: {} ".format(score1,score2) ,align="center", font=("Courier",24,"normal"))  

    #ball trick (tsadom)
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()< madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() ):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor()< -340 and ball.xcor()> -350) and (ball.ycor()< madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() ):
        ball.setx(-340)
        ball.dx *= -1


             

