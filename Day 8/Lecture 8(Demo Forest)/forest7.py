""" CS 5001 - Fall 2023 - Project 7
"""

import pyglet
import pyglet_colors
import random
import datetime

# CONSTANTS

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_MARGIN = 50
N_TREES_MIN = 12
N_TREES_MAX = 20
TREE_SIZE_MIN = 100
TREE_SIZE_MAX = 200
N_BABIES_MIN = 2
N_BABIES_MAX = 6
FLOCK_SIZE = 6
ADULT_SIZE = 70
BABY_SIZE = 30
FLYER_SIZE = 30
BABY_DX_MIN = -40
BABY_DX_MAX = 40
BABY_DY_MIN = -30
BABY_DY_MAX = 15
PAPA_DX = 35
PAPA_DY = -20
MOVE_LIMIT = 30
FLY_WAIT_MIN = 2
FLY_WAIT_MAX = 6

# GLOBAL VARIABLES

window = pyglet.window.Window(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
the_forest = None
forest_paused = False

# GRAPHICS FUNCTIONS


@window.event
def on_draw():
    """ Draw event for Pyglet - clear the window and draw stuff
    """
    window.clear()
    if the_forest is not None:
        the_forest.draw()


def update(dt):
    if (not forest_paused) and (the_forest is not None):
        the_forest.move()


@window.event
def on_key_press(symbol, modifiers):
    """This is called by Pyglet when a key is pressed

    Args:
        symbol (pyglet.window.key): The key that is pressed
        modifiers (pyglet.window.key): Modifiers but I don't think they work
    """
    global forest_paused
    if symbol == pyglet.window.key.SPACE:
        forest_paused = not forest_paused


# PROJECT CLASSES


class Forest:
    def __init__(self):
        self.tree_list = []
        for _ in range(random.randrange(N_TREES_MIN, N_TREES_MAX)):
            tree = Tree(random.randrange(WINDOW_MARGIN,
                                         WINDOW_WIDTH-WINDOW_MARGIN),
                        random.randrange(WINDOW_MARGIN,
                                         WINDOW_HEIGHT-WINDOW_MARGIN),
                        random.randrange(TREE_SIZE_MIN, TREE_SIZE_MAX))
            self.tree_list.append(tree)

    def populate(self):
        self.animal_group_list = []
        family1 = Family(random.randrange(WINDOW_MARGIN,
                                          WINDOW_WIDTH-WINDOW_MARGIN),
                         random.randrange(WINDOW_MARGIN,
                                          WINDOW_HEIGHT-WINDOW_MARGIN),
                         Bear)
        self.animal_group_list.append(family1)
        family2 = Family(random.randrange(WINDOW_MARGIN,
                                          WINDOW_WIDTH-WINDOW_MARGIN),
                         random.randrange(WINDOW_MARGIN,
                                          WINDOW_HEIGHT-WINDOW_MARGIN),
                         Cat)
        self.animal_group_list.append(family2)
        family3 = Flock(Butterfly)
        self.animal_group_list.append(family3)

    def draw(self):
        for tree in self.tree_list:
            tree.draw()
        for family in self.animal_group_list:
            family.draw()

    def move(self):
        for family in self.animal_group_list:
            family.move()

    def random_tree(self):
        return random.choice(self.tree_list)


class Tree:
    """ One tree in the forest
    """
    def __init__(self, x, y, size):
        """ create one tree
        """
        self.x = x
        self.y = y
        self.size = size
        self.shape_list = []
        self.batch = pyglet.shapes.Batch()
        trunk1 = pyglet.shapes.Rectangle(x-(size//40), y, size*0.05, size*0.2,
                                         pyglet_colors.BROWN, batch=self.batch)
        self.shape_list.append(trunk1)
        bottom_branches = pyglet.shapes.Triangle(x, y+(size*0.7),
                                                 x-(size*0.25), y+(size*0.2),
                                                 x+(size*0.25), y+(size*0.2),
                                                 color=pyglet_colors.GREEN,
                                                 batch=self.batch)
        self.shape_list.append(bottom_branches)
        middle_branches = pyglet.shapes.Triangle(x, y+(size*0.8),
                                                 x-(size*0.2), y+(size*0.4),
                                                 x+(size*0.2), y+(size*0.4),
                                                 color=pyglet_colors.GREEN,
                                                 batch=self.batch)
        self.shape_list.append(middle_branches)
        top_branches = pyglet.shapes.Triangle(x, y+size,
                                              x-(size*0.15), y+(size*0.6),
                                              x+(size*0.15), y+(size*0.6),
                                              color=pyglet_colors.GREEN,
                                              batch=self.batch)
        self.shape_list.append(top_branches)

    def draw(self):
        self.batch.draw()

    def perch_x(self):
        return random.randrange(int(self.x-(self.size*0.15)),
                                int(self.x+(self.size*0.15)))

    def perch_y(self):
        return random.randrange(int(self.y+(self.size*0.25)),
                                int(self.y+(self.size*0.8)))


class AnimalGroup:
    """ This is an interface for Family and Flock to show the methods they have in common
    """
    def move(self):
        pass

    def draw(self):
        pass


class Family(AnimalGroup):
    def __init__(self, x, y, animal_class):
        self.x = x
        self.y = y
        self.dx = random.randrange(-MOVE_LIMIT, MOVE_LIMIT)
        self.dy = random.randrange(-MOVE_LIMIT, MOVE_LIMIT)
        self.animal_list = []
        self.mama = animal_class(x, y, ADULT_SIZE)
        self.animal_list.append(self.mama)
        self.baby_list = []
        for _ in range(random.randrange(N_BABIES_MIN, N_BABIES_MAX+1)):
            baby = animal_class(x+random.randrange(BABY_DX_MIN, BABY_DX_MAX),
                                y+random.randrange(BABY_DY_MIN, BABY_DY_MAX),
                                BABY_SIZE)
            self.animal_list.append(baby)
            self.baby_list.append(baby)
        self.papa = animal_class(x+PAPA_DX, y+PAPA_DY, ADULT_SIZE)
        self.animal_list.append(self.papa)

    def draw(self):
        for animal in self.animal_list:
            animal.draw()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x < 0:
            self.x = -self.x
            self.dx = random.randrange(10, MOVE_LIMIT)
        elif self.x > window.width:
            self.x = (2 * window.width) - self.x
            self.dx = random.randrange(-MOVE_LIMIT, -10)
        if self.y < 0:
            self.y = -self.y
            self.dy = random.randrange(10, MOVE_LIMIT)
        elif self.y > window.height:
            self.y = (2 * window.height) - self.y
            self.dy = random.randrange(-MOVE_LIMIT, -10)
        self.mama.move(self.x, self.y)
        for baby in self.baby_list:
            baby.move(self.x+random.randrange(BABY_DX_MIN, BABY_DX_MAX),
                      self.y+random.randrange(BABY_DY_MIN, BABY_DY_MAX))
        self.papa.move(self.x+PAPA_DX, self.y+PAPA_DY)


class Flock(AnimalGroup):
    def __init__(self, flyer_class):
        self.flyer_list = []
        for _ in range(FLOCK_SIZE):
            tree = the_forest.random_tree()
            flyer = flyer_class(tree.perch_x(), tree.perch_y(), FLYER_SIZE)
            self.flyer_list.append(flyer)

    def draw(self):
        for flyer in self.flyer_list:
            flyer.draw()

    def move(self):
        for flyer in self.flyer_list:
            tree = the_forest.random_tree()
            flyer.move(tree.perch_x(), tree.perch_y())


class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.batch = pyglet.shapes.Batch()
        self.shape_list = []

    def draw(self):
        self.batch.draw()

    def move(self, x, y):
        dx = x - self.x
        dy = y - self.y
        for shape in self.shape_list:
            shape.x += dx
            shape.y += dy
        self.x = x
        self.y = y


class Bear(Animal):
    def __init__(self, x, y, size):
        super().__init__(x, y)
        body = pyglet.shapes.Ellipse(x, y, size*0.2, size*0.35,
                                     color=pyglet_colors.SIENNA4,
                                     batch=self.batch)
        self.shape_list.append(body)
        leg1 = pyglet.shapes.Ellipse(x-(size*0.13), y-(size*0.3),
                                     size*0.08, size*0.2,
                                     color=pyglet_colors.SIENNA4,
                                     batch=self.batch)
        leg1.rotation = 18.0
        self.shape_list.append(leg1)
        leg2 = pyglet.shapes.Ellipse(x+(size*0.13), y-(size*0.3),
                                     size*0.08, size*0.2,
                                     color=pyglet_colors.SIENNA4,
                                     batch=self.batch)
        leg2.rotation = -18.0
        self.shape_list.append(leg2)
        arm1 = pyglet.shapes.Ellipse(x-(size*0.22), y+(size*0.15),
                                     size*0.05, size*0.13,
                                     color=pyglet_colors.SIENNA4,
                                     batch=self.batch)
        arm1.rotation = 120.0
        self.shape_list.append(arm1)
        arm2 = pyglet.shapes.Ellipse(x+(size*0.22), y+(size*0.15),
                                     size*0.05, size*0.13,
                                     color=pyglet_colors.SIENNA4,
                                     batch=self.batch)
        arm2.rotation = -120.0
        self.shape_list.append(arm2)
        head = pyglet.shapes.Ellipse(x, y+(size*0.35),
                                     size*0.17, size*0.17,
                                     color=pyglet_colors.SIENNA4,
                                     batch=self.batch)
        self.shape_list.append(head)
        ear1 = pyglet.shapes.Circle(x-(size*0.13), y+(size*0.45), size*0.07,
                                    color=pyglet_colors.SIENNA4,
                                    batch=self.batch)
        self.shape_list.append(ear1)
        ear2 = pyglet.shapes.Circle(x+(size*0.13), y+(size*0.45), size*0.07,
                                    color=pyglet_colors.SIENNA4,
                                    batch=self.batch)
        self.shape_list.append(ear2)
        eye1 = pyglet.shapes.Circle(x-(size*0.05), y+(size*0.38), size*0.02,
                                    color=pyglet_colors.WHITE,
                                    batch=self.batch)
        self.shape_list.append(eye1)
        eye2 = pyglet.shapes.Circle(x+(size*0.05), y+(size*0.38), size*0.02,
                                    color=pyglet_colors.WHITE,
                                    batch=self.batch)
        self.shape_list.append(eye2)
        belly = pyglet.shapes.Ellipse(x, y, size*0.10, size*0.21,
                                      color=pyglet_colors.TAN,
                                      batch=self.batch)
        self.shape_list.append(belly)


class Cat(Animal):
    def __init__(self, x, y, size):
        super().__init__(x, y)
        body = pyglet.shapes.Ellipse(x, y, size*0.3, size*0.14,
                                     color=pyglet_colors.DARKORANGE,
                                     batch=self.batch)
        self.shape_list.append(body)
        leg1 = pyglet.shapes.Ellipse(x-(size*0.2), y-(size*0.18),
                                     size*0.03, size*0.16,
                                     color=pyglet_colors.DARKORANGE,
                                     batch=self.batch)
        self.shape_list.append(leg1)
        leg2 = pyglet.shapes.Ellipse(x+(size*0.2), y-(size*0.18),
                                     size*0.03, size*0.16,
                                     color=pyglet_colors.DARKORANGE,
                                     batch=self.batch)
        self.shape_list.append(leg2)
        tail = pyglet.shapes.Ellipse(x+(size*0.24), y+(size*0.16),
                                     size*0.02, size*0.12,
                                     color=pyglet_colors.DARKORANGE,
                                     batch=self.batch)
        self.shape_list.append(tail)
        head = pyglet.shapes.Ellipse(x-(size*0.27), y+(size*0.15),
                                     size*0.14, size*0.14,
                                     color=pyglet_colors.DARKORANGE,
                                     batch=self.batch)
        self.shape_list.append(head)
        ear1 = pyglet.shapes.Triangle(x-(size*0.32), y+(size*0.35),
                                      x-(size*0.37), y+(size*0.25),
                                      x-(size*0.27), y+(size*0.25),
                                      color=pyglet_colors.DARKORANGE,
                                      batch=self.batch)
        self.shape_list.append(ear1)
        ear2 = pyglet.shapes.Triangle(x-(size*0.22), y+(size*0.35),
                                      x-(size*0.27), y+(size*0.25),
                                      x-(size*0.17), y+(size*0.25),
                                      color=pyglet_colors.DARKORANGE,
                                      batch=self.batch)
        self.shape_list.append(ear2)
        eye1 = pyglet.shapes.Circle(x-(size*0.22), y+(size*0.18), size*0.02,
                                    color=pyglet_colors.WHITE,
                                    batch=self.batch)
        self.shape_list.append(eye1)
        eye2 = pyglet.shapes.Circle(x-(size*0.32), y+(size*0.18), size*0.02,
                                    color=pyglet_colors.WHITE,
                                    batch=self.batch)
        self.shape_list.append(eye2)


class Butterfly(Animal):
    def __init__(self, x, y, size):
        super().__init__(x, y)
        self.last_moved = datetime.datetime.now()
        wing1top = pyglet.shapes.Circle(x-(size*0.172), y+(size*0.07),
                                        size*0.16,
                                        color=pyglet_colors.ALICEBLUE,
                                        batch=self.batch)
        self.shape_list.append(wing1top)
        wing1dot = pyglet.shapes.Circle(x-(size*0.172), y+(size*0.07),
                                        size*0.06,
                                        color=pyglet_colors.PINK,
                                        batch=self.batch)
        self.shape_list.append(wing1dot)
        wing1bottom = pyglet.shapes.Circle(x-(size*0.125), y-(size*0.1),
                                           size*0.11,
                                           color=pyglet_colors.ALICEBLUE,
                                           batch=self.batch)
        self.shape_list.append(wing1bottom)
        wing2top = pyglet.shapes.Circle(x+(size*0.172), y+(size*0.07),
                                        size*0.16,
                                        color=pyglet_colors.ALICEBLUE,
                                        batch=self.batch)
        self.shape_list.append(wing2top)
        wing2dot = pyglet.shapes.Circle(x+(size*0.172), y+(size*0.07),
                                        size*0.06,
                                        color=pyglet_colors.PINK,
                                        batch=self.batch)
        self.shape_list.append(wing2dot)
        wing2bottom = pyglet.shapes.Circle(x+(size*0.125), y-(size*0.1),
                                           size*0.11,
                                           color=pyglet_colors.ALICEBLUE,
                                           batch=self.batch)
        self.shape_list.append(wing2bottom)
        body = pyglet.shapes.Ellipse(x, y, size*0.04, size*0.17,
                                     color=pyglet_colors.MISTYROSE1,
                                     batch=self.batch)
        self.shape_list.append(body)

    def move(self, x, y):
        if (datetime.datetime.now() - self.last_moved).seconds >= \
                random.randrange(FLY_WAIT_MIN, FLY_WAIT_MAX):
            super().move(x, y)
            self.last_moved = datetime.datetime.now()


# APPLICATION

class App:
    """ Application class
    """
    def run(self):
        """ Run the application
        """
        global the_forest
        the_forest = Forest()
        the_forest.populate()
        pyglet.clock.schedule_interval(update, 1/3)
        pyglet.app.run()


if __name__ == "__main__":
    app = App()
    app.run()
