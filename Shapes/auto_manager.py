from os import path, listdir
from typing import List

def list_module_shapes():
    exempted_files: List[str] = ["__init__.py", "__pycache__", "Shape.py", "auto_manager.py", "Manager.py"]
    shape_file_names: List[str|None] = []

    for file_name in listdir('Shapes'):
        file_path: str = path.join('Shapes', file_name)
        if file_name not in exempted_files and path.isfile(file_path):
            clean_name: str = file_name.replace('.py', '')
            shape_file_names.append(clean_name)

    return shape_file_names

def update_manager_py():
    shapes: List[str] = list_module_shapes()
    manager_path: str = path.join('Shapes', 'Manager.py')

    code_lines = [
        "from typing import List, Dict, Type",
        "from Shapes.Shape import Shape",
        "",
        *[f"from Shapes.{shape} import {shape}" for shape in shapes],
        "",
        "def names() -> List[str]:",
        '''    """''',
        "    Static method to get the class names of all subclasses of Shape.",
        "",
        "    Returns:",
        "        List[str]: List of class names of all subclasses of Shape.",
        '''    """''',
        "    shape_names = shapes()",
        "    return list(shape_names)",
        "",
        "def shapes() -> Dict[str, Type['Shape']]:",
        '''    """''',
        "    Static method to get the class names and class objects of all subclasses of Shape.",
        "",
        "    Returns:",
        "        Dict[str, Type['Shape']]: Dictionary mapping class names to class objects of all subclasses of Shape.",
        '''    """''',
        "    return {subclass.__name__: subclass for subclass in Shape.__subclasses__()}"
    ]

    try:
        with open(manager_path, 'w') as file:
            for line in code_lines:
                file.write(line + '\n')

        return True
    except Exception as error:
        print(error)
        return False