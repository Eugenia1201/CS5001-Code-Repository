"""Try JSON serializer."""

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
    print(s1)
    s2 = jsonpickle.encode(pl1, indent=2)
    print(s2)
    s3 = jsonpickle.encode(pl1, unpicklable=False)
    print(s3)
