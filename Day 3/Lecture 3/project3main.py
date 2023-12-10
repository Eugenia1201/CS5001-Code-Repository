""" CS 5001 - Fall 2023 - Project 3 - Guided Turtles

by Steve Shafer
"""

import turtle


def do_forward(arguments):
    """ Move forward

    Args:
        arguments (list of strings): [0] is how far to move forward
    """
    if len(arguments) < 2:
        how_far_to_move = int(arguments[0] if len(arguments) > 0 else 100)
        steve.forward(how_far_to_move)
    else:
        print("Whoa!  Too many arguments, my poor\
 little turtle head is spinning!")


def do_left(arguments):
    """ Turn left

    Args:
        arguments (list of strings): [0] is how far to turn
    """
    if len(arguments) < 2:
        how_far_to_turn = int(arguments[0] if len(arguments) > 0 else 45)
        steve.left(how_far_to_turn)
    else:
        print("Whoa!  Too many arguments, my poor\
 little turtle head is spinning!")


def do_box(arguments):
    """ Draw a box

    Args:
        arguments (list of strings): [0] is how big to make the box
    """
    if len(arguments) < 2:
        how_wide = 100
        how_high = 100
        if (len(arguments) > 0) and (arguments[0].count("x") == 1):
            dimension_list = arguments[0].split(sep="x")
            how_wide = int(dimension_list[0])
            how_high = int(dimension_list[1])
        # should do more error checking, but this is enough for this project
        for _ in range(2):
            steve.forward(how_wide)
            steve.left(90)
            steve.forward(how_high)
            steve.left(90)
    else:
        print("Whoa!  Too many arguments, my poor\
 little turtle head is spinning!")


def do_color(arguments):
    """ Change color

    Args:
        arguments (list of strings): [0] is the new color name
    """
    if len(arguments) == 1:
        if arguments[0] in allowed_colors:
            steve.color(arguments[0])
        else:
            print("What-what-what color would that be???")
    else:
        print("Whoa!  Wrong number of arguments, my poor\
 little turtle head is spinning!")


def do_move(arguments):
    """ Move turtle to indicated place

    Args:
        arguments (list of strings): [0] is x, [1] is y
    """
    if len(arguments) == 2:
        steve.penup()
        steve.setposition(int(arguments[0]), int(arguments[1]))
        steve.pendown()
    else:
        print("Whoa!  Wrong number of arguments, my poor\
 little turtle head is spinning!")


# Main Program

if (__name__ == "__main__"):

    window = turtle.Screen()
    steve = turtle.Turtle()

    allowed_colors = ["red", "green", "blue"]

    # Turtle program
    keep_going = True
    while keep_going:
        input_string = input("What now, master? ")
        argument_list = input_string.lower().split()

        if len(argument_list) < 1:
            print("What's that you say?")

        elif argument_list[0] == "forward":
            do_forward(argument_list[1:])

        elif argument_list[0] == "left":
            do_left(argument_list[1:])

        elif argument_list[0] == "box":
            do_box(argument_list[1:])

        elif argument_list[0] == "color":
            do_color(argument_list[1:])

        elif argument_list[0] == "move":
            do_move(argument_list[1:])

        elif argument_list[0] == "bye":
            keep_going = False

        else:
            print("I do not understand this foolishness!")

    window.bye()
