"""CS 5001 - Kaiqi Zhang - Project 6 'The Forest Awakens' - Extension 1 - 26 Oct
"""

import pyglet
import pyglet_colors as pc
import math
import random
import time

window = pyglet.window.Window(width=1000, height=1000)
pause = False

class Tree:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
        self.batch = pyglet.graphics.Batch()
    
        # Draw the leaves (a triangle)
        self.leaves1 = pyglet.shapes.Triangle(self.x*self.size, self.y*self.size, (self.x+50)*self.size, 
                                              (self.y+200)*self.size, (self.x+100)*self.size, 
                                              self.y*self.size, color=pc.GREEN, batch=self.batch)
        # Draw the trunk (a rectangle)
        self.trunk = pyglet.shapes.Rectangle((self.x+45)*self.size, (self.y-100)*self.size, 10*self.size, 
                                             100*self.size, color=(222, 184, 135, 255), batch=self.batch)

    def draw(self):
        self.batch.draw()


class Animal:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
        self.cat = pyglet.graphics.Batch()
        self.shapes = []

         # Draw the cat's head (a circle)
        head = pyglet.shapes.Circle(self.x*size,self.y*size ,38*size, color=pc.GRAY, batch=self.cat)
        self.shapes.append(head)

        # Draw the cat's eyes (two circles)
        l_eye = pyglet.shapes.Circle((self.x-15)*size, (self.y+10)*size, 7*size, color=pc.BLUE, batch = self.cat)
        self.shapes.append(l_eye)
        r_eye = pyglet.shapes.Circle((self.x+15)*size, (self.y+10)*size, 7*size, color=pc.BLUE, batch = self.cat)
        self.shapes.append(r_eye)

        # Draw the cat's nose (a small pink ellipse)
        nose = pyglet.shapes.Ellipse((self.x)*size, (self.y-10)*size, 4*size, 2*size, color=pc.BLUE2, batch = self.cat)
        self.shapes.append(nose)

        # Draw the cat's mouth (a curve)
        mouth = pyglet.shapes.Arc((self.x)*size, (self.y-20)*size, 10*size, start_angle=180, angle=math.pi*2/3,color=pc.BLACK, batch = self.cat)
        self.shapes.append(mouth)

        # Draw the cat's ears (two triangles)
        l_ear = pyglet.shapes.Triangle((self.x-30)*size, (self.y+10)*size, (self.x-35)*size, (self.y+45)*size, (self.x-10)*size, (self.y+30)*size, color=pc.GRAY, batch = self.cat)
        r_ear = pyglet.shapes.Triangle((self.x+10)*size, (self.y+30)*size, (self.x+35)*size, (self.y+45)*size, (self.x+30)*size, (self.y+10)*size, color=pc.GRAY, batch = self.cat) 
        self.shapes.append(l_ear)
        self.shapes.append(r_ear)

        # Draw the cat's body (an ellipse)
        body = pyglet.shapes.Ellipse(self.x*size, (self.y-100)*size, 40*size, 70*size, color=pc.GRAY, batch = self.cat)
        self.shapes.append(body)

        # Draw the cat's feet (an sector)
        l_foot = pyglet.shapes.Sector((self.x-17)*size, (self.y-160)*size, 20*size, start_angle=53, angle=math.pi*2/3, color=pc.GRAY, batch = self.cat)
        r_foot = pyglet.shapes.Sector((self.x+17)*size, (self.y-160)*size, 20*size, start_angle=55, angle=math.pi*2/3, color=pc.GRAY, batch = self.cat)
        self.shapes.append(l_foot)
        self.shapes.append(r_foot)


    def draw(self):
        self.cat.draw()

    def move(self,new_x,new_y):
        dx=new_x - self.x
        dy=new_y - self.y
        for shape in self.shapes:
            shape.x += dx
            shape.y += dy
        self.x=new_x
        self.y=new_y

class Family:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.mama = Animal(self.x,self.y,1)
        self.papa = Animal(self.x+70,self.y-60,1.2)
        self.kids = []
        num_kids = random.randint(3,5)
        for x in range(num_kids):
            kid = Animal(self.x+random.uniform(-10.0,10.0),self.y+random.uniform(-10.0,10.0),
                         size=random.uniform(0.3,0.5))
            self.kids.append(kid)

    def draw(self):
        self.mama.draw()
        self.papa.draw()
        for kid in self.kids:
            kid.draw()

    def move(self):
        # make random movement for mama
        new_x = self.mama.x + random.randrange(-100,100)
        new_y = self.mama.y + random.randrange(-100,100)

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
            kid_new_x = self.mama_new_x + random.randint(150,400)
            kid_new_y = self.mama_new_y + random.randint(150,400)
            kid.move(kid_new_x,kid_new_y)
     
