from OpenGL.GLUT import *
from OpenGL.GLU import *
from Shapes import Shape
from OpenGL.GL import *
from math import *

from custom_types import *
from constants import *

class Octagon(Shape):
    """
    Represents an octagon shape.
    """

    def draw(self) -> None:
        """
        Draws the octagon shape.
        """
        center_x = (self.start_coordinates[0] + self.end_coordinates[0]) / 2
        center_y = (self.start_coordinates[1] + self.end_coordinates[1]) / 2
        half_size: NUMBER = min(self.width, self.height) / 2

        if self.selected:
            border_offset = 10
            glColor3f(*self.border_color)

            glBegin(GL_LINE_LOOP)
            for index in range(8):
                angle = 2 * pi * index / 8
                x: NUMBER = center_x + (half_size + border_offset) * cos(angle)
                y: NUMBER = center_y + (half_size + border_offset) * sin(angle)
                glVertex2f(x, y)
            glEnd()

        glColor3f(*self.background_color)
        glBegin(GL_POLYGON)
        for index in range(8):
            angle = 2 * pi * index / 8
            x: NUMBER = center_x + half_size * cos(angle)
            y: NUMBER = center_y + half_size * sin(angle)
            glVertex2f(x, y)
        glEnd()

        glFlush()
