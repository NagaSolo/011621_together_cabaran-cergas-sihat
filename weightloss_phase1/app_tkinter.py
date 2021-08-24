import tkinter as tk

class Window:
    def __init__(self, root, title, geometry, message):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        tk.Label(self.root, message).pack()

def main():
    root = tk()
    windows1 = Window(root, 'Example', '300x300', 'Window 1 From class Window')