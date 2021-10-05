import tkinter
from tkinter import ttk
import sys

class Window(tkinter.Tk):
    def __init__(self, name="World"):
        super().__init__()
        self.title(f"Hello, {name}!")
        self.geometry("200x200")
        self.resizable(False, False)
        ttk.Label(self, text=f"Hello, {name}!").grid(column=0, row=0)


if __name__ == '__main__':
    try:
        win = Window(name=sys.argv[1])
    except IndexError:
        win = Window()
    win.mainloop()


