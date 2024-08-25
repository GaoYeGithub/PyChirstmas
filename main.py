import turtle
from random import randint

def box(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
    turtle.setheading(0)

def star(turtle, color, x, y, size):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
        turtle.forward(size)
    turtle.end_fill()
    turtle.setheading(0)

def balls(turtle, color, x, y, radius):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.setheading(0)

def snowflake(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color("white")
    turtle.pendown()
    for _ in range(8):
        turtle.forward(10)
        turtle.backward(10)
        turtle.right(45)

def snowman(turtle, x, y):
  turtle.penup()
  turtle.goto(x, y)
  turtle.color("white")
  turtle.fillcolor("white")
  turtle.pendown()
  for radius in [20, 15, 10]:
      turtle.begin_fill()
      turtle.circle(radius)
      turtle.end_fill()
      turtle.penup()
      turtle.goto(turtle.xcor(), turtle.ycor() + radius * 2)
      turtle.pendown()
  turtle.penup()
  turtle.goto(x - 5, y + 35)
  turtle.dot(3, "black")
  turtle.goto(x + 5, y + 35)
  turtle.dot(3, "black")
  turtle.goto(x, y + 15)
  turtle.dot(3, "black")
  turtle.goto(x, y + 5)
  turtle.dot(3, "black")

def draw_christmas_card():
    screen = turtle.Screen()
    screen.bgcolor("#99004D")

    t = turtle.Turtle()
    t.speed(0)

    box(t, "#4F4553", -15, -140, 30, 40)

    y = -100
    width = 240
    while width > 20:
        width -= 20
        height = randint(20, 30)
        x = 0 - width / 2
        box(t, "#05A167", x, y, width, height)
        balls(t, "#fc045b", x, y, 5)
        balls(t, "#fc045b", -x, y, 5)
        y += height

    star(t, "#e5f614", 0.4, y, 20)
    box(t, "#FFD700", -50, -180, 30, 30)
    box(t, "#FF4500", 20, -180, 30, 30)
    for _ in range(20):
        snowflake(t, randint(-300, 300), randint(-200, 200))
    snowman(t, -200, -150)
    snowman(t, 150, -150)
    t.penup()
    t.color("#ff59ac")
    t.goto(-350, -250)
    t.write("Merry Christmas !!!", font=("Calibri", 50, "bold"))

    t.hideturtle()
    turtle.done()

draw_christmas_card()