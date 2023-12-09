""" Exceptions handled
"""

try:
    my_file = open("testfile", "r")
except FileNotFoundError:
    print("Error: can't find file or open it for reading")
