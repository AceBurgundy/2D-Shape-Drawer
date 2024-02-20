from typing import List, Dict, Type, Tuple
from abc import ABC, abstractmethod
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

from custom_types import *
from constants import *

class Shape(ABC):
    """
    Abstract base class representing a geometric shape.

    Attributes:
        static_field canvas_width (NUMBER): the width of the canvas
        static_field canvas_height (NUMBER): the height of the canvas
        background_color (RGB): The RGB values of the background color.
        border_color (RGB): The RGB values of the border color.
        width (NUMBER): The width of the shape.
        height (NUMBER): The height of the shape.
        start_coordinates (COORDINATE): The start coordinates of the shape's position.
        end_coordinates (COORDINATE): The end coordinates of the shape's position.
        selected (bool): Flag indicating if the shape is selected.
    """

    canvas_width: NUMBER = 0
    canvas_height: NUMBER = 0

    def __init__(
            self,
            start_coordinates: COORDINATE,
            end_coordinates: COORDINATE,
            border_color: RGB = WHITE,
            background_color: RGB = WHITE
        ) -> None:
        """
        Initializes a Shape object with the given parameters.

        Args:
            background_color (RGB): The RGB values of the background color.
            border_color (RGB): The RGB values of the border color.
            start_coordinates (COORDINATE): The start coordinates of the shape's position.
            end_coordinates (COORDINATE): The end coordinates of the shape's position.
        """
        self.background_color: RGB = background_color
        self.border_color: RGB = border_color
        self.selected: bool = False
        self.start_coordinates: COORDINATE = start_coordinates
        self.end_coordinates: COORDINATE = end_coordinates

    @property
    def width(self) -> NUMBER:
        return abs(self.start_coordinates[0] - self.end_coordinates[0])

    @property
    def height(self) -> NUMBER:
        return abs(self.start_coordinates[1] - self.end_coordinates[1])

    @abstractmethod
    def draw(self) -> None:
        """
        Abstract method to draw the shape.
        """
        pass

    def within_bounds(self, mouse_x: int, mouse_y: int) -> bool:
        """
        Checks if the given coordinates are within the bounds of the shape.

        Args:
            mouse_x (int): The x-coordinate of the mouse cursor.
            mouse_y (int): The y-coordinate of the mouse cursor.

        Returns:
            bool: True if the coordinates are within the bounds of the shape, False otherwise.
        """
        inside_width: bool = self.start_coordinates[0] <= mouse_x <= self.end_coordinates[0]
        inside_height: bool = self.start_coordinates[1] <= mouse_y <= self.end_coordinates[1]
        return inside_width and inside_height

    @staticmethod
    def names() -> List[str]:
        """
        Static method to get the class names of all subclasses of Shape.

        Returns:
            List[str]: List of class names of all subclasses of Shape.
        """
        shape_names = Shape.shapes()
        return list(shape_names)

    @staticmethod
    def shapes() -> Dict[str, Type['Shape']]:
        """
        Static method to get the class names and class objects of all subclasses of Shape.

        Returns:
            Dict[str, Type['Shape']]: Dictionary mapping class names to class objects of all subclasses of Shape.
        """
        return {subclass.__name__: subclass for subclass in Shape.__subclasses__()}
