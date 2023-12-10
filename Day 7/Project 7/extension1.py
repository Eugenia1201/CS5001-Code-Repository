"""CS 5001 - Kaiqi Zhang - Project 7 'Things That Fly' - 3 Nov

    Please note that I worked with the instructor on this project, and he
    helped me refactor the code to make the second ground animal inherit from
    the first one, instead of being a subclass of Animal class.
"""

import pyglet
import pyglet_colors as pc
import math
import random
import datetime

window = pyglet.window.Window(width=1000, height=1000)
pause = False


class Tree:
    """
    Represents a tree in a forest.

    Attributes:
        x (int): The x-coordinate of the tree's position.
        y (int): The y-coordinate of the tree's position.
        size (float): The size of the tree.

    Methods:
        draw():
            Draws the tree using Pyglet graphics.
        perch_x():
            Return the x coordinates for the flyer to land
        perch_y():
            Return the y coordinates for the flyer to land
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

    def perch_x(self):
        """
        Return the x coordinates plus a 100 pixels offset for the flyer to land
        """
        return self.x+100

    def perch_y(self):
        """
        Return the y coordinates plus a 400 pixels offset for the flyer to land
        """
        return self.y+400


class Animal:
    """
    Initializes an Animal object by creating a Pyglet batch for graphics
    and an empty list to store shapes.

    Attributes:
        batch (pyglet.graphics.Batch): A Pyglet batch for drawing shapes.
        shapes (list): A list to store shape objects for drawing.

    Methods:
        draw():
            Draw the Animal using Pyglet graphics.
    """
    def __init__(self):
        """
        Initialize an Animal object.
        """
        self.batch = pyglet.graphics.Batch()
        self.shapes = []

    def draw(self):
        """
        Draw the Animal using Pyglet graphics.
        """
        self.batch.draw()


class Cat(Animal):
    """
    Represents a Cat, a subclass of the Animal class.

    Attributes:
        x (int): The x-coordinate of the Cat's position.
        y (int): The y-coordinate of the Cat's position.
        size (float): The size of the Cat.
    Method:
        move(new_x, new_y):
            Moves the Cat to a new position.
    """
    def __init__(self, x, y, size):
        """
        Initializes a Cat object.

        Args:
            x (int): The x-coordinate of the Cat's head position.
            y (int): The y-coordinate of the Cat's head position.
            size (float): The size of the Cat.

        Initializes and draws the Cat's body parts using Pyglet shapes.
        """
        self.x = x
        self.y = y
        self.size = size
        super().__init__()
        # Draw the cat's head (a circle)
        head = pyglet.shapes.Circle(self.x*size,
                                    self.y*size,
                                    38*size,
                                    color=pc.LIGHTSLATEGRAY,
                                    batch=self.batch)
        self.shapes.append(head)

        # Draw the cat's eyes (two circles)
        l_eye = pyglet.shapes.Circle((self.x-15)*size,
                                     (self.y+10)*size,
                                     7*size, color=pc.BLACK,
                                     batch=self.batch)
        self.shapes.append(l_eye)
        r_eye = pyglet.shapes.Circle((self.x+15)*size,
                                     (self.y+10)*size,
                                     7*size, color=pc.BLACK,
                                     batch=self.batch)
        self.shapes.append(r_eye)

        # Draw the cat's nose (a small pink ellipse)
        nose = pyglet.shapes.Ellipse((self.x)*size,
                                     (self.y-10)*size,
                                     4*size, 2*size,
                                     color=pc.BLACK,
                                     batch=self.batch)
        self.shapes.append(nose)

        # Draw the cat's mouth (a curve)
        mouth = pyglet.shapes.Arc((self.x)*size,
                                  (self.y-20)*size,
                                  10*size, start_angle=180,
                                  angle=math.pi*2/3,
                                  color=pc.BLACK,
                                  batch=self.batch)
        self.shapes.append(mouth)

        # Draw the cat's ears (two triangles)
        l_ear = pyglet.shapes.Triangle((self.x-30)*size, (self.y+10)*size,
                                       (self.x-35)*size, (self.y+45)*size,
                                       (self.x-10)*size, (self.y+30)*size,
                                       color=pc.LIGHTSLATEGRAY,
                                       batch=self.batch)
        r_ear = pyglet.shapes.Triangle((self.x+10)*size, (self.y+30)*size,
                                       (self.x+35)*size, (self.y+45)*size,
                                       (self.x+30)*size, (self.y+10)*size,
                                       color=pc.LIGHTSLATEGRAY,
                                       batch=self.batch)
        self.shapes.append(l_ear)
        self.shapes.append(r_ear)

        # Draw the cat's body (an ellipse)
        body = pyglet.shapes.Ellipse(self.x*size, (self.y-100)*size,
                                     40*size, 70*size,
                                     color=pc.LIGHTSLATEGRAY, batch=self.batch)
        self.shapes.append(body)

        # Draw the cat's feet (an sector)
        l_foot = pyglet.shapes.Sector((self.x-17)*size, (self.y-160)*size,
                                      20*size, start_angle=53,
                                      angle=math.pi*2/3,
                                      color=pc.LIGHTSLATEGRAY,
                                      batch=self.batch)
        r_foot = pyglet.shapes.Sector((self.x+17)*size, (self.y-160)*size,
                                      20*size, start_angle=55,
                                      angle=math.pi*2/3,
                                      color=pc.LIGHTSLATEGRAY,
                                      batch=self.batch)
        self.shapes.append(l_foot)
        self.shapes.append(r_foot)

    def move(self, new_x, new_y):
        """
        Moves the Cat to a new position.

        Args:
            new_x (int): The new x-coordinate for the Cat.
            new_y (int): The new y-coordinate for the Cat.

        Moves the Cat and updates the positions of its body parts.
        """
        dx = new_x - self.x
        dy = new_y - self.y
        for shape in self.shapes:
            shape.x += dx
            shape.y += dy
        self.x = new_x
        self.y = new_y


class Tiger(Cat):
    """
    Represents a Tiger, a subclass of the Cat class.

    Attributes:
        Inherits attributes from the Cat class.
    """
    def __init__(self, x, y, size):
        """
        Initializes a Tiger object.

        Args:
            x (int): The x-coordinate of the Tiger's beard position.
            y (int): The y-coordinate of the Tiger's beard position.
            size (float): The size of the Tiger.

        Initializes and draws the Tiger's body parts using Pyglet shapes.
        """
        super().__init__(x, y, size)
        self.rbeard1 = pyglet.shapes.Line(x*size, (y-10)*size,
                                          (x+30)*size, (y+5)*size, 1,
                                          color=pc.GOLD1, batch=self.batch)
        self.rbeard2 = pyglet.shapes.Line(x*size, (y-10)*size, (x+30)*size,
                                          (y-5)*size, 1,
                                          color=pc.GOLD1, batch=self.batch)
        self.rbeard3 = pyglet.shapes.Line(x*size, (y-10)*size, (x+30)*size,
                                          (y-15)*size, 1,
                                          color=pc.GOLD1, batch=self.batch)
        self.shapes.append(self.rbeard1)
        self.shapes.append(self.rbeard2)
        self.shapes.append(self.rbeard3)
        self.lbeard1 = pyglet.shapes.Line(x*size, (y-10)*size,
                                          (x-30)*size, (y+5)*size, 1,
                                          color=pc.GOLD1, batch=self.batch)
        self.lbeard2 = pyglet.shapes.Line(x*size, (y-10)*size, (x-30)*size,
                                          (y-5)*size, 1,
                                          color=pc.GOLD1, batch=self.batch)
        self.lbeard3 = pyglet.shapes.Line(x*size, (y-10)*size, (x-30)*size,
                                          (y-15)*size, 1,
                                          color=pc.GOLD1, batch=self.batch)
        self.shapes.append(self.lbeard1)
        self.shapes.append(self.lbeard2)
        self.shapes.append(self.lbeard3)


class Bee(Animal):
    """
    Represents a Bee, a subclass of the Animal class.

    Attributes:
        x (int): The x-coordinate of the Bee's position.
        y (int): The y-coordinate of the Bee's position.
        size (float): The size of the Bee.
        last_moved (datetime): The timestamp of the last movement.

    Methods:
        move(new_x, new_y):
            Moves the Bee to a new position.

        Args:
            new_x (int): The new x-coordinate for the Bee.
            new_y (int): The new y-coordinate for the Bee.

        Moves the Bee and updates its position while limiting its
        moving frequency.
    """
    def __init__(self, x, y, size):
        """
        Initializes a Bee object.

        Args:
            x (int): The x-coordinate of the Bee's position.
            y (int): The y-coordinate of the Bee's position.
            size (float): The size of the Bee.
            last_moved (datetime): The timestamp of the last movement.

        Initializes and draws the Bee's body parts using Pyglet shapes.
        """
        super().__init__()
        self.x = x
        self.y = y
        self.size = size

        # Body of the bee (an ellipse)
        body = pyglet.shapes.Ellipse(self.x*size, self.y*size, 50*size,
                                     25*size, color=pc.YELLOW1,
                                     batch=self.batch)
        self.shapes.append(body)
        # Head of the bee (a smaller ellipse)
        head = pyglet.shapes.Circle((self.x+50)*size, self.y*size, 25*size,
                                    color=pc.YELLOW2, batch=self.batch)
        self.shapes.append(head)
        # Eyes of the bee (two circles)
        eye1 = pyglet.shapes.Circle((self.x+65)*size, (self.y+15)*size, 8*size,
                                    color=pc.BLACK, batch=self.batch)
        self.shapes.append(eye1)
        eye2 = pyglet.shapes.Circle((self.x+65)*size, (self.y-10)*size, 8*size,
                                    color=pc.BLACK, batch=self.batch)
        self.shapes.append(eye2)
        # Wings of the bee (two rectangles)
        wing1 = pyglet.shapes.Ellipse(self.x*size, self.y*size, 8*size,
                                      40*size, color=pc.YELLOW4,
                                      batch=self.batch)
        self.shapes.append(wing1)
        wing2 = pyglet.shapes.Ellipse((self.x-20)*size, self.y*size, 8*size,
                                      40*size, color=pc.YELLOW4,
                                      batch=self.batch)
        self.shapes.append(wing2)
        wing3 = pyglet.shapes.Ellipse((self.x+20)*size, (self.y)*size, 8*size,
                                      40*size, color=pc.YELLOW4,
                                      batch=self.batch)
        self.shapes.append(wing3)
        # Instance variable
        self.last_moved = datetime.datetime.now()

    def move(self, new_x, new_y):
        """
        Moves the Bee to a new position.

        Args:
            new_x (int): The new x-coordinate for the Bee.
            new_y (int): The new y-coordinate for the Bee.

        Moves the Bee and updates its position while limiting its
        moving frequency.
        """
        if ((datetime.datetime.now() - self.last_moved) < datetime
                .timedelta(seconds=random.randint(1, 5))):
            return
        else:
            dx = new_x - self.x
            dy = new_y - self.y
            for shape in self.shapes:
                shape.x += dx
                shape.y += dy
            self.x = new_x
            self.y = new_y
            self.last_moved = datetime.datetime.now()


class Family:
    """
    Represents a Family of animals.

    Attributes:
        mama (Animal): The mother of the family.
        papa (Animal): The father of the family.
        kids (list): List of kids (Animal instances).

    Methods:
        draw():
            Draws the entire family on the screen.

        move():
            Moves the entire family, including parents and kids.
    """
    def __init__(self, animal_class):
        """
        Initializes a Family object with parents and kids of the specified
        animal class.

        Args:
            animal_class (class): The class of animals in the family.
        """
        self.mama = animal_class(500, 500, 1)
        self.papa = animal_class(550, 450, 1.2)
        self.kids = []
        num_kids = random.randint(3, 5)
        for x in range(num_kids):
            kid = animal_class(800, 800, size=random.uniform(0.3, 0.5))
            self.kids.append(kid)

    def draw(self):
        """
        Draws the entire family on the screen.
        """
        self.mama.draw()
        self.papa.draw()
        for kid in self.kids:
            kid.draw()

    def move(self):
        """
        Moves the entire family, including parents and kids.
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
            kid_new_x = self.mama.x + random.randint(300, 500)
            kid_new_y = self.mama.y + random.randint(300, 400)
            kid.move(kid_new_x, kid_new_y)


