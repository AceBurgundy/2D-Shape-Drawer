from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel
from custom_types import *
from constants import *

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

        resize_title = CTkLabel(self, text="Resize")
        resize_title.grid(row=1, column=0, pady=TOP_PADDING_ONLY, sticky="nswe")

        # Increase size
        div = CTkFrame(self)
        div.grid(row=3, column=0, sticky="ns")

        control = CTkButton(div, height=10, width=10, text='Cntrl')
        control.grid(row=0, column=0, sticky="nswe", padx=LEFT_PADDING_ONLY, pady=DEFAULT_PADDING)

        plus = CTkLabel(div, text='+', width=5)
        plus.grid(row=0, column=1, sticky="nswe", padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

        shift = CTkButton(div, height=10, width=10, text='Shift')
        shift.grid(row=0, column=2, sticky="nswe", pady=DEFAULT_PADDING)

        equals = CTkLabel(div, text='=', width=5)
        equals.grid(row=0, column=3, sticky="nswe", padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

        increase = CTkButton(div, height=10, width=10, text='Increase size')
        increase.grid(row=0, column=4, sticky="nswe", padx=RIGHT_PADDING_ONLY, pady=DEFAULT_PADDING)

        # Decrease Size
        div = CTkFrame(self)
        div.grid(row=5, column=0, sticky="ns", pady=TOP_PADDING_ONLY)

        control = CTkButton(div, height=10, width=10, text='Cntrl')
        control.grid(row=0, column=0, sticky="nswe", padx=LEFT_PADDING_ONLY, pady=DEFAULT_PADDING)

        plus = CTkLabel(div, height=5, text='+', width=5)
        plus.grid(row=0, column=1, sticky="nswe", padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

        shift = CTkButton(div, height=10, width=10, text='Shift')
        shift.grid(row=0, column=2, sticky="nswe", pady=DEFAULT_PADDING)

        equals = CTkLabel(div, height=5, text='=', width=5)
        equals.grid(row=0, column=3, sticky="nswe", padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

        decrease = CTkButton(div, height=10, width=10, text='Decrease size')
        decrease.grid(row=0, column=4, sticky="nswe", padx=RIGHT_PADDING_ONLY, pady=DEFAULT_PADDING)

        # Rotate counter
        rotate_title = CTkLabel(self, text="Rotate")
        rotate_title.grid(row=7, column=0, sticky="nswe", pady=TOP_PADDING_ONLY)

        div = CTkFrame(self)
        div.grid(row=8, column=0, sticky="ns")

        control = CTkButton(div, height=10, width=10, text='Cntrl')
        control.grid(row=0, column=0, sticky="nswe", padx=LEFT_PADDING_ONLY, pady=DEFAULT_PADDING)

        plus = CTkLabel(div, height=5, text='+', width=5)
        plus.grid(row=0, column=1, sticky="nswe", padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

        shift = CTkButton(div, height=10, width=10, text='Shift')
        shift.grid(row=0, column=2, sticky="nswe", pady=DEFAULT_PADDING)

        equals = CTkLabel(div, height=5, text='=', width=5)
        equals.grid(row=0, column=3, sticky="nswe", padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

        left_arrow = CTkButton(div, height=10, width=10, text='Left Arrow')
        left_arrow.grid(row=0, column=4, sticky="nswe", padx=RIGHT_PADDING_ONLY, pady=DEFAULT_PADDING)

        # Rotate
        div = CTkFrame(self)
        div.grid(row=9, column=0, sticky="ns", pady=TOP_PADDING_ONLY)

        control = CTkButton(div, height=10, width=10, text='Cntrl')
        control.grid(row=0, column=0, sticky="nswe", padx=LEFT_PADDING_ONLY, pady=DEFAULT_PADDING)

        plus = CTkLabel(div, height=10, text='+', width=5)
        plus.grid(row=0, column=1, sticky="nswe", padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

        shift = CTkButton(div, height=10, width=10, text='Shift')
        shift.grid(row=0, column=2, sticky="nswe", pady=DEFAULT_PADDING)

        equals = CTkLabel(div, height=1, text='=', width=5)
        equals.grid(row=0, column=3, sticky="nswe", padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

        right_arrow = CTkButton(div, height=10, width=10, text='Right Arrow')
        right_arrow.grid(row=0, column=4, sticky="nswe", padx=RIGHT_PADDING_ONLY, pady=DEFAULT_PADDING)

        # Movement
        arrow_titles = CTkLabel(self, text="Movement")
        arrow_titles.grid(row=10, column=0, sticky="nswe", pady=TOP_PADDING_ONLY)

        div = CTkFrame(self)
        div.grid(row=11, column=0, sticky="ns")

        left_arrow = CTkButton(div, height=10, width=10, text='<')
        left_arrow.grid(row=0, column=0, sticky="nswe", padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

        right_arrow = CTkButton(div, height=10, width=10, text='>')
        right_arrow.grid(row=0, column=2, sticky="nswe", padx=RIGHT_PADDING_ONLY, pady=DEFAULT_PADDING)

        top_arrow = CTkButton(div, height=10, text='^', width=5)
        top_arrow.grid(row=0, column=3, sticky="nswe", pady=DEFAULT_PADDING)

        bottom_arrow = CTkButton(div, height=10, width=10, text='v')
        bottom_arrow.grid(row=0, column=4, sticky="nswe", padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

        # Delete
        delete_title = CTkLabel(self, text="Movement")
        delete_title.grid(row=12, column=0, sticky="nswe", pady=TOP_PADDING_ONLY)

        div = CTkFrame(self)
        div.grid(row=13, column=0, sticky="ns")

        delete = CTkButton(div, height=10, width=10, text='Delete')
        delete.grid(row=0, column=0, sticky="nswe", padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)
