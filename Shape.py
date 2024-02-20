from typing import List, Dict, Type, Tuple
from abc import ABC, abstractmethod
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from constants import *
from Types import *
from math import *

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
        start_coordinates (Tuple[NUMBER, NUMBER]): The start coordinates of the shape's position.
        end_coordinates (Tuple[NUMBER, NUMBER]): The end coordinates of the shape's position.
        selected (bool): Flag indicating if the shape is selected.
    """

    canvas_width: NUMBER = 0
    canvas_height: NUMBER = 0

    def __init__(
            self,
            start_coordinates,
            end_coordinates,
            border_color: RGB = WHITE,
            background_color: RGB = WHITE
        ) -> None:
        """
        Initializes a Shape object with the given parameters.

        Args:
            background_color (RGB): The RGB values of the background color.
            border_color (RGB): The RGB values of the border color.
            start_coordinates (Tuple[NUMBER, NUMBER]): The start coordinates of the shape's position.
            end_coordinates (Tuple[NUMBER, NUMBER]): The end coordinates of the shape's position.
        """
        self.background_color: RGB = background_color
        self.border_color: RGB = border_color
        self.selected: bool = False
        self.start_coordinates: Tuple[NUMBER, NUMBER] = start_coordinates
        self.end_coordinates: Tuple[NUMBER, NUMBER] = end_coordinates

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
            border_offset = 15  # Offset for the border

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
            border_offset = 10  # Offset for the border

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

class Pentagon(Shape):
    """
    Represents a pentagon shape.
    """

    def draw(self) -> None:
        """
        Draws the pentagon shape.
        """
        center_x = (self.start_coordinates[0] + self.end_coordinates[0]) / 2
        center_y = (self.start_coordinates[1] + self.end_coordinates[1]) / 2
        half_size: NUMBER = min(self.width, self.height) / 2

        if self.selected:
            border_offset = 10
            glColor3f(*self.border_color)

            glBegin(GL_LINE_LOOP)
            for index in range(5):
                angle = 2 * pi * index / 5 + pi / 10
                x: NUMBER = center_x + (half_size + border_offset) * cos(-angle)
                y: NUMBER = center_y + (half_size + border_offset) * sin(-angle)
                glVertex2f(x, y)
            glEnd()

        glColor3f(*self.background_color)
        glBegin(GL_POLYGON)
        for index in range(5):
            angle = 2 * pi * index / 5 + pi / 10
            x: NUMBER = center_x + half_size * cos(-angle)
            y: NUMBER = center_y + half_size * sin(-angle)
            glVertex2f(x, y)
        glEnd()
        glFlush()

class Hexagon(Shape):
    """
    Represents a hexagon shape.
    """

    def draw(self) -> None:
        """
        Draws the hexagon shape.
        """
        center_x = (self.start_coordinates[0] + self.end_coordinates[0]) / 2
        center_y = (self.start_coordinates[1] + self.end_coordinates[1]) / 2
        half_size: NUMBER = min(self.width, self.height) / 2

        if self.selected:
            border_offset = 10
            glColor3f(*self.border_color)

            glBegin(GL_LINE_LOOP)
            for index in range(6):
                angle = 2 * pi * index / 6
                x: NUMBER = center_x + (half_size + border_offset) * cos(angle)
                y: NUMBER = center_y + (half_size + border_offset) * sin(angle)
                glVertex2f(x, y)
            glEnd()

        glColor3f(*self.background_color)
        glBegin(GL_POLYGON)
        for index in range(6):
            angle = 2 * pi * index / 6
            x: NUMBER = center_x + half_size * cos(angle)
            y: NUMBER = center_y + half_size * sin(angle)
            glVertex2f(x, y)
        glEnd()
        glFlush()

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
