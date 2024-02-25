from typing import override
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

from Shapes.Shape import Shape
from custom_types import *
from constants import *

class Polygon(Shape):
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

    def __init__(self, number_of_sides: int, start_coordinates: COORDINATE, end_coordinates: COORDINATE, border_color: RGB = WHITE, background_color: RGB = WHITE, angle: NUMBER = 0) -> None:
        """
        Initializes a Shape object with the given parameters.

        Args:
            number_of_sides int: The number of sides the polygon has.
            start_coordinates (COORDINATE): The start coordinates of the shape's position.
            end_coordinates (COORDINATE): The end coordinates of the shape's position.
            border_color (RGB): The RGB values of the border color.
            background_color (RGB): The RGB values of the background color.
            angle (NUMBER): The shapes initial angle of rotation.
        """
        super().__init__(start_coordinates, end_coordinates, border_color, background_color, angle)
        self.number_of_sides: int = number_of_sides
        self.padding: int = 10

    def draw(self) -> None:
        """
        Draws a polygon using GL_POLYGON

        Args:
            - self.number_of_sides (int): The number of sides for the polyon. Defaults to 0
        """
        glColor3f(*self.background_color)
        glBegin(GL_POLYGON)
        for index in range(self.number_of_sides):
            angle = 2 * pi * index / self.number_of_sides + pi / -10
            x: NUMBER = self.center_x + self.half_size * cos(angle)
            y: NUMBER = self.center_y + self.half_size * sin(angle)
            glVertex2f(x, y)
        glEnd()

        self.draw_border()

    def draw_border(self) -> None:
        """
        Draws a polygon using GL_LINE_LOOP instead of GL_POLYGON.
        After that, it draws a circle to where each point meet.

        Args:
            - self.number_of_sides (int): The number of sides for the polyon. Defaults to 0
        """
        if not self.selected:
            return

        glColor3f(*self.border_color)

        self.border_endpoints = []

        glBegin(GL_LINE_LOOP)
        for index in range(self.number_of_sides):
            angle: NUMBER = 2 * pi * index / self.number_of_sides + pi / 10
            x: NUMBER = self.center_x + (self.half_size + self.padding) * cos(-angle)
            y: NUMBER = self.center_y + (self.half_size + self.padding) * sin(-angle)
            glVertex2f(x, y)

            endpoint: ENDPOINT = (x, y)
            self.border_endpoints.append(endpoint)
        glEnd()

        # Prevent circle from having dots
        if self.border_endpoints and self.number_of_sides != 100:
            for endpoint in self.border_endpoints:
                self.draw_dot_at(*endpoint)

    @override
    def within_bounds(self, mouse_x: int, mouse_y: int) -> None:
        """
        Checks whether the mouse is inside the polygon.

        Args:
            x (int): The mouse x-coordinate.
            y (int): The mouse y-coordinate.
            self.number_of_sides (int): The number of sides the polygon has.
        """
        vertices: VERTICES = []

        for index in range(self.number_of_sides):
            angle = 2 * pi * index / self.number_of_sides + radians(self.angle)
            x: NUMBER = self.center_x + self.half_size * cos(angle)
            y: NUMBER = self.center_y + self.half_size * sin(angle)
            endpoint: Tuple[NUMBER, NUMBER] = (x, y)
            vertices.append(endpoint)

        crossings: int = 0

        for index in range(self.number_of_sides):
            start_x, start_y = vertices[index]
            end_x, end_y = vertices[(index + 1) % self.number_of_sides]

            if (start_y > mouse_y) != (end_y > mouse_y):
                if mouse_x < (end_x - start_x) * (mouse_y - start_y) / (end_y - start_y) + start_x:
                    crossings += 1

        return crossings % 2 == 1
