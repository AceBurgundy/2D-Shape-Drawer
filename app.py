from Shapes.auto_manager import update_manager_py
from Program import App

if __name__ == '__main__':
    update: bool = update_manager_py()

    if update:
        App().mainloop()
