" PYGLET DEMO "

import pyglet
import pyglet_colors as pc
import math

# SET UP GLOBAL VARIABLES FOR EVENT HANDLERS

window = pyglet.window.Window(width=600, height=400)
frog_x_increment = 1
frog_y_increment = 3

# EVENT HANDLERS


@window.event
def on_draw():
    """This is called automatically by Pyglet to draw the screen
    """
    global frog_x_increment, frog_y_increment

    # Clear the window
    window.clear()

    # Draw everything
    # label.draw()
    # bezier.draw()
    round_batch.draw()
    # square_batch.draw()
    # line.draw()
    # triangle.draw()
    # star.draw()
    # polygon.draw()
    # frog.draw()

    # Move the frog
    #   move x
    frog.x += frog_x_increment
    #   bounce off of left and right walls
    if frog.x <= 0:
        frog_x_increment = 1
    elif frog.x >= window.width - frog.width:
        frog_x_increment = -1
    #   move y
    frog.y += frog_y_increment
    #   gravity
    frog_y_increment -= 0.1
    #   bounce off of ground
    if frog.y <= 0:
        frog_y_increment = 3


@window.event
def on_key_press(symbol, modifiers):
    """This is called by Pyglet when a key is pressed
    Args:
        symbol (pyglet.window.key): The key that is pressed
        modifiers (pyglet.window.key): Modifiers but I don't think they work
    """
    if symbol == pyglet.window.key.A:
        print('"A"')
    elif symbol == pyglet.window.key.SPACE:
        print('"SPACE"')
        pyglet.app.exit()


@window.event
def on_mouse_press(x, y, button, modifiers):
    """This is called by Pyglet when the mouse is pressed
    Args:
        x (int): Mouse x position
        y (int): Mouse y position
        button (pyglet.window.mouse): The mouse button that is pressed
        modifiers (pyglet.window.key): Modifiers but I don't think they work
    """
    if button == pyglet.window.mouse.LEFT:
        # Circle x,y is the center point
        circle.x = x
        circle.y = y
    elif button == pyglet.window.mouse.RIGHT:
        # Rectangle x,y is lower left corner so we need to calculate center
        rectangle.x = x - (rectangle.width // 2)
        rectangle.y = y - (rectangle.height // 2)


@window.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    """This is called by Pyglet when the mouse is dragged
    Args:
        x (int): Mouse x position
        y (int): Mouse y position
        dx (int): Amount of x movement
        dy (int): Amount of y movement
        button (pyglet.window.mouse): The mouse button that is pressed
        modifiers (pyglet.window.key): Modifiers but I don't think they work
    """
    if button == pyglet.window.mouse.LEFT:
        # Circle x,y is the center point
        circle.x = x
        circle.y = y
    elif button == pyglet.window.mouse.RIGHT:
        # Rectangle x,y is lower left corner so we need to calculate center
        rectangle.x = x - (rectangle.width // 2)
        rectangle.y = y - (rectangle.width // 2)


# Two batches that draw a number of shapes together
round_batch = pyglet.graphics.Batch()
square_batch = pyglet.graphics.Batch()

# Trying every shape in Pyglet
label = pyglet.text.Label("Hello, world", x=window.width//2,
                          y=window.height//2, color=pc.SKYBLUE)
circle = pyglet.shapes.Circle(100, 300, 30, color=pc.RED1,
                              batch=round_batch)
ellipse = pyglet.shapes.Ellipse(250, 300, 60, 30, color=pc.GREEN,
                                batch=round_batch)
sector = pyglet.shapes.Sector(400, 300, 40, angle=math.pi*2/3, start_angle=45,
                              color=pc.LAVENDER, batch=round_batch)
arc = pyglet.shapes.Arc(500, 300, 30, start_angle=45, angle=math.pi*2/3,
                        color=pc.SALMON, batch=round_batch)
line = pyglet.shapes.Line(100, 180, 400, 180, width=3, color=pc.CHARTREUSE1)
bezier = pyglet.shapes.BezierCurve([100, 150], [175, 120], [250, 200],
                                   [325, 120], [400, 150], color=pc.WHITE)
rectangle = pyglet.shapes.Rectangle(100, 50, 50, 80,
                                    color=pc.AQUA, batch=square_batch)
bordered_rectangle = pyglet.shapes.BorderedRectangle(200, 50, 50, 80,
                                                     color=pc.MAGENTA,
                                                     border_color=pc.YELLOW1,
                                                     batch=square_batch)
triangle = pyglet.shapes.Triangle(350, 120, 315, 80, 385, 80,
                                  color=pc.ORANGE)
star = pyglet.shapes.Star(500, 100, 50, 15, num_spikes=12,
                          color=pc.GOLD1)
polygon = pyglet.shapes.Polygon([475, 200], [450, 240], [525, 240], [500, 200],
                                color=pc.PINK)

# A Sprite is an image you display
frog_image = pyglet.image.load("frog.jpg")
frog = pyglet.sprite.Sprite(frog_image, x=0, y=0)
frog.scale = 1/16

# run the app
pyglet.app.run()
