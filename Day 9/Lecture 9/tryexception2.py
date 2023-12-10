""" Exceptions with analyzing Exception object
"""

try:
    my_file = open("testfile", "r")
    print("Opened testfile")
except OSError as exc:
    print("Error: can't find testfile or open it for reading")
    print(exc)
    print(f"errno={exc.errno} filename='{exc.filename}'")
    print(f"strerror='{exc.strerror}'")

print()
try:
    my_file2 = open("testfile2", "w")
    print("Opened testfile2")
except FileNotFoundError:
    print("Error:  can't find testfile2")
except PermissionError as exc:
    print("No permission to open testfile2 for writing")
    print(exc)