class Bee:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.bee = pyglet.graphics.Batch()
    
        # Body of the bee (an ellipse)
        self.body = pyglet.shapes.Ellipse(self.x, self.y, 50, 25, color=pc.YELLOW1, batch=self.bee)

        # Head of the bee (a smaller ellipse)
        self.head = pyglet.shapes.Circle(self.x+50,self.y, 25, color=pc.YELLOW2, batch=self.bee)

        # Eyes of the bee (two circles)
        self.eye1 = pyglet.shapes.Circle(self.x+65, self.y+15, 8, color=pc.BLACK, batch=self.bee)
        self.eye2 = pyglet.shapes.Circle(self.x+65, self.y-10, 8, color=pc.BLACK, batch=self.bee)

        # Wings of the bee (two rectangles)
        self.wing1 = pyglet.shapes.Ellipse(self.x, self.y, 8, 40, color=pc.YELLOW4, batch=self.bee)
        self.wing2 = pyglet.shapes.Ellipse(self.x-20, self.y, 8, 40, color=pc.YELLOW4, batch=self.bee)
        self.wing3 = pyglet.shapes.Ellipse(self.x+20, self.y, 8, 40, color=pc.YELLOW4, batch=self.bee)

    def draw(self):
        self.bee.draw()

    def move(self,new_x,new_y):
        dx = new_x - self.x
        dy = new_y - self.y
        self.x += dx
        self.y += dy
        self.x = new_x
        self.y = new_y

class FlyingBee:
    def __init__(self, forest):
        self.forest = forest
        self.tree = random.choice(self.forest.trees)  # Select a random tree
        self.x = self.tree.x
        self.y = self.tree.y
        self.bee = Bee(self.x, self.y)
        
        self.stay_duration = 2  # Number of seconds to stay at each tree
        self.time_at_tree = time.time()  # Record the time when the object arrived at the current tree
        
    def draw(self):
        self.bee.draw()

    def move(self):
        self.current_time = time.time()  
 
        # Record the time when the object arrived at the current tree
        if self.current_time - self.time_at_tree >= self.stay_duration:
           # Time to move to a new tree
            new_tree = random.choice(self.forest.trees)
            self.tree = new_tree
            self.bee.move(self.tree.x,self.tree.y)
            self.time_at_tree = self.current_time     


class Forest:
    def __init__(self):
        self.trees = []
        self.families = []
        
        for _ in range(12):
            tree = Tree(x=random.randint(10,window.width-200), y=random.randint(200, window.height-250),
                        size=random.uniform(0.7, 1.2))
            self.trees.append(tree)
        
        family1 = Family(x=random.randint(100,window.width//2), y=random.randint(200, window.height-300))
        self.families.append(family1)
        family2 = Family(x=random.randint(window.width//2,window.width-400), y=random.randint(200, window.height-300))
        self.families.append(family2)

    def draw(self):
        for tree in self.trees:
            tree.draw()

        for family in self.families:
            family.draw()

    def move(self,dx,dy):
        self.dx = dx
        self.dy = dy

        for family in self.families:
            family.move(dx, dy) 

forest = Forest()
flying_bee = FlyingBee(forest)

@window.event
def on_draw():
    window.clear()
    forest.draw()
    flying_bee.draw()
def update(self):
    if not pause:
        forest.move()
        flying_bee.move()
        
@window.event
def on_key_press(symbol, modifiers):
    global pause
    if symbol == pyglet.window.key.SPACE:
        pause = not pause

        
pyglet.clock.schedule_interval(update, 1/3)
pyglet.app.run()

# class App:
#     def __init__(self):
#         pass

#     def run(self):
#         forest = Forest()
#         flying_bee = FlyingBee(forest)


#         @window.event
#         def on_draw():
#             window.clear()
#             forest.draw()
#             flying_bee.draw()
 

        
#         def update(self):
#             if not pause:
#                 forest.move(10,10)
#                 flying_bee.move()

#         @window.event
#         def on_key_press(symbol, modifiers):
#             global pause
#             if symbol == pyglet.window.key.SPACE:
#                 pause = not pause

#         pyglet.clock.schedule_interval(update, 1/3)
#         pyglet.app.run()

# # MAIN PROGRAM
# if __name__ == "__main__":
#     app = App()
#     app.run()