# for type checking purposes.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Buttons.ShapeButton import ShapeButton
    from Shapes.Shape import Shape

# start of code
from typing import Type

class Global:

    clicked_button: ShapeButton = None
    shape: Type[Shape] = None