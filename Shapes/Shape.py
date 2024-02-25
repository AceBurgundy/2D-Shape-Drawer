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

    def __init__(self, start_coordinates: COORDINATE, end_coordinates: COORDINATE, border_color: RGB = WHITE, background_color: RGB = WHITE, angle: NUMBER = 0) -> None:
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

        self.center_x: NUMBER = (self.start_coordinates[0] + self.end_coordinates[0]) / 2
        self.center_y: NUMBER = (self.start_coordinates[1] + self.end_coordinates[1]) / 2
        self.half_size: NUMBER = min(self.width, self.height) / 2

        # list of endpoints where the tip of each line meet (for creating dots)
        self.border_endpoints: VERTICES = []

    @property
    def width(self) -> NUMBER:
        return abs(self.start_coordinates[0] - self.end_coordinates[0])

    @property
    def height(self) -> NUMBER:
        return abs(self.start_coordinates[1] - self.end_coordinates[1])

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
        # To keep track of rotation
        glPushMatrix() # Save the current matrix
        glTranslatef(self.center_x, self.center_y, 0) # Translate to the center of the shape
        glRotatef(self.angle, 0, 0, 1) # Rotate around the z-axis
        glTranslatef(-self.center_x, -self.center_y, 0) # Translate back to the original position

        self.draw()

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

    def __change_shape(self, increment: bool=True) -> None:
        """
        Increases or decreases the size of the shape by 5 pixels.
        """
        end_x: NUMBER = self.end_coordinates[0]
        end_y: NUMBER = self.end_coordinates[1]

        self.end_coordinates = (
            end_x + 5 if increment else end_x - 5,
            end_y + 5 if increment else end_y - 5
        )

        self.half_size = min(self.width, self.height) / 2

    def increase_shape(self) -> None:
        """
        Increase the size of the shape by 5 pixels.
        """
        self.__change_shape()

    def decrease_shape(self) -> None:
        """
        Decrease the size of the shape by 5 pixels.
        """
        if self.width > 10:
            self.__change_shape(False)

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

    def move_up(self) -> None:
        """
        Moves shape up
        """
        self.center_y -= 10
        return

    def move_down(self) -> None:
        """
        Moves shape down
        """
        self.center_y += 10
        return

    def move_left(self) -> None:
        """
        Moves shape left
        """
        self.center_x -= 10
        return

    def move_right(self) -> None:
        """
        Moves shape right
        """
        self.center_x += 10
        return