from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

from Shapes.Polygon import Polygon
from custom_types import *
from constants import *

class Square(Polygon):
    """
    Represents an square shape.
    """
    def __init__(self, start_coordinates: COORDINATE, end_coordinates: COORDINATE):
        super().__init__(4, start_coordinates, end_coordinates)

