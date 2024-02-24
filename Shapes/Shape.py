from typing import List, Dict, Type
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

    def draw_polygon(self, number_of_sides: int = 0) -> None:
        """
        Draws a polygon using GL_POLYGON

        Args:
            - number_of_sides (int): The number of sides for the polyon. Defaults to 0
        """
        glColor3f(*self.background_color)
        glBegin(GL_POLYGON)
        for index in range(number_of_sides):
            angle = 2 * pi * index / number_of_sides + pi / -10
            x: NUMBER = self.center_x + self.half_size * cos(angle)
            y: NUMBER = self.center_y + self.half_size * sin(angle)
            glVertex2f(x, y)
        glEnd()

        if self.selected:
            self.draw_polygon_lines(number_of_sides)

        return

    def draw_polygon_lines(self, number_of_sides: int = 0, padding: int = 10) -> None:
        """
        Draws a polygon using GL_LINE_LOOP instead of GL_POLYGON.
        After that, it draws a circle to where each point meet.

        Args:
            - number_of_sides (int): The number of sides for the polyon. Defaults to 0
        """
        glColor3f(*self.border_color)

        glBegin(GL_LINE_LOOP)
        for index in range(number_of_sides):
            angle = 2 * pi * index / number_of_sides + pi / 10
            x: NUMBER = self.center_x + (self.half_size + padding) * cos(-angle)
            y: NUMBER = self.center_y + (self.half_size + padding) * sin(-angle)
            endpoint: ENDPOINT = (x, y)

            # Prevent circle from having dots
            if number_of_sides < 100:
                self.border_endpoints.append(endpoint)

            glVertex2f(x, y)
        glEnd()

        if self.border_endpoints:
            for endpoint in self.border_endpoints:
                self.draw_dot_at(*endpoint)

    def draw_dot_at(self, x, y) -> None:
        """
        Draw a circle at the specified (x, y) coordinate.

        Args:
            x (int, int): The x-coordinate of the center of the circle.
            y (int, int): The y-coordinate of the center of the circle.
        """
        num_segments: int = 100
        radius: int = 4

        glBegin(GL_POLYGON)
        glColor3f(*self.background_color)
        for index in range(num_segments):
            theta = 2.0 * 3.1415926 * index / num_segments
            glVertex2f(x + radius * cos(theta), y + radius * sin(theta))
        glEnd()

    def use_within_polygon_bounds(self, mouse_x: int, mouse_y: int, number_of_sides: int = 0) -> None:
        """
        Checks whether the mouse is inside the polygon.

        Args:
            x (int): The mouse x-coordinate.
            y (int): The mouse y-coordinate.
        """
        # Get the vertices of the polygon
        vertices: VERTICES = []

        for index in range(number_of_sides):
            angle = 2 * pi * index / number_of_sides + radians(self.angle)
            x: NUMBER = self.center_x + self.half_size * cos(angle)
            y: NUMBER = self.center_y + self.half_size * sin(angle)
            endpoint: Tuple[NUMBER, NUMBER] = (x, y)
            vertices.append(endpoint)

        # Initialize the number of crossings to zero
        crossings: int = 0

        # Loop through each edge of the polygon
        for index in range(number_of_sides):
            # Get the start and end points of the edge
            start_x, start_y = vertices[index]
            end_x, end_y = vertices[(index + 1) % number_of_sides]

            # Check if the ray crosses the edge
            if (start_y > mouse_y) != (end_y > mouse_y): # The edge is not horizontal
                if mouse_x < (end_x - start_x) * (mouse_y - start_y) / (end_y - start_y) + start_x: # The ray is to the left of the edge
                    crossings += 1 # Increment the number of crossings

        # Check if the number of crossings is odd or even
        return crossings % 2 == 1

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
