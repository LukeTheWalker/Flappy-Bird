from Bird import Bird
from World import World



def setup ():
    fullScreen()
    #size (500,500)
    global mimmo, world, bg
    advance = 5
    bg = loadImage("background.png")
    bg.resize(width, height)
    mimmo = Bird(40, height/2, advance, 0.4)
    world = World(advance, mimmo)


def draw ():
    image(bg, 0,0)
    mimmo.run()
    world.run()


def keyPressed():
    if (key == " "):
        mimmo.jump()
    
