from tkinter import filedialog, Tk
from CTkToast import CTkToast
import pickle

def export_to_file(input_list) -> bool:
    """
    Save a list of class instances to a file with the .dsd format.

    Args:
    input_list (list): The list of class instances to be saved.
    file_path (str): The path to save the file.

    Returns:
        bool: If the file has been saved succesfully
    """
    file_path: str = save_file_dialog()

    if file_path is None:
        CTkToast.toast('Cancelled file selection')
        return False

    with open(file_path, 'wb') as file:
        pickle.dump(input_list, file)

    return True

def open_file_dialog() -> str | None:
    """
    Prompts the user where to pick the file
    """
    root = Tk()
    root.withdraw()

    file_path: str = filedialog.askopenfilename()
    return file_path if file_path else None

def save_file_dialog() -> str | None:
    """
    Prompts the user on where to save the file
    """
    root: Tk = Tk()
    root.withdraw()

    file_path: str = filedialog.asksaveasfilename(
        defaultextension=".pkl",
        filetypes=[
            ("Pickle", "*.pkl"),
            ("All files", "*.*")
        ]
    )

    return file_path if file_path else None

def import_from_file():
    """
    Import a list of class instances from a file with the .dsd format.

    Args:
    file_path (str): The path of the file to import.

    Returns:
    list: The imported list of class instances.
    """
    file_path: str = open_file_dialog()

    if not file_path:
        CTkToast.toast('Cancelled selection')
        return

    with open(file_path, 'rb') as file:
        output_list = pickle.load(file)

    return output_list
