# for type checking purposes.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Program import App

# start of code
from customtkinter import CTkButton, CTkFrame
from AppManager import AppManager
from CTkColorPicker import *
from typing import Type

class ColorPickerToggle(CTkButton):
    def __init__(self, parent: Type[CTkFrame], app: App, *args, **kwargs):
        """
        Initializes the Button object.

        Args:
            parent (Navigation): The parent CTkButton object.
            app (App): The MainApp object associated with the button.
            *args: Additional positional arguments to pass to the parent class initializer.
            **kwargs: Additional keyword arguments to pass to the parent class initializer.
        """
        super().__init__(parent, *args, **kwargs)
        self.configure(corner_radius=0, fg_color="orange", text='', width=25, height=25)

        self.app: App = app

    def _clicked(self, event) -> None:
        """
        The click event for the button
        """
        super()._clicked(event)
        pick_color: AskColor = AskColor()

        chosen_color = pick_color.get()
        self.configure(fg_color=chosen_color if chosen_color else "white")

        if not AppManager.selected_shape:
            return

        AppManager.selected_shape.set_new_color_from_hex(chosen_color)