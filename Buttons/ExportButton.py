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

from Save import export_to_file

class ExportButton(CTkButton):

    def __init__(self, master: Navigation, canvas: OpenGLCanvas, width: int|20 = 20, *args, **kwargs):
        super().__init__(master, text="Export", width=width, *args, **kwargs)
        self.canvas: OpenGLCanvas = canvas

        if not canvas:
            raise Exception('OpengGL canvas must be passed as an argument')

    def _clicked(self, event):
        super()._clicked(event)
        shapes: List[Type[Shape]] = self.canvas.shapes

        if export_to_file(shapes):
            CTkToast.toast("Exported Successfully")