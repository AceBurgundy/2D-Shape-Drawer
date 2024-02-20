from OpenGL.GLUT import *
from OpenGL.GLU import *
from Shapes import Shape
from OpenGL.GL import *
from math import *

from custom_types import *
from constants import *

class Triangle(Shape):
    """
    Represents a triangle shape.
    """

    def draw(self) -> None:
        """
        Draws the triangle shape.
        """
        center_x = (self.start_coordinates[0] + self.end_coordinates[0]) / 2
        center_y = (self.start_coordinates[1] + self.end_coordinates[1]) / 2
        half_size = min(self.width, self.height) / 2

        # Draw border lines if selected
        if self.selected:
            border_offset = 15

            # Top line
            glColor3f(*self.border_color)
            glBegin(GL_LINES)
            glVertex2f(center_x, center_y - half_size - border_offset)
            glVertex2f(center_x - half_size - border_offset, center_y + half_size - 5 + border_offset)
            glEnd()

            # Bottom left line
            glColor3f(*self.border_color)
            glBegin(GL_LINES)
            glVertex2f(center_x - half_size - 13, center_y + half_size + border_offset - 6)
            glVertex2f(center_x + half_size + 13, center_y + half_size + border_offset - 6)
            glEnd()

            # Bottom right line
            glColor3f(*self.border_color)
            glBegin(GL_LINES)
            glVertex2f(center_x + half_size - 1 + border_offset, center_y + half_size - 5 + border_offset)
            glVertex2f(center_x, center_y - half_size - border_offset)
            glEnd()

        glColor3f(*self.background_color)
        glBegin(GL_TRIANGLES)
        glVertex2f(center_x, center_y - half_size)  # Top vertex
        glVertex2f(center_x - half_size, center_y + half_size)  # Bottom left vertex
        glVertex2f(center_x + half_size, center_y + half_size)  # Bottom right vertex
        glEnd()
