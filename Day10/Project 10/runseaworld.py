"""CS 5001 - Project 10 - Into the Sea World - Kaiqi Zhang 28 Nov"""


import pyglet
from pyglet import shapes
from pyglet import gl
import pyglet_colors as pc
import jsonpickle
import random
import datetime


# Constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
WINDOW_MARGIN = 50

# Initializing global variables
window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT,
                              "Into the Sea World")
the_seaworld = None
submarine = None
seaworld_paused = False
config_de = None


# Graphics Functions
@window.event
def on_draw():
    """ Draw event for Pyglet - clear the window and draw stuff"""
    window.clear()
    gl.glClearColor(0.5, 0.7, 1.0, 1.0)
    if the_seaworld is not None:
        the_seaworld.draw()


def update(dt):
    if (not seaworld_paused) and (the_seaworld is not None):
        the_seaworld.move()


@window.event
def on_key_press(symbol, modifiers):
    """This is called by Pyglet when a key is pressed

    Args:
        symbol (pyglet.window.key): The key that is pressed
        modifiers (pyglet.window.key): Modifiers but I don't think they work
    """
    global seaworld_paused
    if symbol == pyglet.window.key.SPACE:
        seaworld_paused = not seaworld_paused


@window.event
def on_mouse_press(x, y, button, modifiers):
    """Move the existing object to the clicked position"""
    submarine.move(x, y)


class App:
    """
    Represents the main application for running the sea world simulation
    """
    def run(self):
        """Run the application"""
        global the_seaworld
        global config_de
        with open("seaworldconfig.json", "r", newline="") as in_file:
            config_en = in_file.read()
            config_de = jsonpickle.decode(config_en)
        the_seaworld = SeaWorld()
        the_seaworld.populate()
        pyglet.clock.schedule_interval(update, 1/2)
        pyglet.app.run()


class Seagrass():
    """Represent seagrass"""

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.shape_list = []
        self.batch = pyglet.shapes.Batch()
        blade1 = shapes.Triangle(x*size, y*size, (x+5)*size, (y+5)*size,
                                 (x-10)*size, y*4*size,
                                 color=pc.GREEN, batch=self.batch)
        self.shape_list.append(blade1)
        blade2 = shapes.Triangle(x, y, x+10, y+10, x+30, y*4,
                                 color=pc.GREEN, batch=self.batch)
        self.shape_list.append(blade2)
        blade3 = shapes.Triangle(x, y, x+5, y+10, x-20, y*3,
                                 color=pc.GREEN, batch=self.batch)
        self.shape_list.append(blade3)
        blade4 = shapes.Triangle(x, y, x+20, y+5, x+50, y*3.5,
                                 color=pc.GREEN, batch=self.batch)
        self.shape_list.append(blade4)

    def draw(self):
        """Draw the seagrass"""
        self.batch.draw()

    def move(self):
        """each single seagrass moves with in a small range"""
        for shape in self.shape_list:
            shape.x += random.randrange(-5, 5)
            shape.y += random.randrange(-5, 5)


class SeaObjects:
    """This is an interface to show the methods that sea Animals,
    seagrassClusters and the Submarine have in common"""
    def move(self):
        pass

    def draw(self):
        pass


class FishFamily(SeaObjects):
    """Represent a random number of fishes of a specificed fish class.
    It also implements SeaObject interface"""
    def __init__(self, x, y, animal_class):
        self.x = x
        self.y = y
        self.dx = random.randrange(-10, 10)
        self.dy = random.randrange(-10, 10)
        self.fish_list = []
        for _ in range(config_de.nfish_min, config_de.nfish_max):
            fish = animal_class(x+random.randrange(50, 500),
                                y+random.randrange(50, 500),
                                size=random.uniform(config_de.fish_size_min,
                                                    config_de.fish_size_max))
            self.fish_list.append(fish)

    def draw(self):
        """draw the fish family"""
        for fish in self.fish_list:
            fish.draw()

    def move(self):
        """All fishes move the same way. Handle bouncing off here"""
        self.x += self.dx
        self.y += self.dy
        if self.x < 0:
            self.x = -self.x
        elif self.x > window.width:
            self.x = (2 * window.width) - self.x
        if self.y < 0:
            self.y = -self.y
        elif self.y > window.height:
            self.y = (2 * window.height) - self.y

        for fish in self.fish_list:
            fish.move(self.x + random.randrange(-500, 500),
                      self.y + random.randrange(-400, 400))


