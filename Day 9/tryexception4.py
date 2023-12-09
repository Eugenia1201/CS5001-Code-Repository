""" Exceptions and raise
    Exception chaining
"""


class MyError(Exception):
    def __init__(self, message, x, y):
        super().__init__(message)
        self.x = x
        self.y = y


try:
    raise MyError("Help!", 3, 4)
except MyError as err:
    print(err)
    print(f"{err.x=} {err.y=}")
    raise err
