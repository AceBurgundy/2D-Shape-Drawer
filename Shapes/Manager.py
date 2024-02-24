from typing import List, Dict, Type
from Shapes.Shape import Shape

from Shapes.Circle import Circle
from Shapes.Hexagon import Hexagon
from Shapes.Octagon import Octagon
from Shapes.Pentagon import Pentagon
from Shapes.Square import Square
from Shapes.Triangle import Triangle

def names() -> List[str]:
    """
    Static method to get the class names of all subclasses of Shape.

    Returns:
        List[str]: List of class names of all subclasses of Shape.
    """
    shape_names = shapes()
    return list(shape_names)

def shapes() -> Dict[str, Type['Shape']]:
    """
    Static method to get the class names and class objects of all subclasses of Shape.

    Returns:
        Dict[str, Type['Shape']]: Dictionary mapping class names to class objects of all subclasses of Shape.
    """
    return {subclass.__name__: subclass for subclass in Shape.__subclasses__()}