class SeastarFamily(SeaObjects):
    """Represent a group of seastars, which implements SeaObject interface"""
    def __init__(self, x, y, animal_class):
        self.x = x
        self.y = y
        self.seastar_list = []
        for _ in range(config_de.nseastar_min, config_de.nseastar_max):
            random_seagrassCluster = the_seaworld.random_seagrassCluster()
            seastar = animal_class(random_seagrassCluster.rest_x(),
                                   random_seagrassCluster.rest_y(),
                                   size=random.uniform(
                                       config_de.seastar_size_min,
                                       config_de.seastar_size_max))
            self.seastar_list.append(seastar)

    def draw(self):
        """Draw all the seastars"""
        for seastar in self.seastar_list:
            seastar.draw()

    def move(self):
        """Seastars moves to a randomly chosen seagrass"""
        for seastar in self.seastar_list:
            destination_seagrassCluster = the_seaworld.random_seagrassCluster()
            seastar.move(destination_seagrassCluster.rest_x(),
                         destination_seagrassCluster.rest_y())


class SeagrassCluster(SeaObjects):
    """ Class represent a bunch of seagrass spread out in the underwater"""
    def __init__(self, x, y, seagrass_class):
        self.x = x
        self.y = y
        """initialize a random number of seagrass clusters"""
        self.seagrass_list = []
        for _ in range(3):
            seagrass = seagrass_class(random.randint(30, 1000),
                                      random.randint(30, 100),
                                      random.uniform(
                                          config_de.seagrassCluster_size_min,
                                          config_de.seagrassCluster_size_max))
            self.seagrass_list.append(seagrass)

    def draw(self):
        """draw a cluster of seagrass"""
        for seagrass in self.seagrass_list:
            seagrass.draw()

    def move(self):
        """Seagrass moves in slow motion and moves continously"""
        for seagrass in self.seagrass_list:
            seagrass.move()

    def rest_x(self):
        """return the x coordinte of a random spot aound seagrass"""
        return random.randrange(self.x-50, self.x+50)

    def rest_y(self):
        """return the y coordinte of a random spot aound seagrass"""
        return random.randrange(self.y-50, self.y+50)


class SeaAnimal:
    def __init__(self, x, y):
        """Initializing an SeaAnimal object"""
        self.x = x
        self.y = y
        self.batch = pyglet.graphics.Batch()
        self.shape_list = []

    def draw(self):
        """Draw the SeaAnimal using Pyglet graphics"""
        self.batch.draw()

    def move(self, x, y):
        """Move seaAnimal object to a specificed x, y coordinates"""
        dx = x - self.x
        dy = y - self.y
        for shape in self.shape_list:
            shape.x += dx
            shape.y += dy
        self.x = x
        self.y = y


class Seastar(SeaAnimal):
    """Represent a Seastar, a subclass of the SeaAnimal class"""

    def __init__(self, x, y, size):
        """create a seastar shape"""
        super().__init__(x, y)
        self.last_moved = datetime.datetime.now()
        seastar = shapes.Star(x, y, 10*size, 50*size, 5, 0,
                              color=pc.PINK, batch=self.batch)
        self.shape_list.append(seastar)

    def move(self, x, y):
        """Move seastar object based on a random time interval of 4-6s"""
        if (datetime.datetime.now() - self.last_moved).seconds >= \
                random.randrange(4, 6):
            super().move(x, y)
            self.last_moved = datetime.datetime.now()


class Butterflyfish(SeaAnimal):
    """Represent a Butterflyfish, a subclass of the SeaAnimal class"""

    def __init__(self, x, y, size):
        """create a butterflyfish shape"""
        super().__init__(x, y)

        # Draw the body of the butterflyfish
        body = shapes.Triangle(x, y, x+size*40, y-size*30,
                               x+size*40, y+size*30, color=pc.YELLOW1,
                               batch=self.batch)
        self.shape_list.append(body)

        # Draw the tail of the butterflyfish
        tail = shapes.Triangle(x+size*30, y, x+size*50, y-size*10,
                               x+size*50, y+size*10,
                               color=pc.YELLOW1, batch=self.batch)
        self.shape_list.append(tail)

        # Draw the eye of the butterflyfish
        eye = shapes.Circle(x+10, y, 4, color=pc.BLACK, batch=self.batch)
        self.shape_list.append(eye)

        # Draw the white stripe of the butterflyfish
        stripe1 = shapes.Line(x+size*20, y-size*10, x+size*20, y+size*10,
                              size*3, color=pc.WHITE,
                              batch=self.batch)
        stripe2 = shapes.Line(x+size*30, y-size*20, x+size*30, y+size*20,
                              size*4, color=pc.WHITE,
                              batch=self.batch)
        self.shape_list.append(stripe1)
        self.shape_list.append(stripe2)


