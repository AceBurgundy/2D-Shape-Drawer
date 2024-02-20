from typing import List, Type
from customtkinter import CTk
from OpenGL.GLU import *
from OpenGL.GL import *
from Manager import Manager
from Shape import Shape
import pyopengltk

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
        self.bind("<Motion>", self.on_mouse_move)
        self.bind("<ButtonPress-1>", self.on_mouse_press)
        self.bind("<ButtonRelease-1>", self.on_mouse_release)

        # Main frame
        self.parent = parent

        # Animation
        self.animate: int = 1
        self.after(100)

        # Shapes
        self.shapes: List[Type[Shape]] = []

        # Drag Events
        self.dragging = False
        self.start_coordinates = None
        self.current_coordinates = None
        self.end_coordinates = None

    def on_mouse_move(self, event):
        if Manager.clicked_button:
            if self.dragging:
                self.current_coordinates = (event.x, event.y)

    def on_mouse_press(self, event):
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

    def on_mouse_release(self, event):
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

        if self.dragging and self.start_coordinates:
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
        print(start_coordinates, end_coordinates)
        shape_class_reference = Shape.shapes().get(Manager.clicked_button.shape_name)
        shape_instance = shape_class_reference(start_coordinates=start_coordinates, end_coordinates=end_coordinates)

        Manager.clicked_button.configure(fg_color="transparent")
        Manager.clicked_button = None

        self.parent.configure(cursor='arrow')
        self.shapes.append(shape_instance)
