"this is the working file for project1_shape2"
import turtle
scale = 1.5


# Create a canvas for drawing
window = turtle.Screen()
window.bgcolor("lightblue")
window.setup(width=0.5, height=0.75, startx=None, starty=None)

Lisa = turtle.Turtle()
Lisa.color("orange")
Lisa.pensize(3)
Lisa.speed(100)
# draw a circle
Lisa.circle(80*scale)
Lisa.right(90)



# draw petals

def draw_one_petal(length, degree):
    "the function to draw one petal-like shape"
    for number in range(55):
        Lisa.forward(length)
        Lisa.left(degree)


draw_one_petal(2*scale, 4)


def draw_many_petals(f):
    "the function to draw many petal-like shapes while adjusting orientation"
    for number in range(f):
        Lisa.right(180)
        draw_one_petal(2*scale, 4)


draw_many_petals(8)

Lisa.right(180)
Lisa.color("lightgreen")
Lisa.forward(200*scale)
Lisa.left(70)

# Draw half leaf


def draw_half_leaf(length, degree):
    "the function to draw an curve, which resembles a half of a leaf in this case"
    for number in range(30):
        Lisa.forward(length)
        Lisa.left(degree)


draw_half_leaf(3*scale, 3)
Lisa.left(90)
draw_half_leaf(3*scale, 3)
Lisa.right(135)
draw_half_leaf(3*scale, 3)
Lisa.left(90)
draw_half_leaf(3*scale, 3)
Lisa.right(115)
Lisa.forward(50*scale)

window.mainloop()