class Barracuda(SeaAnimal):
    """Represent a Barracuda, a subclass of the SeaAnimal class"""

    def __init__(self, x, y, size):
        super().__init__(x, y)

        # Draw the body of the barracuda
        body = shapes.Ellipse(x, y, size*100, size*15, color=pc.SILVER,
                              batch=self.batch)
        self.shape_list.append(body)

        # Draw the tail of the barracuda
        tail1 = shapes.Triangle(x+size*80, y, x+size*110, y,
                                x+size*120, y+size*20,
                                color=pc.SILVER, batch=self.batch)
        tail2 = shapes.Triangle(x+size*80, y, x+size*110, y,
                                x+size*120, y-size*20,
                                color=pc.SILVER, batch=self.batch)
        self.shape_list.append(tail1)
        self.shape_list.append(tail2)

        # Draw the fin of the barracuda
        fin1 = shapes.Triangle(x-size*40, y+size*5, x-size*20, y+size*5,
                               x, y+size*20,
                               color=pc.SILVER, batch=self.batch)
        fin2 = shapes.Triangle(x+size*20, y+size*5, x+size*40, y+size*5,
                               x+size*60, y+size*20,
                               color=pc.SILVER, batch=self.batch)
        fin3 = shapes.Triangle(x-size*40, y-size*10, x-size*20, y-size*10,
                               x-size*10, y-size*30,
                               color=pc.SILVER, batch=self.batch)
        fin4 = shapes.Triangle(x+size*20, y-size*10, x+size*40, y-size*10,
                               x+size*60, y-size*30,
                               color=pc.SILVER, batch=self.batch)
        self.shape_list.append(fin1)
        self.shape_list.append(fin2)
        self.shape_list.append(fin3)
        self.shape_list.append(fin4)

        # Draw the eye of the barracuda
        eyeframe = shapes.Circle(x-size*80, y, 5,
                                 color=pc.WHITE, batch=self.batch)
        eye = shapes.Circle(x-size*80, y, 2,
                            color=pc.BLACK, batch=self.batch)
        self.shape_list.append(eyeframe)
        self.shape_list.append(eye)

        # Draw the strips of the barracuda
        strip0 = shapes.Line(x-size*60, y+size*5, x+size*70, y+size*5, 1,
                             color=pc.BLACK, batch=self.batch)
        strip1 = shapes.Line(x-size*50, y+size*10, x-size*55, y-size*10, 1,
                             color=pc.BLACK, batch=self.batch)
        strip2 = shapes.Line(x-size*40, y+size*10, x-size*45, y-size*10, 1,
                             color=pc.BLACK, batch=self.batch)
        strip3 = shapes.Line(x-size*30, y+size*10, x-size*35, y-size*10, 1,
                             color=pc.BLACK, batch=self.batch)
        strip4 = shapes.Line(x-size*20, y+size*10, x-size*25, y-size*10, 1,
                             color=pc.BLACK, batch=self.batch)
        strip5 = shapes.Line(x-size*10, y+size*10, x-size*15, y-size*10, 1,
                             color=pc.BLACK, batch=self.batch)
        strip6 = shapes.Line(x, y+size*10, x-size*5, y-10, 1, color=pc.BLACK,
                             batch=self.batch)
        strip7 = shapes.Line(x+size*10, y+size*10, x+size*5, y-size*10, 1,
                             color=pc.BLACK, batch=self.batch)
        strip8 = shapes.Line(x+size*20, y+size*10, x+size*15, y-size*10, 1,
                             color=pc.BLACK, batch=self.batch)
        strip9 = shapes.Line(x+size*30, y+size*10, x+size*25, y-size*10, 1,
                             color=pc.BLACK, batch=self.batch)
        strip10 = shapes.Line(x+size*40, y+size*10, x+size*35, y-size*10, 1,
                              color=pc.BLACK, batch=self.batch)
        self.shape_list.append(strip0)
        self.shape_list.append(strip1)
        self.shape_list.append(strip2)
        self.shape_list.append(strip3)
        self.shape_list.append(strip4)
        self.shape_list.append(strip5)
        self.shape_list.append(strip6)
        self.shape_list.append(strip7)
        self.shape_list.append(strip8)
        self.shape_list.append(strip9)
        self.shape_list.append(strip10)


