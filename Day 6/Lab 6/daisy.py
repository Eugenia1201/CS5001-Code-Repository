import pyglet
import pyglet_colors as pc
import math
import random

class Flower:
    """
    A class to represent a daisy flower.

    Attributes:
    - x (int): The x-coordinate of the flower's base.
    - y (int): The y-coordinate of the flower's base.
    - batch (pyglet.graphics.Batch): A batch for drawing the flower.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.batch = pyglet.graphics.Batch()
        self.shapes = []

        # Create shapes to draw the daisy flower
        # You can customize the flower's appearance here

        # Draw the daisy center (yellow circle)
        self.draw_center()

        # Draw the daisy petals (white circles)
        self.draw_petals()

    def draw_center(self):
        daisy_center = pyglet.shapes.Circle(
            x=self.x, y=self.y,
            radius=20,
            color=pc.WHITE,
            batch=self.batch
        )
        self.shapes.append(daisy_center)

    def draw_petals(self):
        num_petals = 8
        petal_radius = 40

        for angle in range(0, 360, 360 // num_petals):
            petal_x = self.x + petal_radius * math.cos(math.radians(angle))
            petal_y = self.y + petal_radius * math.sin(math.radians(angle))

            petal = pyglet.shapes.Circle(petal_x, petal_y, 20, 
                                         color=pc.YELLOW1, batch=self.batch)

            self.shapes.append(petal)

    def draw(self):
        """
        Draw the daisy flower by calling the draw method of the flower's batch.
        """
        self.batch.draw()

class Garden:
    def __init__(self, number_of_flowers):
        self.flowers = []
        for _ in range(number_of_flowers):
            x = random.randrange(0, 1000)
            y = random.randrange(0, 1000)
            flower = Flower(x, y)
            self.flowers.append(flower)

    def draw(self):
        for flower in self.flowers:
            flower.draw()


class App:
    def __init__(self):
        pass

    def run(self):
        self.window = pyglet.window.Window(width=1000, height=1000)
        self.garden = Garden(20)

        @self.window.event
        def on_draw():
            self.window.clear()
            self.garden.draw()                
        pyglet.app.run()

# MAIN PROGRAM
if __name__ == "__main__":
    app = App()
    app.run()
