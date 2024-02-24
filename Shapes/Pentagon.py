from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

from Shapes.Shape import Shape
from custom_types import *
from constants import *

class Pentagon(Shape):
    """
    Represents a pentagon shape.
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
        return super().use_within_polygon_bounds(mouse_x, mouse_y, 5)

    def draw(self) -> None:
        """
        Draws the hexagon shape.
        """
        self.draw_polygon(5)
