"""CS 5001 - Kaiqi Zhang - Project 6 'The Forest Awakens' - 26 Oct
"""

import pyglet
import pyglet_colors as pc
import math
import random

window = pyglet.window.Window(width=1000, height=1000)
pause = False


class Tree:
    """
    Represents a tree in a forest.

    Attributes:
        x (int): The x-coordinate of the tree's position.
        y (int): The y-coordinate of the tree's position.
        size (float): The size of the tree.
    """
    def __init__(self, x, y, size):
        """
        Initialize a Tree object.

        Args:
            x (int): The x-coordinate of the tree's position.
            y (int): The y-coordinate of the tree's position.
            size (float): The size of the tree.
        """
        self.x = x
        self.y = y
        self.size = size
        self.trees = pyglet.graphics.Batch()
        # Draw the leaves (a triangle)
        self.leaves1 = pyglet.shapes.Triangle(self.x*self.size,
                                              self.y*self.size,
                                              (self.x+50)*self.size,
                                              (self.y+200)*self.size,
                                              (self.x+100)*self.size,
                                              self.y*self.size,
                                              color=pc.GREEN,
                                              batch=self.trees)
        # Draw the trunk (a rectangle)
        self.trunk = pyglet.shapes.Rectangle((self.x+45)*self.size,
                                             (self.y-100)*self.size,
                                             10*self.size,
                                             100*self.size,
                                             color=(222, 184, 135, 255),
                                             batch=self.trees)

    def draw(self):
        """
        Draw the tree using Pyglet graphics.
        """
        self.trees.draw()


class Animal:
    """
    Represents an animal, specifically a cat.

    Attributes:
        x (int): The x-coordinate of the cat's position.
        y (int): The y-coordinate of the cat's position.
        size (float): The size of the cat.
    """
    def __init__(self, x, y, size):
        """
        Initialize an Animal (cat) object.

        Args:
            x (int): The x-coordinate of the cat's position.
            y (int): The y-coordinate of the cat's position.
            size (float): The size of the cat.
        """

        self.x = x
        self.y = y
        self.size = size
        self.cat = pyglet.graphics.Batch()
        self.shapes = []

        # Draw the cat's head (a circle)
        head = pyglet.shapes.Circle(self.x*size,
                                    self.y*size,
                                    38*size,
                                    color=pc.LIGHTSLATEGRAY,
                                    batch=self.cat)
        self.shapes.append(head)

        # Draw the cat's eyes (two circles)
        l_eye = pyglet.shapes.Circle((self.x-15)*size,
                                     (self.y+10)*size,
                                     7*size, color=pc.BLACK,
                                     batch=self.cat)
        self.shapes.append(l_eye)
        r_eye = pyglet.shapes.Circle((self.x+15)*size,
                                     (self.y+10)*size,
                                     7*size, color=pc.BLACK,
                                     batch=self.cat)
        self.shapes.append(r_eye)

        # Draw the cat's nose (a small pink ellipse)
        nose = pyglet.shapes.Ellipse((self.x)*size,
                                     (self.y-10)*size,
                                     4*size, 2*size,
                                     color=pc.BLACK,
                                     batch=self.cat)
        self.shapes.append(nose)

        # Draw the cat's mouth (a curve)
        mouth = pyglet.shapes.Arc((self.x)*size,
                                  (self.y-20)*size,
                                  10*size, start_angle=180,
                                  angle=math.pi*2/3,
                                  color=pc.BLACK,
                                  batch=self.cat)
        self.shapes.append(mouth)

        # Draw the cat's ears (two triangles)
        l_ear = pyglet.shapes.Triangle((self.x-30)*size, (self.y+10)*size,
                                       (self.x-35)*size, (self.y+45)*size,
                                       (self.x-10)*size, (self.y+30)*size,
                                       color=pc.LIGHTSLATEGRAY, batch=self.cat)
        r_ear = pyglet.shapes.Triangle((self.x+10)*size, (self.y+30)*size,
                                       (self.x+35)*size, (self.y+45)*size,
                                       (self.x+30)*size, (self.y+10)*size,
                                       color=pc.LIGHTSLATEGRAY, batch=self.cat)
        self.shapes.append(l_ear)
        self.shapes.append(r_ear)

        # Draw the cat's body (an ellipse)
        body = pyglet.shapes.Ellipse(self.x*size, (self.y-100)*size,
                                     40*size, 70*size,
                                     color=pc.LIGHTSLATEGRAY, batch=self.cat)
        self.shapes.append(body)

        # Draw the cat's feet (an sector)
        l_foot = pyglet.shapes.Sector((self.x-17)*size, (self.y-160)*size,
                                      20*size, start_angle=53,
                                      angle=math.pi*2/3,
                                      color=pc.LIGHTSLATEGRAY,
                                      batch=self.cat)
        r_foot = pyglet.shapes.Sector((self.x+17)*size, (self.y-160)*size,
                                      20*size, start_angle=55,
                                      angle=math.pi*2/3,
                                      color=pc.LIGHTSLATEGRAY,
                                      batch=self.cat)
        self.shapes.append(l_foot)
        self.shapes.append(r_foot)

    def draw(self):
        """
        Draw the cat using Pyglet graphics.
        """
        self.cat.draw()

    def move(self, new_x, new_y):
        """
        Move the cat to a new position.

        Args:
            new_x (int): The new x-coordinate for the cat.
            new_y (int): The new y-coordinate for the cat.
        """
        dx = new_x - self.x
        dy = new_y - self.y
        for shape in self.shapes:
            shape.x += dx
            shape.y += dy
        self.x = new_x
        self.y = new_y


