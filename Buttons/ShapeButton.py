# for type checking purposes.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Navigation import Navigation
    from Program import App

# start of code
from Buttons.ImageButton import ImageButton
from AppManager import AppManager

class ShapeButton(ImageButton):
    def __init__(self, parent: Navigation, app: App, shape_name: str, *args, **kwargs):
        """
        Initializes the Shape Button object.

        Args:
            parent (Navigation): The parent CTkFrame object.
            app (App): The MainApp object associated with the button.
            shape_name (str): The str representing the shape draw method.
            *args: Additional positional arguments to pass to the parent class initializer.
            **kwargs: Additional keyword arguments to pass to the parent class initializer.
        """
        super().__init__(parent, app, shape_name, *args, **kwargs)
        self.shape_name = shape_name

    def _clicked(self, event):
        """
        Handles the button click event.

        Args:
            event: The event object.
        """
        super()._clicked(event)

        if AppManager.clicked_button:
            clicked_same_as_current = AppManager.clicked_button.shape_name == self.shape_name

            if clicked_same_as_current:
                AppManager.clicked_button.configure(fg_color="transparent")
                AppManager.clicked_button = None
                self.app.configure(cursor='arrow')
            else:
                AppManager.clicked_button.configure(fg_color="transparent")
                self.configure(fg_color="blue", hover=False)
                self.app.configure(cursor="crosshair")

                AppManager.clicked_button = self

        else:
            self.configure(fg_color="blue", hover=False)
            self.app.configure(cursor="crosshair")
            AppManager.clicked_button = self
