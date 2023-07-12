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
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)


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
    wind.update() # updates the screen everytime the loop run