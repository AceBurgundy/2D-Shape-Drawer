from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

from Shapes.Shape import Shape
from custom_types import *
from constants import *

class Square(Shape):
    """
    Represents a square shape.
    """
    def within_bounds(self, mouse_x: int, mouse_y: int) -> bool:
        """
        Checks if the given coordinates are within the bounds of the shape.

        Args:
            mouse_x (int): The x-coordinate of the mouse cursor.
            mouse_y (int): The y-coordinate of the mouse cursor.

        Returns:
            bool: True if the coordinates are within the bounds of the shape, False otherwise.
        """
        # Get the minimum and maximum values of the x and y coordinates of the square
        min_x = min(self.start_coordinates[0], self.end_coordinates[0])
        max_x = max(self.start_coordinates[0], self.end_coordinates[0])
        min_y = min(self.start_coordinates[1], self.end_coordinates[1])
        max_y = max(self.start_coordinates[1], self.end_coordinates[1])

        # Check if the point is within the range of the x and y coordinates of the square
        return min_x <= mouse_x <= max_x and min_y <= mouse_y <= max_y

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

            self.border_endpoints.append([self.end_coordinates[0] + border_offset, self.start_coordinates[1] - border_offset])

            # Right border line
            glBegin(GL_LINES)
            glVertex2f(self.end_coordinates[0] + border_offset, self.start_coordinates[1] - border_offset)
            glVertex2f(self.end_coordinates[0] + border_offset, self.end_coordinates[1] + border_offset)
            glEnd()

            self.border_endpoints.append([self.end_coordinates[0] + border_offset, self.end_coordinates[1] + border_offset])

            # Bottom border line
            glBegin(GL_LINES)
            glVertex2f(self.end_coordinates[0] + border_offset, self.end_coordinates[1] + border_offset)
            glVertex2f(self.start_coordinates[0] - border_offset, self.end_coordinates[1] + border_offset)
            glEnd()

            self.border_endpoints.append([self.start_coordinates[0] - border_offset, self.end_coordinates[1] + border_offset])

            # Left border line
            glBegin(GL_LINES)
            glVertex2f(self.start_coordinates[0] - border_offset, self.end_coordinates[1] + border_offset)
            glVertex2f(self.start_coordinates[0] - border_offset, self.start_coordinates[1] - border_offset)
            glEnd()

            self.border_endpoints.append([self.start_coordinates[0] - border_offset, self.start_coordinates[1] - border_offset])

            for endpoint in self.border_endpoints:
                self.draw_dot_at(*endpoint)