class Family:
    """
    Represents a family of animals (cats).

    Attributes:
        mama (Animal): The mother cat in the family.
        papa (Animal): The father cat in the family.
        kids (list): A list of kid cat objects in the family.
    """
    def __init__(self, x, y):
        """
        Initialize a Family object.

        Args:
            x (int): The x-coordinate of the family's position.
            y (int): The y-coordinate of the family's position.
        """
        self.mama = Animal(x, y, 1)
        self.papa = Animal(x+70, y-60, 1.2)
        self.kids = []
        num_kids = random.randint(3, 5)
        for x in range(num_kids):
            kid = Animal(x, y, size=random.uniform(0.3, 0.5))
            self.kids.append(kid)

    def draw(self):
        """
        Draw the entire cat family, including mama, papa, and kids.
        """

        self.mama.draw()
        self.papa.draw()
        for kid in self.kids:
            kid.draw()

    def move(self):
        """
        Move the family, including random movement for mama and
        bouncing off window edges.

        Papa maintains the same relevant distance to mama during the move.
        Kids moves randomly but still around mama.
        """

        # make random movement for mama
        new_x = self.mama.x + random.randrange(-200, 200)
        new_y = self.mama.y + random.randrange(-200, 200)

        # make the family bounce off the edge of the window
        if new_x < 0:
            new_x = -new_x
        elif new_x > window.width:
            new_x = window.width - (new_x - window.width)
        if new_y < 0:
            new_y = -new_y
        elif new_y > window.width:
            new_y = window.height - (new_y - window.height)
        dx = new_x - self.mama.x
        dy = new_y - self.mama.y

        self.mama.move(new_x, new_y)
        self.papa.move(self.papa.x+dx, self.papa.y+dy)

        for kid in self.kids:
            kid_new_x = self.mama.x + random.randint(-100, 100)
            kid_new_y = self.mama.y + random.randint(200, 250)
            kid.move(kid_new_x, kid_new_y)


class Forest:
    """
    Represents a forest containing trees and animal families.

    Attributes:
        trees (list): A list of Tree objects in the forest.
        families (list): A list of Family objects in the forest.
    """

    def __init__(self):
        """
        Initialize a Forest object with trees and families.
        """

        self.trees = []
        self.families = []
        for _ in range(12):
            tree = Tree(x=random.randint(10, window.width-200),
                        y=random.randint(200, window.height-250),
                        size=random.uniform(0.7, 1.2))
            self.trees.append(tree)
        family1 = Family(x=random.randint(100, window.width//2),
                         y=random.randint(200, window.height-300))
        self.families.append(family1)

        family2 = Family(x=random.randint(window.width//2, window.width-400),
                         y=random.randint(200, window.height-300))
        self.families.append(family2)

    def draw(self):
        """
        Draw the entire forest, including trees and animal families.
        """

        for tree in self.trees:
            tree.draw()

        for family in self.families:
            family.draw()

    def move(self):
        """
        Move the animal families in the forest.
        """

        for family in self.families:
            family.move()


class App:
    """
    Represents the main application.

    This class is responsible for running the forest simulation.

    Attributes:
        None
    """
    def __init__(self):
        """
        Initialize the App object.
        """

        pass

    def run(self):
        """
        Run the forest simulation application.
        """
        forest = Forest()

        @window.event
        def on_draw():
            window.clear()
            forest.draw()

        def update(self):
            if not pause:
                forest.move()

        @window.event
        def on_key_press(symbol, modifiers):
            global pause
            if symbol == pyglet.window.key.SPACE:
                pause = not pause

        pyglet.clock.schedule_interval(update, 1/3)
        pyglet.app.run()


# MAIN PROGRAM
if __name__ == "__main__":
    app = App()
    app.run()
