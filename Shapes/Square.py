from OpenGL.GLUT import *
from OpenGL.GLU import *
from Shapes import Shape
from OpenGL.GL import *
from math import *

from custom_types import *
from constants import *

class Square(Shape):
    """
    Represents a square shape.
    """

    def draw(self) -> None:
        """
        Draws the square shape.
        """
        glColor3f(*self.background_color)
        glBegin(GL_QUADS)
        glVertex2f(self.start_coordinates[0], self.start_coordinates[1])
        glVertex2f(self.end_coordinates[0], self.start_coordinates[1])
        glVertex2f(self.end_coordinates[0], self.end_coordinates[1])
        glVertex2f(self.start_coordinates[0], self.end_coordinates[1])
        glEnd()

        # Draw border lines if selected
        if self.selected:
            border_offset = 10

            glColor3f(*self.border_color)

            # Top border line
            glBegin(GL_LINES)
            glVertex2f(self.start_coordinates[0] - border_offset, self.start_coordinates[1] - border_offset)
            glVertex2f(self.end_coordinates[0] + border_offset, self.start_coordinates[1] - border_offset)
            glEnd()

            # Right border line
            glBegin(GL_LINES)
            glVertex2f(self.end_coordinates[0] + border_offset, self.start_coordinates[1] - border_offset)
            glVertex2f(self.end_coordinates[0] + border_offset, self.end_coordinates[1] + border_offset)
            glEnd()

            # Bottom border line
            glBegin(GL_LINES)
            glVertex2f(self.end_coordinates[0] + border_offset, self.end_coordinates[1] + border_offset)
            glVertex2f(self.start_coordinates[0] - border_offset, self.end_coordinates[1] + border_offset)
            glEnd()

            # Left border line
            glBegin(GL_LINES)
            glVertex2f(self.start_coordinates[0] - border_offset, self.end_coordinates[1] + border_offset)
            glVertex2f(self.start_coordinates[0] - border_offset, self.start_coordinates[1] - border_offset)
            glEnd()

        glFlush()
