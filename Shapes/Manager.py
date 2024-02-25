from typing import List, Dict, Type
from Shapes.Polygon import Polygon
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
    shape_names: List[str] = shapes()
    return list(shape_names)

def shapes() -> Dict[str, Type['Shape']]:
    """
    Static method to get the class names and class objects of all subclasses of Shape.

    Returns:
        Dict[str, Type['Shape']]: Dictionary mapping class names to class objects of all subclasses of Shape.
    """
    shape_dictionary: Dict[str, Type[Shape|Polygon]] = {subclass.__name__: subclass for subclass in Shape.__subclasses__()}
    polygon_dictionary: Dict[str, Type[Shape|Polygon]] = {subclass.__name__: subclass for subclass in Polygon.__subclasses__()}

    shape_dictionary.pop('Polygon')
    merged: Dict[str, Type[Shape|Polygon]] = shape_dictionary.copy()
    merged.update(polygon_dictionary)
    return merged
