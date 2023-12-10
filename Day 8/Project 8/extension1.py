"""CS 5001 - 23fall - Project 8 - Extension 1 - Kaiqi Zhang - 8 Nov 2023
   Chapter 16: Classes and Objects — Digging a little deeper
"""
# import copy


class Point:
    """ Create a new point at coordinates x, y"""
    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


class Rectangle:
    """ A class to manufacture rectangle objects """
    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h. """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        """ Return the position of lower left corner, width and height of
        a rectangule object. """
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas. """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas. """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        """ Return the area of a rectangle object. """
        return self.width * self.height

    def perimeter(self):
        """ Return the perimeter of a rectangle object."""
        return self.width * 2 + self.height * 2

    def flip(self):
        """ Flip the width and the height of a rectangle object."""
        self.width, self.height = self.height, self.width

    def contains(self, point):
        """ Test if a Point object fall within a rectangle object."""
        x_upper_bound = self.corner.x + self.width
        y_upper_bound = self.corner.y + self.height
        if (self.corner.x <= point.x < x_upper_bound) and \
                (self.corner.y <= point.y < y_upper_bound):
            return True
        else:
            return False

    def get_all_points_on_perimeter(self):
        """
        Get all points on the perimeter of a rectangle object into
        a list of tuples.
        """
        self.points_on_perimeter = set([])
        lower_right_corner_x = self.corner.x + self.width
        upper_left_corner_y = self.corner.y + self.height

        # Get point on the base of the Rectangle object
        for base in range(lower_right_corner_x):
            self.points_on_perimeter.add((base, self.corner.y))

        # Get point on the top of the Rectangle object
        for top in range(lower_right_corner_x):
            self.points_on_perimeter.add((top, upper_left_corner_y))

        # Get point on the left edge of the Rectangle object
        for left_edge in range(upper_left_corner_y):
            self.points_on_perimeter.add((self.corner.x, left_edge))

        # Get point on the right edge of the Rectangle object
        for right_edge in range(upper_left_corner_y):
            self.points_on_perimeter.add((lower_right_corner_x, right_edge))

        return self.points_on_perimeter

    def collision_detection(self, rectangle):
        """ Check if two rectangle objects overlap. """
        for tuple in rectangle.get_all_points_on_perimeter():
            (x, y) = tuple
            point = Point(x, y)
            if self.contains(point):
                return True
        return False


# Main Program
# if __name__ == "__main__":

    # ======16.1 Rectangles======
    # box = Rectangle(Point(0, 0), 100, 200)
    # bomb = Rectangle(Point(100, 80), 5, 10)
    # print("box: ", box)
    # print("bomb: ", bomb)

    # ======16.2 Objects are mutable======
    # r = Rectangle(Point(10, 5), 100, 50)
    # print(r)
    # r.grow(25, -10)
    # print(r)
    # r.move(-10, 10)
    # print(r)

    # ======16.3 Sameness======
    # p1 = Point(3, 4)
    # p2 = Point(3, 4)
    # print(p1 is p2)
    # p3 = p1
    # print(p1 is p3)  # Compares only the references - shallow equality

    # def same_coordinates(p1, p2):
    #     """Compare if two points have the same x and y coordinates
    #     """
    #     return (p1.x == p2.x) and (p1.y == p2.y)

    # print(same_coordinates(p1, p2))  # deep equality

    # ======16.4 Copying======
    # p1 = Point(3, 4)
    # p2 = copy.copy(p1)  # Shallow copying
    # print(p1 is p2)
    # print(same_coordinates(p1, p2))
    # b1 = Rectangle(Point(0, 0), 100, 200)
    # b2 = copy.deepcopy(b1)  # Deepcopy
    # print(b1 is b2)
    # print(same_coordinates(b1.corner, b2.corner))
