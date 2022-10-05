import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import matplotlib.cm
from vectors import *
from math import *
from math_xiaoqi import *

def normal(face):
    return (cross(subtract(face[1],face[0]), subtract(face[2],face[0])))

blues = matplotlib.cm.get_cmap('Blues')

def shade(face, color_map=blues, light=(1,2,3)):
    return color_map(1 - dot(unit(normal(face)), unit(light)))

light = (1,2,3)

faces = [
    [(1,0,0), (0,1,0), (0,0,1)],
    [(1,0,0), (0,0,-1), (0,1,0)],
    [(1,0,0), (0,0,1), (0,-1,0)],
    [(1,0,0), (0,-1,0), (0,0,-1)],
    [(-1,0,0), (0,0,1), (0,1,0)],
    [(-1,0,0), (0,1,0), (0,0,-1)],
    [(-1,0,0), (0,-1,0), (0,0,1)],
    [(-1,0,0), (0,0,-1), (0,-1,0)]
]

pygame.init()
display = (400,400)
window = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)