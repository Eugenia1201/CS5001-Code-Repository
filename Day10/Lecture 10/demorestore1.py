"""Try persistence with JSON."""

import jsonpickle


class Point:
    """An x y z point."""

    def __init__(self, x, y, z=None):
        """Initialize the point."""
        self.x = x
        self.y = y
        self.z = z


class PointList:
    """A list of points."""

    def __init__(self, p1, p2):
        """Initialize the list of points."""
        self.points = [p1, p2]


if __name__ == "__main__":
    with open("persist1.json", "r", newline="") as in_file:
        s1 = in_file.read()
        pl1 = jsonpickle.decode(s1)

        s2 = jsonpickle.encode(pl1, indent=2)
        print(s2)
