from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

from Shapes.Shape import Shape
from custom_types import *
from constants import *

class Circle(Shape):
    """
    Represents a circle shape.
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
        # Calculate the distance between the point and the center using the distance formula
        distance = sqrt((mouse_x - self.center_x) ** 2 + (mouse_y - self.center_y) ** 2)

        # Check if the distance is less than or equal to the radius
        return distance <= self.half_size

    def draw(self) -> None:
        """
        Draws the circle shape.
        """
        self.draw_polygon(100)
