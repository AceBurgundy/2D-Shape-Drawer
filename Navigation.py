from customtkinter import CTkFrame, CTk

from Button import ShapeButton
from Shapes.Shape import Shape
from typing import Type

class Navigation(CTkFrame):
    def __init__(self, parent: Type[CTk], **kwargs):
        """
        Initializes the Navigation object.

        Args:
            parent (Type[CTk]): The parent CTk object.
            buttons (List[Str]): A list of str objects representing the names of the shapes.
            **kwargs: Additional keyword arguments to pass to the parent class initializer.

        Raises:
            TypeError: If the list of buttons is empty.
        """
        super().__init__(parent, **kwargs)
        self.parent: Type[CTk] = parent

        button_box: CTkFrame = CTkFrame(self)
        button_box.pack(pady=(5, 0), padx=3)

        for index, shape_name in enumerate(Shape.names()):
            button_box.configure(fg_color="transparent")
            button: ShapeButton = ShapeButton(button_box, self.parent, shape_name)

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
