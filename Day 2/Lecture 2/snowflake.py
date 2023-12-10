"Snowflakes for Project 2"

import turtle
import random


def move_to(to_x, to_y):
    "move to"
    steve.penup()
    steve.goto(to_x, to_y)
    steve.pendown()


def draw_box(x_left, y_bottom, x_width, y_height):
    "draw box"
    move_to(x_left, y_bottom)
    steve.forward(x_width)
    steve.left(90)
    steve.forward(y_height)
    steve.left(90)
    steve.forward(x_width)
    steve.left(90)
    steve.forward(y_height)
    steve.left(90)


def draw_snowflake(center_x, center_y, snowflake_size, snowflake_color):
    "draw snowflake"
    move_to(center_x, center_y)
    steve.color(snowflake_color)
    for _spoke_number in range(6):
        steve.forward(snowflake_size)
        steve.backward(snowflake_size)
        steve.left(60)


my_bool = True
window = turtle.Screen()
steve = turtle.Turtle()
steve.speed(0)

draw_box(-200, -200, 400, 400)
draw_box(-75, -75, 150, 150)
for snowflake_number in range(20):
    random_x = random.randrange(400)-200
    random_y = random.randrange(400)-200
    random_size = random.randrange(15)+10
    if (random_x > -75 and random_x < 75 and random_y > -75 and random_y < 75):
        draw_snowflake(random_x, random_y, random_size, "red")
    else:
        draw_snowflake(random_x, random_y, random_size, "green")

window.mainloop()
