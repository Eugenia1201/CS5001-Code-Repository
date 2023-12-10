"This is the working file to draw a fractal tree"
import turtle

# Create a turtle screen and a turtle
window = turtle.Screen()
window.setup(width=0.9, height=0.9, startx=None, starty=None)
Leaf = turtle.Turtle()
Leaf.speed("fastest")

# Function to draw a fractal tree


def fractal_tree(branch_len, Leaf):
    if branch_len > 5:
        Leaf.forward(branch_len)
        Leaf.right(20)
        fractal_tree(branch_len - 15, Leaf)
        Leaf.left(40)
        fractal_tree(branch_len - 15, Leaf)
        Leaf.right(20)
        Leaf.backward(branch_len)


Leaf.left(90)
Leaf.up()
Leaf.backward(300)
Leaf.down()
fractal_tree(120, Leaf)
Leaf.hideturtle()


# Close the turtle graphics window on click
window.exitonclick()
