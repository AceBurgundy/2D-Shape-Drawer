from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

from Shapes.Polygon import Polygon
from custom_types import *
from constants import *

class Octagon(Polygon):
    """
    Represents an octagon shape.
    """
    def __init__(self, start_coordinates: COORDINATE, end_coordinates: COORDINATE):
        super().__init__(8, start_coordinates, end_coordinates)

