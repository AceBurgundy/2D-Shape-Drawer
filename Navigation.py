# for type checking purposes.

from __future__ import annotations

from typing import TYPE_CHECKING

from Buttons.ColorPickerToggle import ColorPickerToggle

if TYPE_CHECKING:
    from Program import App

# start of code
from Buttons.ImportButton import ImportButton
from Buttons.ExportButton import ExportButton
from Buttons.ShapeButton import ShapeButton
from customtkinter import CTkFrame, CTkButton
from Tutorial import Tutorial
from typing import List
from constants import *

from Shapes.Manager import names

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

        controls_button: CTkButton = CTkButton(self, text="Controls", command=lambda: Tutorial().mainloop(), width=20)
        controls_button.pack(fill="both", padx=DEFAULT_PADDING, pady=TOP_PADDING_ONLY)

        export_button: ExportButton = ExportButton(self, parent.right_content)
        export_button.pack(fill="both", padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

        import_button: ImportButton = ImportButton(self, parent.right_content)
        import_button.pack(fill="both", pady=BOTTOM_PADDING_ONLY, padx=DEFAULT_PADDING)

        container: CTkFrame = CTkFrame(self)
        container.pack(pady=TOP_PADDING_ONLY, padx=3)

        shape_names: List[str] = names()
        index: int = 2

        for shape_name in shape_names:
            container.configure(fg_color="transparent")
            button: ShapeButton = ShapeButton(container, self.parent, shape_name)

            # Creates a new container for the next 2 buttons
            if (index + 1) % 2 != 0:
                button.grid(row=0, column=0)
                index += 1
                continue

            button.grid(row=0, column=1)
            container: CTkFrame = CTkFrame(self)
            container.pack(pady=TOP_PADDING_ONLY, padx=3)
            index += 1

        # Inserting the color picker as the last button
        color_picker: ColorPickerToggle = ColorPickerToggle(container, self.parent)
        color_picker.grid(row=0, column=0)
        container.pack(pady=10, padx=10)

        # Removes the last button container if it doesn't contain any child
        if not container.winfo_children():
            container.destroy()
