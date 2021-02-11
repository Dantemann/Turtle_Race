import turtle
import random

screen = turtle.Screen()
screen.title('Turtle Race')
screen.bgcolor('blue')

# Map
pointer = turtle.Turtle()
pointer.speed(10)
pointer.penup()
pointer.goto(250,100)
pointer.pendown()
pointer.pensize(2)
pointer.circle(50)
pointer.penup()
pointer.goto(250,-100)
pointer.pendown()
pointer.circle(50)
pointer.hideturtle()


# Turtles
turtle_1 = turtle.Turtle()
turtle_1.color('white', 'orange')
turtle_1.shape('turtle')
turtle_1.shapesize(2,1,1)
turtle_1.penup()
turtle_1.goto(-300,150)
turtle_1.pendown()

turtle_2 = turtle.Turtle()
turtle_2.color('white', 'yellow')
turtle_2.shape('turtle')
turtle_2.shapesize(2,1,1)
turtle_2.penup()
turtle_2.goto(-300,-50)
turtle_2.pendown()

# Race
while True:
    turtle_1.forward(random.randrange(0, 15))
    turtle_2.forward(random.randrange(0, 15))
    if turtle_1.pos()[0] >= 200:
        print("Turtle 1 win")
        break
    elif turtle_2.pos()[0] >= 200:
        print("Turtle 2 win")
        break




turtle.done()