"This is the working file for drawing a smiley sunflower"
import turtle

# Create a turtle screen and a turtle
window = turtle.Screen()
window.bgcolor("cornsilk")
Jay = turtle.Turtle()
Jay.pencolor("pink")
Jay.pensize(5)
Jay.speed(50)
scale = 1


# Function to draw a circle
Jay.circle(80*scale)
Jay.right(90)

# Function to draw a patal

def draw_petal(length, degree):
    "the function to draw one petal-like shape"
    for number in range(55):
        Jay.forward(length)
        Jay.left(degree)


draw_petal(2*scale, 4)

def draw_petals(count):
    "the function to draw many petal-like shapes while adjusting orientation"
    for number in range(count):
        Jay.right(180)
        draw_petal(2*scale, 4)

draw_petals(8)

Jay.right(180)
Jay.color("lightgreen")
Jay.forward(200*scale)
Jay.left(70)

# Function to draw a half leaf

def draw_half_leaf(length, degree):
    "the function to draw an curve, which resembles a half of a leaf in this case"

    for number in range(30):
        Jay.forward(length)
        Jay.left(degree)

# draw two leaves in full shape
draw_half_leaf(3*scale, 3)
Jay.left(90)
draw_half_leaf(3*scale, 3)
Jay.right(135)
draw_half_leaf(3*scale, 3)
Jay.left(90)
draw_half_leaf(3*scale, 3)
Jay.right(115)
Jay.forward(50*scale)

#move the pen up to draw smiley face
Jay.penup()
Jay.left(180)
Jay.forward(350)
Jay.left(90)
Jay.forward(45)
Jay.right(120)
Jay.pendown()
Jay.pencolor("skyblue")
Jay.pensize(2)

#draw a smiley face
def draw_smiley_eye(length, degree):
    "function to draw one smiley eye"
    for number in range(25):
        Jay.forward(length)
        Jay.right(degree)

def draw_smiley_eyes(length, degree):
    "function to draw smiley eyes"
    draw_smiley_eye(length, degree)
    Jay.penup()
    Jay.left(100)
    Jay.forward(17)
    Jay.pendown()
    draw_smiley_eye(length, degree)

def draw_simley_face(length,degree):
    "function to draw a smiley face"
    draw_smiley_eyes(length,degree)
    Jay.penup()
    Jay.right(100)
    Jay.forward(20)
    Jay.left(90)
    Jay.forward(70)
    Jay.right(40)
    Jay.pendown()
    for number in range(25):
        Jay.forward(length)
        Jay.right(degree)
    Jay.hideturtle()

draw_simley_face(2,5)

# Close the turtle graphics window on click
window.exitonclick()
