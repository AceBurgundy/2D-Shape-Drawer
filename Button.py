from customtkinter import CTkButton, CTkFrame, CTk, CTkImage
from Manager import Manager
from typing import Type
from PIL import Image
from os import path

class ShapeButton(CTkButton):
    def __init__(self, parent: Type[CTkFrame], app: Type[CTk], shape_name: str, *args, **kwargs):
        """
        Initializes the Button object.

        Args:
            parent (Type[CTkFrame]): The parent CTkFrame object.
            app (Type[CTk]): The MainApp object associated with the button.
            shape_name (str): The str representing the shape draw method.
            *args: Additional positional arguments to pass to the parent class initializer.
            **kwargs: Additional keyword arguments to pass to the parent class initializer.
        """
        super().__init__(parent, *args, **kwargs)
        self.configure(corner_radius=0, fg_color="transparent")

        self.shape_name: str = shape_name
        self.app: Type[CTk] = app

        image_path: str = path.join('icon_asset', f"{shape_name}.PNG")

        if not path.exists(image_path):
            raise TypeError('The name of the image must be the same as the __name__ of the method')

        image = Image.open(fp=image_path)
        icon: CTkImage = CTkImage(size=(50, 50), light_image=image, dark_image=image)
        self.configure(image=icon, text='', height=0, width=0)

    def _clicked(self, event):
        """
        Handles the button click event.

        Args:
            event: The event object.
        """
        super()._clicked(event)

        if Manager.clicked_button:
            clicked_same_as_current = Manager.clicked_button.shape_name == self.shape_name

            if clicked_same_as_current:
                Manager.clicked_button.configure(fg_color="transparent")
                Manager.clicked_button = None
                self.app.configure(cursor='arrow')
            else:
                Manager.clicked_button.configure(fg_color="transparent")
                self.configure(fg_color="blue", hover=False)
                self.app.configure(cursor="crosshair")

                Manager.clicked_button = self

        else:
            self.configure(fg_color="blue", hover=False)
            self.app.configure(cursor="crosshair")

            Manager.clicked_button = self
