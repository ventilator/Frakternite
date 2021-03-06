""" 
Pentigree L-System 
by Geraldine Sarmiento. 

This code was based on Patrick Dwyer's L-System class. 
"""

from l_system import LSystem
from pentigree_l_system import PentigreeLSystem

PUSHES = 2500

def setMaxPushes(pg, pushes):
    pg.transformStack = expand(pg.transformStack, abs(pushes))

def setup():
    setMaxPushes(this.getGraphics(), PUSHES)
    colorMode(HSB, 100)
    size(1000, 500)
    global ps
    ps = PentigreeLSystem()
    ps.simulate(4)
    
    

def draw():
    colorMode(RGB, 255) #discord
    background(32,34,37) #discord
    colorMode(HSB, 100) #discord
    ps.render()
    
def mousePressed():
    save("line.png")   
