"This is the working file for drawing equilateral triangles and other shapes"

import turtle
import math
# Create a canvas for drawing
window = turtle.Screen()
window.bgcolor("lightblue")
window.setup(width=0.9, height=0.9, startx=None, starty=None)

Frank = turtle.Turtle()
Frank.color("hotpink")
Frank.pensize(3)


def draw_equilateral_triangle(side_length):
    "this function draws an equilateral triangle with a given side length"
    for number in range(3):
        Frank.left(120)
        Frank.forward(side_length)


def draw_square(side_length):
    "this function draws a square with a given side length"
    for number in range(4):
        Frank.forward(side_length)
        Frank.left(90)


def draw_pentagon_with_star(side_length):
    "this function draws a pentagon with a star inside"
    for number in range(5):
        Frank.forward(side_length)
        Frank.left(72)

    Frank.right(144)
    for number in range(5):
        Frank.forward(side_length*math.cos(54)*2)
        Frank.left(144)


def test_basic():
    "this is the function to test out the shapes we drew so far"
    draw_equilateral_triangle(200)
    Frank.color("yellow")
    draw_equilateral_triangle(100)

    Frank.penup()
    Frank.forward(50)

    Frank.pendown()
    draw_square(200)
    Frank.color("hotpink")
    draw_square(100)

    Frank.penup()
    Frank.forward(50)
    Frank.right(90)
    Frank.forward(300)
    Frank.left(90)
    Frank.pendown()
    draw_pentagon_with_star(100)

    Frank.right(36)
    Frank.penup()
    Frank.forward(270)
    Frank.right(180)
    Frank.pendown()
    Frank.color("yellow")
    draw_pentagon_with_star(100*1.5)


test_basic()

Frank.left(144)
Frank.forward(500)

def draw_composition(shape1_length,shape2_length,shape3_length,moving_distance):
    "this function to draw shape compositions"
    draw_pentagon_with_star(shape1_length)
    Frank.left(144)
    Frank.forward(moving_distance)
    draw_equilateral_triangle(shape2_length)
    Frank.left(90)
    draw_square(shape3_length)

def test_composition():
    "this function to test out draw_composition function"
    draw_composition(50,150,150,100)
    Frank.right(90)
    Frank.forward(50)
    draw_composition(30, 90, 90, 60)

test_composition()

Frank.left(90)
Frank.forward(1000)
Frank.left(180)
Frank.color("forestgreen")

def scene(shape1_length, shape2_length, shape3_length, moving_distance):
    "this function to draw a scene combining all the shapes together with different scales"
    draw_composition(shape1_length, shape2_length,
                     shape3_length, moving_distance)
    Frank.forward(300)
    draw_square(shape1_length)
    draw_equilateral_triangle(shape2_length)
    draw_square(shape3_length)
    draw_pentagon_with_star(shape3_length)
    Frank.left(144)
    Frank.forward(200)
    draw_pentagon_with_star(shape1_length)
    

scene(40,120,120,80)
window.mainloop()
