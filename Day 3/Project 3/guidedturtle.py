"""CS5001_Kaiqi Zhang_Project3_Sep/27/2023"""

import turtle
import random


def do_forward(arguments):
    """
    This function makes turtle go forward

    Args:
        arguments (list): command from user input 
    """    
    
    if len(arguments) == 1:
        frank.forward(int(arguments[0]))
    elif len(arguments) > 1:
        print("Input invalid!")
    else:
        frank.forward(50)


def turn_left(arguments):
    """This function makes turtle turn left

    Args:
        arguments (list): command from user input
    """    
    if len(arguments) == 1:
        frank.left(int(arguments[0]))
    elif len(arguments) > 1:
        print("Input invalid!")
    else:
        frank.left(45)


def draw_box(argument):
    """This funciton makes turtle draw a box

    Args:
        argument (string): command from user input
    """    
    argument_size = argument.split(sep="x")
    width = int(argument_size[0])
    height = int(argument_size[1])

    if len(argument_size) != 2 or "x" not in argument:
        print("Invalid input!")
    else:
        for number in range(2):
            frank.forward(width)
            frank.left(90)
            frank.forward(height)
            frank.left(90)


def draw_color(argument):
    """This function makes turtle draw in a given color

    Args:
        argument (string): command from user input
    """    
    if argument in colors:
        frank.color(argument)
    else:
        print("Invalid input!")


def move_to(argument):
    """This function makes turtle move to a specific location

    Args:
        argument (list): command from user input
    """    
    frank.penup()
    if len(argument) == 0:
        frank.goto(random.random(), random.random())
    elif len(argument) == 1:
        print("Invalid input!")
    else:
        frank.goto(int(argument[0]), int(argument[1]))
    frank.pendown()



# window = turtle.Screen()
# frank = turtle.Turtle()

# LOOP_CONTINUE = True
# colors = ["blue", "brown", "black", "beige", "gray", "hotpink"]

# while LOOP_CONTINUE:
#     input_string = input("please type in your command").lower()
#     argument_list = input_string.split()

#     if argument_list[0] == "forward":
#         do_forward(argument_list[1:])
#     elif argument_list[0] == "left":
#         turn_left(argument_list[1:])
#     elif argument_list[0] == "box":
#         draw_box(argument_list[1])
#     elif argument_list[0] == "color":
#         draw_color(argument_list[1])
#     elif argument_list[0] == "move":
#         move_to(argument_list[1:])
#     elif argument_list[0] == "bye":
#         LOOP_CONTINUE = False
#     else:
#         print("I don't understand it!")

# window.bye()

print(__name__)





