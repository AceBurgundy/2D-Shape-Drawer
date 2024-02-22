# for type checking purposes.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Button import ImageButton
    from Shapes.Shape import Shape

# start of code
from typing import Type

class Manager:

    clicked_button: ImageButton = None
    selected_shape: Type[Shape] = None