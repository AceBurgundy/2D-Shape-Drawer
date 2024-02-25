from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel
from custom_types import *
from constants import *

type PADDING_LIST = List[Tuple[str, Tuple[int, int]]]

class Tutorial(CTk):
    def __init__(self) -> None:
        """
        Shows a window with the apps controls
        """
        super().__init__()
        self.title("Controls")
        self.iconbitmap(ICON_PATH)

        window_width: int = 300
        window_height: int = 350
        screen_width: int = self.winfo_screenwidth()
        screen_height: int = self.winfo_screenheight()

        x_position: NUMBER = (screen_width - window_width) // 2
        y_position: NUMBER = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.grid_columnconfigure(0, weight=1)

        self.resize_section()
        self.rotate_section()
        self.movement_section()
        self.delete_section()

    def resize_section(self) -> None:
        """
        Contains controls for resizing
        """
        resize_title: CTkLabel = CTkLabel(self, text="Resize")
        resize_title.grid(row=1, column=0, pady=TOP_PADDING_ONLY, sticky="nswe")

        div: CTkFrame = CTkFrame(self)
        div.grid(row=3, column=0, sticky="ns")

        self.resize_buttons(div, 'Increase size', 4)

        div: CTkFrame = CTkFrame(self)
        div.grid(row=5, column=0, sticky="ns", pady=TOP_PADDING_ONLY)

        self.resize_buttons(div, 'Decrease size', 4)

    def resize_buttons(self, parent: CTkFrame, text: str, row: int) -> None:
        """
        Different button controls for resizing
        """
        buttons: PADDING_LIST = [
            ('Cntrl', LEFT_PADDING_ONLY), ('+', DEFAULT_PADDING), ('Shift', 0), ('=', DEFAULT_PADDING), (text, RIGHT_PADDING_ONLY)
        ]

        for index, (button_text, padx) in enumerate(buttons):
            control_button = CTkButton(parent, height=10, width=10, text=button_text)
            control_button.grid(row=0, column=index, sticky="nswe", padx=padx, pady=DEFAULT_PADDING)

    def rotate_section(self) -> None:
        """
        Contains controls for rotation
        """
        rotate_title: CTkLabel = CTkLabel(self, text="Rotate")
        rotate_title.grid(row=7, column=0, sticky="nswe", pady=TOP_PADDING_ONLY)

        div: CTkFrame = CTkFrame(self)
        div.grid(row=8, column=0, sticky="ns")

        self.rotate_buttons(div, 'Left Arrow')

        div: CTkFrame = CTkFrame(self)
        div.grid(row=9, column=0, sticky="ns", pady=TOP_PADDING_ONLY)

        self.rotate_buttons(div, 'Right Arrow')

    def rotate_buttons(self, parent: CTkFrame, text: str) -> None:
        """
        Different button controls for rotation
        """
        buttons: PADDING_LIST = [
            ('Cntrl', LEFT_PADDING_ONLY), ('+', DEFAULT_PADDING), ('Shift', 0), ('=', DEFAULT_PADDING), (text, RIGHT_PADDING_ONLY)
        ]

        for index, (button_text, padx) in enumerate(buttons):
            control_button = CTkButton(parent, height=10, width=10, text=button_text)
            control_button.grid(row=0, column=index, sticky="nswe", padx=padx, pady=DEFAULT_PADDING)

    def movement_section(self) -> None:
        """
        Contains different button for shape movement
        """
        arrow_titles: CTkLabel = CTkLabel(self, text="Movement")
        arrow_titles.grid(row=10, column=0, sticky="nswe", pady=TOP_PADDING_ONLY)

        div: CTkFrame = CTkFrame(self)
        div.grid(row=11, column=0, sticky="ns")

        buttons: PADDING_LIST = [
            ('Left Arrow', DEFAULT_PADDING), ('>', RIGHT_PADDING_ONLY), ('^', DEFAULT_PADDING), ('v', DEFAULT_PADDING)
        ]

        for index, (button_text, padx) in enumerate(buttons):
            control_button = CTkButton(div, height=10, width=10, text=button_text)
            control_button.grid(row=0, column=index, sticky="nswe", padx=padx, pady=DEFAULT_PADDING)

    def delete_section(self) -> None:
        """
        Contains button for delete
        """
        delete_title: CTkLabel = CTkLabel(self, text="Delete")
        delete_title.grid(row=12, column=0, sticky="nswe", pady=TOP_PADDING_ONLY)

        div: CTkFrame = CTkFrame(self)
        div.grid(row=13, column=0, sticky="ns")

        delete: CTkButton = CTkButton(div, height=10, width=10, text='Delete')
        delete.grid(row=0, column=0, sticky="nswe", padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)
