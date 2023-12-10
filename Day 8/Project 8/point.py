"""CS 5001 - 23fall - Project 8 - "The Point Class" - Kaiqi Zhang - 8 Nov 2023
"""


class Point:
    """ Point class represents and manipulates x, y coords.
    """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y."""
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def print_point(pt):
        """ Print out the object in a string format """
        print("({0}, {1})".format(pt.x, pt.y))

    # def to_string(self):
    #   """ Print out the object in a string format """
    #     return "({0}, {1})".format(self.x, self.y)

    def __str__(self):
        """ return the object in a string format using dunder method """
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def __add__(self, other):
        """ create and return a new Point by adding x, y coordinates
        with another point's x, y coordinates """
        return Point(self.x + other.x,  self.y + other.y)

    def __mul__(self, other):
        """ return the dot product of self and another point """
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        """ create and return a new Point after scalar multiplication """
        return Point(other * self.x,  other * self.y)

    def reverse(self):
        """ swap the x and y coordinates of a Point """
        (self.x, self.y) = (self.y, self.x)


if __name__ == "__main__":
    # ======15.2 User-defined compound data types======
    # p = Point()
    # q = Point()

    # print(p.x, p.y, q.x, q.y)

    # ======15.3 Attributes======
    # p.x = 3
    # p.y = 4
    # print(p.y)
    # x = p.x
    # print(x)

    # print("(x={0}, y={1})".format(p.x, p.y))
    # distance_squared_from_origin = p.x * p.x + p.y * p.y
    # print(distance_squared_from_origin)

    # ======15.4 Improving our initializer======
    # p = Point(4, 2)
    # q = Point(6, 3)
    # r = Point()       # r represents the origin (0, 0)
    # print(p.x, q.y, r.x)

    # ======15.5 Adding other methods to our class======
    # p = Point(3, 4)
    # q = Point(5, 12)
    # r = Point()
    # print(p.x)
    # print(p.y)
    # print(p.distance_from_origin())
    # print(q.x)
    # print(q.y)
    # print(q.distance_from_origin())
    # print(r.x)
    # print(r.y)
    # print(r.distance_from_origin())

    # ======15.7 Converting an instance to a string======
    # p = Point(3, 4)
    # print(p.to_string())
    # str(p)
    # print(p)

    # ======15.8 Instance as return values======
    # def midpoint(p1, p2):
    #     """ Return the midpoint of points p1 and p2 """
    #     mx = (p1.x + p2.x)/2
    #     my = (p1.y + p2.y)/2
    #     return Point(mx, my)

    # p = Point(3, 4)
    # q = Point(5, 12)
    # r = midpoint(p, q)
    # r = p.halfway(q)
    # print(r)
    # print(Point(3, 4).halfway(Point(5, 12)))

    # ======21.8 Operator overloading======
    # p1 = Point(3, 4)
    # p2 = Point(5, 7)
    # print(p1 * p2)
    # print(2 * p2)

    # ======21.9 Polymorphism======
    # def multadd(x, y, z):
    #     return x * y + z

    # p1 = Point(3, 4)
    # p2 = Point(5, 7)
    # print(multadd(2, p1, p2))
    # print(multadd(p1, p2, 1))

    def front_and_back(front):
        """ print out a list twice, forward and backward """
        import copy
        back = copy.copy(front)
        back.reverse()
        print(str(front) + str(back))

    p = Point(3, 4)
    front_and_back(p)
