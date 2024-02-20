from customtkinter import CTk, CTkFrame
from typing import Dict, List, Type
from OpenGL.GLU import *
from OpenGL.GL import *
import pyopengltk

from KeyPress import get_pressed_status
from custom_types import COORDINATE
from Shapes.Shape import Shape
from Manager import Manager

class OpenGLCanvas(pyopengltk.OpenGLFrame):
    def __init__(self, parent: Type[CTk], **kwargs) -> None:
        """
        Initializes the App object.

        Args:
            parent (Type[CTk]): The parent MainApp object.
            **kwargs: Additional keyword arguments to pass to the parent class initializer.
        """
        super().__init__(parent, **kwargs)

        # Event binds
        self.bind("<Motion>", self._on_mouse_move)
        self.bind("<ButtonPress-1>", self._on_mouse_press)
        self.bind("<ButtonRelease-1>", self._on_mouse_release)

        # Main frame
        self.parent: Type[CTkFrame] = parent

        # Animation
        self.animate: int = 1
        self.after(100)

        # Shapes
        self.shapes: List[Type[Shape]] = []

        # Drag Events
        self.dragging: bool = False
        self.start_coordinates: COORDINATE = None
        self.current_coordinates: COORDINATE = None
        self.end_coordinates: COORDINATE = None

        # Key press
        self.control_left_pressed: bool = False
        self.shift_left_pressed: bool = False

    def key_pressed(self, event) -> None:
        """
        Handles key pressed events sent from main CTk frame
        """
        if Manager.selected_shape == None:
            return

        press_status: Dict[str, List|str] = get_pressed_status(event)
        state: List[str] = press_status.get('state', None)
        key: str = press_status['key']

        if not state:
            return

        if len(state) > 2:
            return

        pressed_shift: bool = 'Shift' in state
        pressed_control: bool = 'Control' in state
        held_both: bool = pressed_shift and pressed_control

        pressed_plus: bool = held_both and key == 'plus'
        pressed_minus: bool = held_both and key == 'underscore'

        if pressed_plus:
            print("increase shape")
            return

        if pressed_minus:
            print("decrease_shape")
            return

    def _on_mouse_move(self, event) -> None:
        """
        Handles mouse move events
        """
        if Manager.clicked_button:
            if self.dragging:
                self.current_coordinates = (event.x, event.y)

    def _on_mouse_press(self, event) -> None:
        """
        Handles mouse press events
        """
        if Manager.clicked_button:
            self.dragging = True
            self.start_coordinates = (event.x, event.y)
            self.current_coordinates = self.start_coordinates
            return

        if self.shapes:
            for shape in self.shapes:
                if shape.within_bounds(event.x, event.y):
                    if Manager.selected_shape:
                        Manager.selected_shape.selected = False

                        shape.selected = True
                        Manager.selected_shape = shape
                        break;
                    else:
                        shape.selected = True
                        Manager.selected_shape = shape

    def _on_mouse_release(self, event):
        """
        Handles mouse release events
        """
        if Manager.clicked_button:
            if self.dragging:
                self.end_coordinates = (event.x, event.y)
                self.insert_shape(self.start_coordinates, self.end_coordinates)

            self.dragging = False
            self.start_coordinates = None
            self.end_coordinates = None
            return

    def initgl(self) -> None:
        """
        Initializes the canvas
        """
        glViewport(0, 0, self.width, self.height)
        glClearColor(0.17, 0.17, 0.17, 1.0)

    def redraw(self) -> None:
        """
        Sets canvas properties and calls a shape draw method if not None
        """
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, self.width, self.height, 0, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        if self.dragging and Manager.clicked_button:
            glBegin(GL_LINES)
            glVertex2f(*self.start_coordinates)
            glVertex2f(*self.current_coordinates)
            glEnd()

        if self.shapes:
            Shape.canvas_width = self.winfo_width()
            Shape.canvas_height = self.winfo_height()

            for shape in self.shapes:
                shape.draw()

    def insert_shape(self, start_coordinates, end_coordinates) -> None:
        """
        Inserts a shape into the canvas
        """
        shape_class_reference = Shape.shapes().get(Manager.clicked_button.shape_name)
        shape_instance = shape_class_reference(start_coordinates=start_coordinates, end_coordinates=end_coordinates)

        Manager.clicked_button.configure(fg_color="transparent")
        Manager.clicked_button = None

        self.parent.configure(cursor='arrow')
        self.shapes.append(shape_instance)
