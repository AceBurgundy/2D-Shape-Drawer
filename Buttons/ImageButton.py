# for type checking purposes.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Program import App

# start of code
from customtkinter import CTkButton, CTkImage, CTkFrame
from abc import ABC, abstractmethod
from typing import Type
from PIL import Image
from os import path

class ImageButton(CTkButton, ABC):
    def __init__(self, parent: Type[CTkFrame], app: App, image_file_name: str, *args, **kwargs):
        """
        Initializes the Button object.

        Args:
            parent (Navigation): The parent CTkFrame object.
            app (App): The MainApp object associated with the button.
            image_file_name (str): The str representing the shape draw method.
            *args: Additional positional arguments to pass to the parent class initializer.
            **kwargs: Additional keyword arguments to pass to the parent class initializer.
        """
        super().__init__(parent, *args, **kwargs)
        self.configure(corner_radius=0, fg_color="transparent")

        self.image_file_name: str = image_file_name
        self.app: App = app

        image_path: str = path.join('icon_asset', f"{image_file_name}.PNG")

        if not path.exists(image_path):
            raise TypeError('The name of the image must be the same as the __name__ of the method')

        image = Image.open(fp=image_path)
        icon: CTkImage = CTkImage(size=(25, 25), light_image=image, dark_image=image)
        self.configure(image=icon, text='', height=0, width=0)

    @abstractmethod
    def _clicked(self, event) -> None:
        """
        The click event for the button
        """