class Submarine(SeaObjects):
    """Represent a Submarine, which implements SeaObject interface"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape_list = []
        self.batch = pyglet.shapes.Batch()

        cabin = shapes.Ellipse(x, y, 100, 50, color=pc.ORANGE,
                               batch=self.batch)
        self.shape_list.append(cabin)
        top = shapes.Triangle(x-50, y+44, x+50, y+44, x, y+70,
                              color=pc.ORANGE1, batch=self.batch)
        self.shape_list.append(top)
        window1_ext = shapes.Circle(x-50, y, 15, color=pc.ORANGE1,
                                    batch=self.batch)
        self.shape_list.append(window1_ext)
        window1_int = shapes.Circle(x-50, y, 13, color=pc.BLUE,
                                    batch=self.batch)
        self.shape_list.append(window1_int)
        window2_ext = shapes.Circle(x, y, 15, color=pc.ORANGE1,
                                    batch=self.batch)
        self.shape_list.append(window2_ext)
        window2_int = shapes.Circle(x, y, 13, color=pc.BLUE, batch=self.batch)
        self.shape_list.append(window2_int)
        window3_ext = shapes.Circle(x+50, y, 15, color=pc.ORANGE1,
                                    batch=self.batch)
        self.shape_list.append(window3_ext)
        window3_int = shapes.Circle(x+50, y, 13, color=pc.BLUE,
                                    batch=self.batch)
        self.shape_list.append(window3_int)
        flagpole = shapes.Line(x, y+70, x, y+100, color=pc.WHITE,
                               batch=self.batch)
        self.shape_list.append(flagpole)
        flag = shapes.Rectangle(x, y+100, 30, 20, color=pc.BLUE4,
                                batch=self.batch)
        self.shape_list.append(flag)
        front = shapes.Rectangle(x-100, y-20, 8, 40, color=pc.BLUE,
                                 batch=self.batch)
        self.shape_list.append(front)

    def draw(self):
        """Draw the submarine"""
        self.batch.draw()

    def move(self, x, y):
        """Move the submarine"""
        dx = x - self.x
        dy = y - self.y
        for shape in self.shape_list:
            shape.x += dx
            shape.y += dy
        self.x = x
        self.y = y

    def float(self):
        """Submarine floats in the water"""
        dy = random.randrange(-10, 10)
        for shape in self.shape_list:
            shape.y += dy


class SeaWorld:
    """Represents the underwater scene"""
    def __init__(self):
        """Create n seagrassClusters"""
        self.seagrassCluster_list = []
        for _ in range(config_de.nseagrassCluster_min,
                       config_de.nseagrassCluster_max):
            seagrassCluster = SeagrassCluster(random.randrange(30, 1000),
                                              random.randrange(30, 100),
                                              Seagrass)
            self.seagrassCluster_list.append(seagrassCluster)

    def populate(self):
        """populate all other sea objects. Passing in a random location within
        the window frame as the inital x, y """
        global submarine
        submarine = Submarine(random.randrange(WINDOW_MARGIN,
                                               WINDOW_WIDTH - WINDOW_MARGIN),
                              random.randrange(WINDOW_MARGIN,
                                               WINDOW_HEIGHT - WINDOW_MARGIN))
        self.fishgroup_list = []
        fishgroup1 = FishFamily(random.randrange(WINDOW_MARGIN, WINDOW_WIDTH -
                                                 WINDOW_MARGIN),
                                random.randrange(WINDOW_MARGIN, WINDOW_HEIGHT -
                                                 WINDOW_MARGIN),
                                Butterflyfish)
        self.fishgroup_list.append(fishgroup1)
        fishgroup2 = FishFamily(random.randrange(WINDOW_MARGIN, WINDOW_WIDTH -
                                                 WINDOW_MARGIN),
                                random.randrange(WINDOW_MARGIN, WINDOW_HEIGHT -
                                                 WINDOW_MARGIN),
                                Barracuda)
        self.fishgroup_list.append(fishgroup2)
        fishgroup3 = SeastarFamily(random.randrange(WINDOW_MARGIN,
                                                    WINDOW_WIDTH -
                                                    WINDOW_MARGIN),
                                   random.randrange(WINDOW_MARGIN,
                                                    WINDOW_HEIGHT -
                                                    WINDOW_MARGIN),
                                   Seastar)
        self.fishgroup_list.append(fishgroup3)

    def draw(self):
        """draw all the sea objects onto the screen"""
        for seagrasscluster in self.seagrassCluster_list:
            seagrasscluster.draw()
        for fishgroup in self.fishgroup_list:
            fishgroup.draw()
        submarine.draw()

    def move(self):
        """move all the sea objects in their own way"""
        for seagrasscluster in self.seagrassCluster_list:
            seagrasscluster.move()
        for fishgroup in self.fishgroup_list:
            fishgroup.move()
        submarine.float()

    def random_seagrassCluster(self):
        """return a random seagrassCluster"""
        return random.choice(self.seagrassCluster_list)


# Main Program
if __name__ == "__main__":
    app = App()
    app.run()
