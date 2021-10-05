import tkinter
from tkinter import ttk
import sys

win = tkinter.Tk()
win.title(f"Hello, {sys.argv[-1]}")
# win.geometry("200x200")
win.resizable(False, False)
ttk.Label(win, text=f"Hello, {sys.argv[-1]}!").grid(column=0, row=0)

win.mainloop()
