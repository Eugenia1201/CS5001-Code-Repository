"""
    CS5001_Kaiqi Zhang_Lab4_Oct042023
"""

import turtle


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


window = turtle.Screen()
window.setup(700, 700)
t = turtle.Turtle()

window.onkey(stop_turtle, "space")
window.onkey(walk_circle, "c")
window.onkey(walk_straight, "s")
window.listen()

KEEP_WALKING = True
walk_shape = "straight"

while KEEP_WALKING:
    t.forward(10)

    if t.xcor() > 350 or t.xcor() < -350 or t.ycor() > 350 or t.ycor() < -350:
        t.reset()
    if walk_shape == "straight":
        t.left(0)
    if walk_shape == "circle":
        t.left(10)

window.mainloop()
