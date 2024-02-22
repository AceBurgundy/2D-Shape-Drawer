# for type checking purposes.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Program import App

# start of code
from customtkinter import CTkFrame
from Shapes.Shape import Shape
from Button import ImageButton
from os import listdir, path
from typing import List

class Navigation(CTkFrame):
    def __init__(self, parent: App, **kwargs):
        """
        Initializes the Navigation object.

        Args:
            parent (App): The parent CTk object.
            **kwargs: Additional keyword arguments to pass to the parent class initializer.
        """
        super().__init__(parent, **kwargs)
        self.parent: App = parent

        button_box: CTkFrame = CTkFrame(self)
        button_box.pack(pady=(5, 0), padx=3)

        exemptions: List[str] = ["__pycache__", "Shape.py", "__init__.py"]
        file_names: List[str] = []

        for file_name in listdir('Shapes'):
            file_path: str = path.join('Shapes', file_name)
            if file_name not in exemptions and path.isfile(file_path):
                clean_name: str = file_name.lower().replace('.py', '')
                file_names.append(clean_name)

        for index, shape_name in enumerate(file_names):
            button_box.configure(fg_color="transparent")
            button: ImageButton = ImageButton(button_box, self.parent, shape_name)

            # Creates a new button_box for the next 2 buttons
            if (index + 1) % 2 != 0:
                button.grid(row=0, column=0)
                continue

            button.grid(row=0, column=1)
            button_box: CTkFrame = CTkFrame(self)
            button_box.pack(pady=(5, 0), padx=3)

        # Removes the last button container if it doesn't contain any child
        if not button_box.winfo_children():
            button_box.destroy()
