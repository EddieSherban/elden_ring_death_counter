import cv2
import numpy as np
import pyautogui
import time
import pygame
import pygame.freetype
import tkinter as tk
import ctypes
import sys
import os
from pygame.locals import *

def toggle_visibility():
    if root.winfo_viewable():
        root.withdraw()
    else:
        root.deiconify()

def read_deaths():
    if os.path.exists('deaths.txt'):
        with open('deaths.txt', 'r') as file:
            return int(file.read())
    return 0

def read_settings():
    settings = {
        "font size": 50,  # default value
        #add defaults for other settings when needed
    }

    if os.path.exists('settings.txt'):
        with open('settings.txt', 'r') as file:
            for line in file:
                # skip empty lines or lines without a colon
                if ':' not in line.strip():
                    continue

                # split line into key and value
                key, value = map(str.strip, line.split(':', 1))

                # convert value to integer if numeric
                if value.isdigit():
                    value = int(value)

                #update settinsg dictrionary
                settings[key.lower()] = value
    return settings
    
def write_deaths(deaths):
    with open('deaths.txt', 'w') as file:
        file.write(str(deaths))

def present_image(image, message):
    cv2.imshow(message, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Not used in program, but may be useful as improvement later on
def detect_color_edges(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)      # Convert BGR to HSV
    hue, saturation, value = cv2.split(hsv_image)           # Split HSV channels
    edges = cv2.Canny(hue, 50, 150)                         # Example: detect edges based on the hue channel
    return edges


# Capture the screen and convert it to grayscale
def capture_screen():
    screenshot = pyautogui.screenshot()
    screen = np.array(screenshot)
    gray_screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
    #print(gray_screen.shape)
    return gray_screen

# Check for "You Died" on the screen
def check_for_death():
    l.config(fg="cyan")
    screen = capture_screen()
    screen_w, screen_h = screen.shape[::-1]
    cropped_screen = screen[round(screen_h*0.48):round(screen_h*0.53), round(screen_w*0.4):round(screen_w*0.605)]
    #present_image(cropped_screen, "cropped screen")
    cropped_screen_equalized = cv2.equalizeHist(cropped_screen)
    #screen_edges = detect_color_edges(cropped_screen)
    screen_edges = cv2.Canny(cropped_screen_equalized, 300, 400)
    #present_image(screen_edges, "screen edges")
    #present_image(template_edges, "template edges")
    res = cv2.matchTemplate(screen_edges, template_edges, cv2.TM_CCOEFF_NORMED)
    threshold = 0.1
    loc = np.where(res >= threshold)
    #print(res)
    if len(loc[0]) > 0:
        return True
    return False

def update_deaths_text(deaths):
    l.config(text=f"Deaths: {deaths}", fg="yellow")

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
    ctypes.windll.user32.SetWindowLongW(hwnd, -20, ctypes.windll.user32.GetWindowLongW(hwnd, -20) | 0x80000)
    # Always on top
    ctypes.windll.user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0003)

def increment_deaths():
    global death_counter
    death_counter += 1
    update_deaths_text(death_counter)

def decrement_deaths():
    global death_counter
    if death_counter > 0:
        death_counter -= 1
        update_deaths_text(death_counter)

# Load the "You Died" image template
template = cv2.imread('you_died.png', 0)
#template16 = cv2.imread('screenshot16.png', 0)
#present_image(template, "template")
template_w, template_h = template.shape[::-1]
cropped_template = template[round(template_h*0.48):round(template_h*0.53), round(template_w*0.4):round(template_w*0.605)] # note: 48% to 53% of image height
cropped_template_equalized = cv2.equalizeHist(cropped_template)
template_edges = cv2.Canny(cropped_template_equalized, 100, 150)
#present_image(cropped_template, "cropped template")
#present_image(template16, "template 16")
#print("beginning")

settings = read_settings()
font_size = settings.get("font size", 50) #default to 50 if key not found

#text overlay init
root = tk.Tk()
root.wm_overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.attributes("-topmost", True)
root.attributes("-transparentcolor", root['bg'])
root.bind("<Control-Button-1>", lambda evt: root.destroy()) # Bind the Q key to exit the script
#root.bind("<Button-1>", lambda evt: toggle_visibility())


# Create a new window for increment/decrement buttons
control_window = tk.Toplevel(root)
control_window.geometry("200x100")
control_window.title("Manual Death Counter")

# Create a window with a button to manually increment/decrement deaths
increment_button = tk.Button(control_window, text="+", command=increment_deaths, font=("Helvetica", 20))
increment_button.pack(side="left", expand=True, fill="both")
decrement_button = tk.Button(control_window, text="-", command=decrement_deaths, font=("Helvetica", 20))
decrement_button.pack(side="right", expand=True, fill="both")

l = tk.Label(root, text='', font=("Helvetica", font_size), bg=root['bg'])
l.pack(expand=True)
l.place(relx=0.5, y=10, anchor='n')

#Get the window handle and make it t ransparent
#print("transparent window:")
hwnd = ctypes.windll.user32.GetForegroundWindow()
make_window_transparent(hwnd)

death_counter = read_deaths()

def check_and_update():
    global death_counter
    update_deaths_text(death_counter)
    if check_for_death():
        death_counter += 1
        print(f"Deaths: {death_counter}")
        update_deaths_text(death_counter)
        root.after(5000, check_and_update)
    else:
        root.after(800, check_and_update)

#Start the periodic death check
#print("periodic death check?")
root.after(800, check_and_update)

# Start the Tkinter main loop
root.mainloop()

# Write the total number of deaths to the file when the program terminates
write_deaths(death_counter)