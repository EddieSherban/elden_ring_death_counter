import tkinter as tk
from random import seed, choice
from string import ascii_letters
import ctypes

seed(42)

colors = ('red', 'yellow', 'green', 'cyan', 'blue', 'magenta')
def do_stuff():
    s = ''.join([choice(ascii_letters) for i in range(10)])
    color = choice(colors)
    l.config(text="Deaths: ", fg=color)
    root.after(1000, do_stuff)

def make_window_transparent(hwnd):
    # Define the MARGINS structure
    class MARGINS(ctypes.Structure):
        _fields_ = [("cxLeftWidth", ctypes.c_int),
                    ("cxRightWidth", ctypes.c_int),
                    ("cyTopHeight", ctypes.c_int),
                    ("cyBottomHeight", ctypes.c_int)]
        
    # Create an instance of MARGINS with -1 to extend frame into entire window
    margins = MARGINS(-1, -1, -1, -1)
    ctypes.windll.dwmapi.DwmExtendFrameIntoClientArea(hwnd, ctypes.byref(margins))
    # Set window style to layered with transparent attributes
    ctypes.windll.user32.SetWindowLongW(hwnd, -20, ctypes.windll.user32.GetWindowLongW(hwnd, -20) | 0x80000 | 0x20)
    # Always on top
    ctypes.windll.user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0003)

root = tk.Tk()
root.wm_overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.attributes("-topmost", True)
root.attributes("-transparentcolor", root['bg'])
root.bind("<Button-1>", lambda evt: root.destroy())

l = tk.Label(root, text='', font=("Helvetica", 60), bg=root['bg'])
l.pack(expand=True)
l.place(relx=0.5, y=10, anchor='n')

#Get the window handle and make it t ransparent
hwnd = ctypes.windll.user32.GetForegroundWindow()
make_window_transparent(hwnd)

do_stuff()
root.mainloop()