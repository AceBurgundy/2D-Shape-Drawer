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
            background_color: RGB = WHITE,
            angle: NUMBER = 0
        ) -> None:
        """
        Initializes a Shape object with the given parameters.

        Args:
            background_color (RGB): The RGB values of the background color.
            border_color (RGB): The RGB values of the border color.
            angle (NUMBER): The shapes initial angle of rotation.
            start_coordinates (COORDINATE): The start coordinates of the shape's position.
            end_coordinates (COORDINATE): The end coordinates of the shape's position.
        """
        self.background_color: RGB = background_color
        self.border_color: RGB = border_color
        self.selected: bool = False
        self.start_coordinates: COORDINATE = start_coordinates
        self.end_coordinates: COORDINATE = end_coordinates
        self.angle: NUMBER = angle

        self.center_x = (self.start_coordinates[0] + self.end_coordinates[0]) / 2
        self.center_y = (self.start_coordinates[1] + self.end_coordinates[1]) / 2
        self.half_size: NUMBER = min(self.width, self.height) / 2

        # list of endpoints where the tip of each line meet (for border)
        self.border_endpoints: VERTICES = []

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

    def draw_to_canvas(self) -> None:
        """
        Draws shape into the canvas while containing it into a rotation algorithm
        """
        glPushMatrix() # Save the current matrix
        glTranslatef(self.center_x, self.center_y, 0) # Translate to the center of the hexagon
        glRotatef(self.angle, 0, 0, 1) # Rotate around the z-axis
        glTranslatef(-self.center_x, -self.center_y, 0) # Translate back to the original position

        self.draw()

        # clear border_endpoints list after its being drawn
        self.border_endpoints = []

        glPopMatrix()
        glFlush()

    @abstractmethod
    def within_bounds(self, mouse_x: int, mouse_y: int) -> bool:
        """
        Checks if the given coordinates are within the bounds of the shape.

        Args:
            mouse_x (int): The x-coordinate of the mouse cursor.
            mouse_y (int): The y-coordinate of the mouse cursor.

        Returns:
            bool: True if the coordinates are within the bounds of the shape, False otherwise.
        """
        pass

    def increase_shape(self) -> None:
        """
        Increase the size of the shape by 5 pixels.
        """
        self.end_coordinates = (
            self.end_coordinates[0] + 5,
            self.end_coordinates[1] + 5
        )

    def decrease_shape(self) -> None:
        """
        Decrease the size of the shape by 5 pixels.
        """
        self.end_coordinates = (
            self.end_coordinates[0] - 5,
            self.end_coordinates[1] - 5
        )

    def rotate_left(self) -> None:
        """
        Rotates the hexagon left by 10 degrees.
        """
        self.angle -= 1

    def rotate_right(self) -> None:
        """
        Rotates the hexagon right by 10 degrees.
        """
        self.angle += 1

    def set_new_color_from_hex(self, hex_color: str) -> Tuple:
        """
        Convert a hexadecimal color string to RGB floats.

        Args:
            hex_color (str): The hexadecimal color string (e.g., "#051dff").

        Returns:
            Tuple: A Tuple of RGB floats in the range [0.0, 1.0] representing the color.
        """
        # Remove '#' from the beginning if present
        hex_color = hex_color.lstrip('#')

        # Convert hexadecimal to RGB
        rgb: Tuple[int] = tuple(int(hex_color[index: index + 2], 16) / 255.0 for index in (0, 2, 4))

        self.background_color = rgb

    def move(self, mouse_x: int, mouse_y: int) -> None:
        """
        Moves the shape along with the mouse
        """
        x_distance: NUMBER = abs(self.center_x - mouse_x)
        y_distance: NUMBER = abs(self.center_y - mouse_y)

        self.center_x = x_distance
        self.center_y = y_distance

    def move_up(self) -> None:
        """
        Moves shape up
        """
        self.center_y -= 1
        return

    def move_down(self) -> None:
        """
        Moves shape down
        """
        self.center_y += 1
        return

    def move_left(self) -> None:
        """
        Moves shape left
        """
        self.center_x -= 1
        return

    def move_right(self) -> None:
        """
        Moves shape right
        """
        self.center_x += 1
        return