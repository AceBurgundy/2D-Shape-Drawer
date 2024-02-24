from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from typing import List
from math import *

from Shapes.Shape import Shape
from custom_types import *
from constants import *

class Triangle(Shape):
    """
    Represents a triangle shape.
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
        top_vertex: Tuple[float, float] = (self.center_x, self.center_y - self.half_size)
        bottom_left_vertex: Tuple[float, float, float] = (self.center_x - self.half_size, self.center_y + self.half_size)
        bottom_right_vertex: Tuple[float, float, float] = (self.center_x + self.half_size, self.center_y + self.half_size)

        # Calculate the area of the triangle using the determinant formula
        area = 0.5 * abs((bottom_left_vertex[0] - top_vertex[0]) * (bottom_right_vertex[1] - top_vertex[1]) - (bottom_right_vertex[0] - top_vertex[0]) * (bottom_left_vertex[1] - top_vertex[1]))

        # Calculate the weights of each vertex for the given point using the same formula
        weight_top = 0.5 * abs((bottom_left_vertex[0] - mouse_x) * (bottom_right_vertex[1] - mouse_y) - (bottom_right_vertex[0] - mouse_x) * (bottom_left_vertex[1] - mouse_y)) / area
        weight_bottom_left = 0.5 * abs((top_vertex[0] - mouse_x) * (bottom_right_vertex[1] - mouse_y) - (bottom_right_vertex[0] - mouse_x) * (top_vertex[1] - mouse_y)) / area
        weight_bottom_right = 0.5 * abs((top_vertex[0] - mouse_x) * (bottom_left_vertex[1] - mouse_y) - (bottom_left_vertex[0] - mouse_x) * (top_vertex[1] - mouse_y)) / area

        # Check if the weights are all positive and sum to one
        return weight_top > 0 and weight_bottom_left > 0 and weight_bottom_right > 0 and weight_top + weight_bottom_left + weight_bottom_right == 1

    def draw(self) -> None:
        """
        Draws the triangle shape.
        """
        # Draw border lines if selected
        if self.selected:
            border_offset = 15

            # Top line
            glColor3f(*self.border_color)
            glBegin(GL_LINES)
            glVertex2f(self.center_x, self.center_y - self.half_size - border_offset)
            glVertex2f(self.center_x - self.half_size - border_offset, self.center_y + self.half_size - 5 + border_offset)
            glEnd()

            self.border_endpoints.append([
                self.center_x - self.half_size - border_offset, self.center_y + self.half_size - 5 + border_offset
            ])

            # Bottom left line
            glColor3f(*self.border_color)
            glBegin(GL_LINES)
            glVertex2f(self.center_x - self.half_size - 13, self.center_y + self.half_size + border_offset - 6)
            glVertex2f(self.center_x + self.half_size + 13, self.center_y + self.half_size + border_offset - 6)
            glEnd()

            self.border_endpoints.append([
                self.center_x + self.half_size + 13, self.center_y + self.half_size + border_offset - 6
            ])

            # Bottom right line
            glColor3f(*self.border_color)
            glBegin(GL_LINES)
            glVertex2f(self.center_x + self.half_size - 1 + border_offset, self.center_y + self.half_size - 5 + border_offset)
            glVertex2f(self.center_x, self.center_y - self.half_size - border_offset)
            glEnd()

            self.border_endpoints.append([
                self.center_x, self.center_y - self.half_size - border_offset
            ])

            for endpoint in self.border_endpoints:
                self.draw_dot_at(*endpoint)

        # Drawing the triangle
        glColor3f(*self.background_color)
        glBegin(GL_TRIANGLES)

        top_vertex: Tuple[float, float] = (self.center_x, self.center_y - self.half_size)
        bottom_left_vertex: Tuple[float, float, float] = (self.center_x - self.half_size, self.center_y + self.half_size)
        bottom_right_vertex: Tuple[float, float, float] = (self.center_x + self.half_size, self.center_y + self.half_size)

        vertices: List[Tuple] = [
            top_vertex,
            bottom_left_vertex,
            bottom_right_vertex
        ]

        for vertex in vertices:
            glVertex2f(*vertex)

        glEnd()