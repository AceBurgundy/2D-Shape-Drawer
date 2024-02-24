import customtkinter
import CTkToast

from Navigation import Navigation
from Canvas import OpenGLCanvas
from CTkToast import CTkToast
from constants import *

class App(customtkinter.CTk):
    def __init__(self) -> None:
        """
        Initializes the app
        """
        super().__init__()
        self.geometry(WINDOW_SIZE)
        self.title("2D Shape Drawer by: Sam Adrian P. Sabalo")
        self.iconbitmap(ICON_PATH)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0, uniform="nav_col")
        self.grid_columnconfigure(1, weight=1, uniform="nav_col")
        self.bind("<Key>", self.pressed)

        self.right_content: OpenGLCanvas = OpenGLCanvas(self)
        self.right_content.grid(row=0, column=1, padx=BOTTOM_PADDING_ONLY, pady=DEFAULT_PADDING, sticky="nsew")

        left_content: Navigation = Navigation(parent=self)
        left_content.grid(row=0, column=0, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING, sticky="nsew")
        CTkToast(master=self)

    def pressed(self, event):
        self.right_content.key_pressed(event)