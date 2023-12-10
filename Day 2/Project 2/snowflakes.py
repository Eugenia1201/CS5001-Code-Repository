"This is the working file to draw a snow flake."
import turtle
import random

window = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
how_many_inside = 0
counter_total = 0
counter_outside = 0


def move_to(to_x, to_y):
    "this function moves turtle to a specific location"
    t.penup()
    t.goto(to_x, to_y)
    t.pendown()


def draw_snowflake(center_x, center_y, snowflake_size, snowflake_color, snowflake_angle):
    "this function draws a snowflake with indicated starting location, size and color"
    t.setheading(snowflake_angle)
    t.color(snowflake_color)
    move_to(center_x,center_y)

    for n in range(6):
        t.forward(snowflake_size)
        t.backward(snowflake_size)
        t.left(60)


def draw_box(x_left, y_bottom, x_width, y_height):
    "this function draws a box with indicated size"
    move_to(x_left, y_bottom)
    for number in range(2):
        t.forward(x_width)
        t.left(90)
        t.forward(y_height)
        t.left(90)


# draw_snowflake(100,100, 50, "red")
draw_box(-200,-200,400,400)
draw_box(-75,-75,150,150)


while how_many_inside <3:
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    angle = random.randrange(360)
    size = random.randint(10,15)
    if ((-75<x<75) & (-75<y<75)):
        draw_snowflake(x, y, size, "red", 0) if counter_total % 2 == 0 else draw_snowflake(x,y,size, "red",angle) 
        how_many_inside += 1
        counter_total +=1
    elif(counter_outside %3 ==0):
        draw_snowflake(x, y, size, "blue", 0) if counter_total % 2 == 0 else draw_snowflake(
            x, y, size, "blue", angle)
        counter_outside += 1
        counter_total += 1
    else: 
        draw_snowflake(x, y, size, "green", 0) if counter_total % 2 == 0 else draw_snowflake(
            x, y, size, "green", angle)
        counter_outside += 1
        counter_total += 1


window.mainloop()
