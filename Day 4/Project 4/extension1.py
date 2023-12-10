""" CS 5001 - Fall 2023 - Project 4 - Wild Turtles - Extension 1

by Kaiqi Zhang
"""

import turtle
import random


def stop_turtle():
    """This function makes turtle stop walking
    """
    global KEEP_WALKING
    KEEP_WALKING = False


def walk_circle():
    """This function makes turtle walk in the shape of a circle
    """
    global walk_shape
    walk_shape = "circle"


def walk_straight():
    """This function makes turtle walk straight
    """
    global walk_shape
    walk_shape = "straight"


def walk_random():
    """This function makes turtle move in a random walk
    """
    global walk_shape
    walk_shape = "random"


def walk_wavy():
    """This function makes turtle move in a wavy walk
    """
    global walk_shape
    walk_shape = "wavy"


def reset():
    """This function reset the turtle's position
    """
    global t, f
    t.reset()
    t.color("hotpink")
    f.reset()
    f.color("blue")
    f.penup()
    f.goto(random.randint(-350, 350), random.randint(-350, 350))
    f.pendown()
    f.setheading(random.randint(0, 359))


def stamp_mode():
    """This function control the stamp mode of the turtle
    """
    global stamp_mode
    if stamp_mode is False:
        stamp_mode = True
    else:
        stamp_mode = False


def click_now(x, y):
    """This function stored the desired heading
    """
    global forced_heading
    forced_heading = t.towards(x, y)


def draw_curve():
    """This function makes turtle draw a curve
    """
    global t
    for i in range(200):
        t.right(1)
        t.forward(1)


def draw_heart():
    """This function makes turtle draw a filled heart.
    """
    global t
    t.fillcolor("red")
    t.begin_fill()
    t.left(140)
    t.forward(110)
    draw_curve()
    t.left(120)
    draw_curve()
    t.forward(110)
    t.end_fill()


def show_txt():
    global t
    t.up()
    t.setpos(-60, 90)
    t.down()
    t.color("blue")
    t.write("Our turtles have fallen in love!", font=("Verdana", 14, "bold"))


window = turtle.Screen()
window.setup(700, 700)
t = turtle.Turtle()
f = turtle.Turtle()
t.color("hotpink")
t.shape("turtle")
f.color("blue")
f.shape("turtle")


f.penup()
f.goto(random.randint(-350, 350), random.randint(-350, 350))
f.pendown()
f.setheading(random.randint(0, 359))
t.forward(random.random())


window.onkey(stop_turtle, "space")
window.onkey(walk_circle, "c")
window.onkey(walk_straight, "s")
window.onkey(walk_random, "r")
window.onkey(walk_wavy, "w")
window.onkey(reset, "=")
window.onkey(stamp_mode, "#")
window.onclick(click_now)

window.listen()

KEEP_WALKING = True
forced_heading = None
walk_shape = "straight"
stamp_mode = False
count = 0

while KEEP_WALKING:
    t.forward(10)
    f.forward(5)

    if walk_shape == "straight":
        t.left(0)
    elif walk_shape == "circle":
        t.left(10)
    elif walk_shape == "random":
        t.left(random.randint(-25, 25))
    elif walk_shape == "wavy":
        t.left(random.randint(-10, 10))

    if t.xcor() > 350 or t.xcor() < -350:
        t.setheading(180.0 - t.heading())
    if t.ycor() > 350 or t.ycor() < -350:
        t.setheading(- t.heading())
    if f.xcor() > 350 or f.xcor() < -350:
        f.setheading(180.0 - f.heading())
    if f.ycor() > 350 or f.ycor() < -350:
        f.setheading(- f.heading())

    if forced_heading is not None:
        t.setheading(forced_heading)

    forced_heading = None

    count += 1
    if count % 15 == 0 and stamp_mode is True:
        t.stamp()

    if t.distance(f) < 15:
        reset()
        draw_heart()
        show_txt()


window.mainloop()
