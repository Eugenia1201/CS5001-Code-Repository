"this is the working file for project1_shape1"

import turtle
# Create a canvas for drawing
window = turtle.Screen()
window.bgcolor("lightblue")
window.setup(width=0.5, height=0.75, startx=None, starty=None)

Jenny = turtle.Turtle()
Jenny.color("hotpink")
Jenny.pensize(3)


def draw_square(side_length):
    "this function is to draw a square"
    for number in range(4):
        Jenny.backward(side_length)
        Jenny.left(90)


def draw_equilateral_triangle(side_length):
    "this function is to draw an equilateral triangle"
    for number in range(2):
        Jenny.left(120)
        Jenny.forward(side_length)


draw_square(200)
draw_equilateral_triangle(200)

# Move the pen to upper-left corner to draw a window

Jenny.penup()
Jenny.left(120)
Jenny.forward(70)
Jenny.right(90)
Jenny.forward(70)
Jenny.pendown()

draw_square(50)

# draw window frame

def draw_windowframe(degree, length1, length2):
    "this function is to draw window frames"
    Jenny.right(degree)
    Jenny.forward(length1)
    Jenny.right(degree)
    Jenny.forward(length2)


draw_windowframe(90, 25, 50)
Jenny.right(90)
Jenny.forward(25)
draw_windowframe(90, 25, 50)

# Move the pen to bottom-right corner
Jenny.penup()
Jenny.forward(20)
Jenny.left(90)
Jenny.forward(155)
Jenny.left(90)
Jenny.forward(130)

# Draw a door
Jenny.pendown()
Jenny.left(90)
Jenny.forward(80)
Jenny.right(90)
Jenny.forward(30)
Jenny.right(90)
Jenny.forward(80)

window.mainloop()
