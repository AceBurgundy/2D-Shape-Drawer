# for type checking purposes.

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from Program import App

# start of code
from typing import Dict, List, Type
from OpenGL.GLU import *
from OpenGL.GL import *
import pyopengltk

from KeyPress import get_pressed_status
from custom_types import COORDINATE
from Shapes.Manager import shapes
from Shapes.Shape import Shape
from CTkToast import CTkToast
from Global import Global

class OpenGLCanvas(pyopengltk.OpenGLFrame):
    def __init__(self, parent: App, **kwargs) -> None:
        """
        Initializes the App object.

        Args:
            parent (App): The parent MainApp object.
            **kwargs: Additional keyword arguments to pass to the parent class initializer.
        """
        super().__init__(parent, **kwargs)

        # Event binds
        self.bind("<Motion>", self._on_mouse_move)
        self.bind("<ButtonPress-1>", self._on_mouse_press)
        self.bind("<ButtonRelease-1>", self._on_mouse_release)

        # Main frame
        self.parent: App = parent

        # Animation
        self.animate: int = 1

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
        press_status: Dict[str, List|str] = get_pressed_status(event)
        state: List[str] = press_status.get('state', None)
        key: str = press_status['key']

        if not state:
            return

        pressed_shift: bool = 'Shift' in state
        pressed_control: bool = 'Control' in state
        held_both: bool = pressed_shift and pressed_control

        if held_both:

            if key == 'plus':
                if Global.shape == None:
                    CTkToast.toast("Select a shape first to increase its size")
                    return

                Global.shape.increase_shape()
                return

            if key == 'underscore':
                if Global.shape == None:
                    CTkToast.toast("Select a shape first to decrease its size")
                    return

                Global.shape.decrease_shape()
                return

            if key == 'Left':
                if Global.shape == None:
                    CTkToast.toast("Select a shape first to rotate it to counter clockwise")
                    return

                Global.shape.rotate_left()
                return

            if key == 'Right':
                if Global.shape == None:
                    CTkToast.toast("Select a shape first to rotate it clockwise")
                    return

                Global.shape.rotate_right()
                return

        else:
            if key == 'Delete':
                if Global.shape == None:
                    CTkToast.toast("Select a shape to delete")
                    return

                for shape in self.shapes:
                    shape_name: str = shape.__class__.__name__
                    selected_shape_name: str = Global.shape.__class__.__name__

                    if selected_shape_name == shape_name:
                        self.shapes.remove(shape)
                        Global.shape = None
                return

            if key == 'Up':
                if Global.shape == None:
                    CTkToast.toast("Select a shape first to move it up")
                    return

                Global.shape.move_up()
                return

            if key == 'Down':
                if Global.shape == None:
                    CTkToast.toast("Select a shape first to move it down")
                    return

                Global.shape.move_down()
                return

            if key == 'Left':
                if Global.shape == None:
                    CTkToast.toast("Select a shape first to move it to the left")
                    return

                Global.shape.move_left()
                return

            if key == 'Right':
                if Global.shape == None:
                    CTkToast.toast("Select a shape first to move it to the right")
                    return

                Global.shape.move_right()
                return

    def _on_mouse_move(self, event) -> None:
        """
        Handles mouse move events
        """
        if self.dragging:
            if Global.clicked_button:
                self.current_coordinates = (event.x, event.y)

    def _on_mouse_press(self, event) -> None:
        """
        Handles mouse press events
        """
        if Global.clicked_button:
            self.dragging = True
            self.start_coordinates = (event.x, event.y)
            self.current_coordinates = self.start_coordinates
            return

        is_within_any_shape_bounds: bool = False

        if len(self.shapes) == 0:
            return

        for shape in self.shapes[::-1]:
            if not shape.within_bounds(event.x, event.y):
                continue

            is_within_any_shape_bounds = True

            if not Global.shape:
                shape.selected = True
                Global.shape = shape

            Global.shape.selected = False
            Global.shape = shape

            Global.shape.selected = True
            break

        if not is_within_any_shape_bounds and Global.shape:
            Global.shape.selected = False
            Global.shape = None


    def _on_mouse_release(self, event):
        """
        Handles mouse release events
        """
        if Global.clicked_button and self.dragging:
            self.end_coordinates = (event.x, event.y)
            self.insert_shape(self.start_coordinates, self.end_coordinates)

            self.dragging = False
            self.start_coordinates = None
            self.end_coordinates = None

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

        if self.shapes:
            Shape.canvas_width = self.winfo_width()
            Shape.canvas_height = self.winfo_height()

            for shape in self.shapes:
                shape.draw_to_canvas()

        if self.dragging and Global.clicked_button:
            glBegin(GL_LINES)
            glVertex2f(*self.start_coordinates)
            glVertex2f(*self.current_coordinates)
            glEnd()

    def insert_shape(self, start_coordinates, end_coordinates) -> None:
        """
        Inserts a shape into the canvas
        """
        shape_class_reference: Type[Shape] = shapes().get(Global.clicked_button.image_file_name)
        shape_instance: Type[Shape] = shape_class_reference(start_coordinates=list(start_coordinates), end_coordinates=list(end_coordinates))

        Global.clicked_button.configure(fg_color="transparent")
        Global.clicked_button = None

        self.parent.configure(cursor='arrow')
        self.shapes.append(shape_instance)
