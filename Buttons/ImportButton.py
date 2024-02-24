# for type checking purposes.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Navigation import Navigation
    from Canvas import OpenGLCanvas

from customtkinter import CTkButton
from Shapes.Shape import Shape
from typing import List, Type
from CTkToast import CTkToast

from Save import import_from_file

class ImportButton(CTkButton):

    def __init__(self, master: Navigation, canvas: OpenGLCanvas, width: int|20 = 20, *args, **kwargs):
        super().__init__(master, text="Import", width=width, *args, **kwargs)
        self.canvas: OpenGLCanvas = canvas

        if not canvas:
            raise Exception('OpengGL canvas must be passed as an argument')

    def _clicked(self, event):
        super()._clicked(event)

        shapes: List[Type[Shape]] = import_from_file()

        if shapes is None:
            return

        all_are_shapes: List[bool] = all(issubclass(type(shape), Shape) for shape in shapes)

        if not all_are_shapes:
            CTkToast.toast('Some data or all data imported are not shapes')
            return

        self.canvas.shapes = shapes
        CTkToast.toast("Imported Successfully")
        return
