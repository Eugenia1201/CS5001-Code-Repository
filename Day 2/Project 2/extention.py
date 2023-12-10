"This is the working file for snowflake extension."
import turtle
import random

window = turtle.Screen()
snow = turtle.Turtle()
snow.speed(0)



def move_to(to_x, to_y):
    "this function moves turtle to a specific location"
    snow.penup()
    snow.goto(to_x, to_y)
    snow.pendown()


def draw_snowflake(center_x, center_y, snowflake_size1, snowflake_size2, snowflake_color, snowflake_angle):
    "this function draws a snowflake with indicated starting location, size and color"
    snow.setheading(snowflake_angle)
    snow.color(snowflake_color)
    move_to(center_x, center_y)

    for n in range(5):
        snow.forward(snowflake_size1)
        snow.backward(snowflake_size1)
        snow.left(36)
        snow.forward(snowflake_size2)
        snow.backward(snowflake_size2)
        snow.left(36)


def draw_fancy_snowflake(center_x, center_y, snowflake_size1, snowflake_size2, snowflake_color):
    "this function draws a fancier snowflake with small lines coming out of the main lines"
    snow.color(snowflake_color)
    move_to(center_x, center_y)

    for n in range(10):
        snow.forward(snowflake_size1)
        snow.left(36)
        snow.forward(snowflake_size2)
        snow.backward(snowflake_size2)
        snow.right(72)
        snow.forward(snowflake_size2)
        snow.backward(snowflake_size2)
        snow.left(36)
        snow.backward(snowflake_size1)
        snow.left(36)


for n in range(5):
    draw_snowflake(random.randrange(200)-250, random.randrange(200)-250, 30, 25, "pink", random.randrange(60))
for n in range(10):
    draw_snowflake(random.randrange(200), random.randrange(200), 20, 15, "purple", random.randrange(30))
for n in range(3):
    draw_fancy_snowflake(random.randint(0,300), random.randint(-200,0), 50, 10, "skyblue")
    
snow.hideturtle()
window.mainloop()
