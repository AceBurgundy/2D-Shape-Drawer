from typing import Type
from Shape import Shape

class Manager:

    clicked_button = None
    selected_shape: Type[Shape] = None