import tkinter as tk
from tkinter import font
from tkinter import colorchooser

root = tk.Tk()

# Get available fonts
available_fonts = list(font.families())

# Print available fonts
for font_name in available_fonts:
    print(font_name)

root.mainloop()