from Simulation.arene import Arene 
import math
from Simulation.robot import Robot 
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Affichage3D() : 

    def __init__(self,arene):
        self.arene=arene