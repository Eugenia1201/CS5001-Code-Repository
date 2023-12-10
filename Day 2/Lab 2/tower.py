"CS 5001_Day 2_Kaiqi Zhang"

import turtle
import random

# main program
window = turtle.Screen()
frank = turtle.Turtle()


def move_to(to_x, to_y):
    "this function moves turtle to a specific location"
    frank.penup()
    frank.goto(to_x, to_y)
    frank.pendown()


def draw_box(x_left, y_bottom, x_width, y_height):
    "this function draws a box with indicated size"
    move_to(x_left, y_bottom)
    for number in range(2):
        frank.forward(x_width)
        frank.left(90)
        frank.forward(y_height)
        frank.left(90)


def draw_tower(x_left, y_bottom, x_width, y_height):
    draw_box(x_left, y_bottom, x_width, y_height)
    draw_box(x_left+(x_width/4), y_bottom+y_height, x_width/2, y_height/2)
    draw_box(x_left + ((3/8) * x_width), y_bottom+((3/2)*y_height),
             x_width/4, y_height/4)


def draw_gafoo():
    for number in range(random.randrange(4)+2):
        draw_tower(random.randrange(500)-300,
                   random.randrange(600) - 200,
                   random.randrange(100)+50,
                   random.randrange(100)+50)
# turtle drawing
# draw_box(0, 0, 100, 150
# draw_box(-200, -150, 50, 100)
# draw_tower(0, 0, 100, 150)
# draw_tower(-100,-100, 50,100)


draw_gafoo()
window.mainloop()
