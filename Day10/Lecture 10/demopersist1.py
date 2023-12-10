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
    p1 = Point(3, 4)
    p2 = Point(2, 3)

    pl1 = PointList(p1, p2)
    s1 = jsonpickle.encode(pl1)

    with open("persist1.json", "w") as out_file:
        out_file.write(s1)
