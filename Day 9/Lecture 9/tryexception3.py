""" Exceptions - try ... else and finally
"""


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


# input("Try divide(2,1):")
# divide(2, 1)

# input("Try divide(2,0):")
# divide(2, 0)

input("Try divide('2','1'):")
divide("2", "1")
# printing "executing finally clause" first, then throw the TypeError below
# TypeError: unsupported operand type(s) for /: 'str' and 'str'
