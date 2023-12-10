import turtle

# Create a canvas for drawing
window = turtle.Screen()
window.bgcolor("lightblue")
window.setup(width=0.5, height=0.75, startx=None, starty=None)

Lisa = turtle.Turtle()
Lisa.color("orange")
Lisa.pensize(3)
Lisa.speed(50)
# draw a circle
# Lisa.circle(80)
# Lisa.right(90)

# draw petals


# def draw_one_petal(length, degree):
#     for number in range(55):
#         Lisa.forward(length)
#         Lisa.left(degree)


# draw_one_petal(2, 4)


# def draw_many_petals(f):
#     for number in range(f):
#         Lisa.right(180)
#         draw_one_petal(2, 4)


# draw_many_petals(8)

# Lisa.right(180)
# Lisa.color("lightgreen")
# Lisa.forward(200)
# Lisa.left(70)
# Draw a leaf


def draw_half_leaf(length, degree):
    for number in range(30):
        Lisa.forward(length)
        Lisa.left(degree)


# draw_half_leaf(3, 3)
# Lisa.left(90)
# draw_half_leaf(3, 3)
# Lisa.right(75)
# draw_half_leaf(3, 3)
# Lisa.left(90)
# draw_half_leaf(3, 3)
# Lisa.right(85)
# Lisa.forward(100)

window.mainloop()
