from OpenGL.GLUT import *
from OpenGL.GLU import *
from Shapes import Shape
from OpenGL.GL import *
from math import *

from custom_types import *
from constants import *

class Circle(Shape):
    """
    Represents a circle shape.
    """

    def draw(self) -> None:
        """
        Draws the circle shape.
        """
        center_x = (self.start_coordinates[0] + self.end_coordinates[0]) / 2
        center_y = (self.start_coordinates[1] + self.end_coordinates[1]) / 2
        half_size = min(self.width, self.height) / 2

        # Draw border lines if selected
        if self.selected:
            border_offset = 10
            glColor3f(*self.border_color)

            glBegin(GL_LINE_LOOP)
            for index in range(100):
                angle = 2 * pi * index / 100
                x = center_x + (half_size + border_offset) * cos(angle)
                y = center_y + (half_size + border_offset) * sin(angle)
                glVertex2f(x, y)
            glEnd()

        glColor3f(*self.background_color)
        glBegin(GL_POLYGON)
        for index in range(100):
            angle = 2 * pi * index / 100
            x = center_x + half_size * cos(angle)
            y = center_y + half_size * sin(angle)
            glVertex2f(x, y)
        glEnd()

        glFlush()
