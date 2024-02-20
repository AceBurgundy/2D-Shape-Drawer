from Shapes.Shape import Shape
from typing import Type

class Manager:

    clicked_button = None
    selected_shape: Type[Shape] = None