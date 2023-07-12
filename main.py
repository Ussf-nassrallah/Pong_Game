# import turtle module
import turtle

# Setup screen window
wind = turtle.Screen()
wind.title("Ping Pong by Youssef nasrallah")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0) # stops the window from updating automatically

# first paddle
first_paddle = turtle.Turtle()
first_paddle.speed(0)
first_paddle.shape("square")
first_paddle.color("blue")
first_paddle.shapesize(stretch_wid=5, stretch_len=1) # width=20*5 and height=20*1
first_paddle.penup() # stops the object from drawing lines
first_paddle.goto(-350, 0)

# second paddle
second_paddle = turtle.Turtle()
second_paddle.speed(0)
second_paddle.shape("square")
second_paddle.color("red")
second_paddle.shapesize(stretch_wid=5, stretch_len=1) # width=20*5 and height=20*1
second_paddle.penup()
second_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# Score

player_1_score = 0
player_2_score = 0

score = turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 || Player 2: 0", align="center", font=("Hack", 20, "normal"))


# Game functions
def first_paddle_up():
    y = first_paddle.ycor()
    y += 20
    first_paddle.sety(y)


def first_paddle_down():
    y = first_paddle.ycor()
    y -= 20
    first_paddle.sety(y)


def second_paddle_up():
    y = second_paddle.ycor()
    y += 20
    second_paddle.sety(y)


def second_paddle_down():
    y = second_paddle.ycor()
    y -= 20
    second_paddle.sety(y)


# keyboard bindings
wind.listen()

wind.onkeypress(first_paddle_up, 'w')
wind.onkeypress(first_paddle_down, 's')

wind.onkeypress(second_paddle_up, 'Up')
wind.onkeypress(second_paddle_down, 'Down')

# Game loop
while True:
    # updates the screen everytime the loop run
    wind.update()

    # move the ball
    ball.setx(ball.dx + ball.xcor())
    ball.sety(ball.dy + ball.ycor())

    # check border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_1_score += 1
        score.clear()
        score.write("Player 1: {} || Player 2: {}".format(player_1_score, player_2_score), align="center",
                    font=("Hack", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_2_score += 1
        score.clear()
        score.write("Player 1: {} || Player 2: {}".format(player_1_score, player_2_score), align="center",
                    font=("Hack", 20, "normal"))

    if (340 < ball.xcor() < 350) and (second_paddle.ycor() + 40 > ball.ycor() > second_paddle.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (340 < ball.xcor() < 350) and (second_paddle.ycor() + 40 > ball.ycor() > second_paddle.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (first_paddle.ycor() + 40 > ball.ycor() > first_paddle.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1