class Forest:
    """
    Represents a forest environment with trees, families, and flocks of
    animals.

    Attributes:
        trees (list): List of Tree objects.
        families (list): List of Family objects.
        flocks (list): List of Flock objects.

    Methods:
        draw():
            Draws the entire forest on the screen.

        move():
            Moves all the families and flocks in the forest.
    """
    def __init__(self):
        """
        Initializes a Forest object with trees, families, and
        flocks of animals.
        """
        self.trees = []
        self.families = [Family(Tiger), Family(Cat)]
        for _ in range(20):
            tree = Tree(x=random.randint(10, window.width-200),
                        y=random.randint(200, window.height-250),
                        size=random.uniform(0.7, 1.5))
            self.trees.append(tree)

        self.flocks = [Flock(Bee, self)]

    def draw(self):
        """
        Draws the entire forest on the screen.
        """
        for tree in self.trees:
            tree.draw()

        for family in self.families:
            family.draw()

        for flock in self.flocks:
            flock.draw()

    def move(self):
        """
        Moves all the families and flocks in the forest.
        """
        for family in self.families:
            family.move()
        for flock in self.flocks:
            flock.move()


class Flock:
    """
    Represents a flock of animals within the forest.

    Attributes:
        flyers (list): List of animal instances in the flock.

    Methods:
        move():
            Moves all the animals in the flock to new positions.

        draw():
            Draws all the animals in the flock on the screen.
    """
    def __init__(self, animal_class, forest):
        """
        Initializes a Flock object with animals of the specified class.

        Args:
            animal_class (class): The class of animals in the flock.
            forest (Forest): The forest where the flock resides.
        """
        self.flyers = []
        # Create a few flyers of the given animal class
        for _ in range(random.randint(3, 5)):
            random_tree = random.choice(forest.trees)
            x, y = random_tree.perch_x(), random_tree.perch_y()
            flyer = animal_class(x, y, size=random.uniform(0.3, 0.7))
            self.flyers.append(flyer)

    def move(self):
        """
        Moves all the animals in the flock to new positions.
        """
        for flyer in self.flyers:
            random_tree = random.choice(forest.trees)
            x, y = random_tree.perch_x(), random_tree.perch_y()
            flyer.move(x, y)

    def draw(self):
        """
        Draws all the animals in the flock on the screen.
        """
        for flyer in self.flyers:
            flyer.draw()


class App:
    """
    Represents the main application for running the forest simulation.

    Attributes:
        None

    Methods:
        run():Runs the forest simulation application.
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
        pyglet.clock.schedule_interval(update, 1/3)
        pyglet.app.run()


# MAIN PROGRAM
if __name__ == "__main__":

    forest = Forest()

    @window.event
    def on_draw():
        """
        Pyglet event handler for drawing the forest on the screen.
        """
        window.clear()
        forest.draw()

    def update(self):
        """
        Updates the forest's movements.
        """
        if not pause:
            forest.move()

    @window.event
    def on_key_press(symbol, modifiers):
        """
        Pyglet event handler for key presses (pausing the simulation).
        """
        global pause
        if symbol == pyglet.window.key.SPACE:
            pause = not pause

    app = App()
    app.run()
