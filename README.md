# elden_ring_death_counter
 Image processing OpenCV Python program that automatically detects and shows number of deaths on the screen

 # Controlling the program and exiting
  • Go to the dist folder. "deaths.txt" can be deleted and edited, but do not delete the png image. 
  • Upon program start, a "Manual Death Counter" window is opened, where deaths can be incremented or decremented in case of errors.  
  • A "deaths.txt" is written at the end of the program, which can be modified to any number. It'll be read at the start next time.  
  • The "settings.txt" can be edited to adjust different features, as of right now it only has the "Deaths: " text font size. Save the "settings.txt" then run the program to see changes.
**• You can exit the program by control-clicking the "Deaths" text.**
**NOTE: Game should be in borderless window** 

 # Note on Operating Systems
   Currently only tested on my windows computer, not sure if works with other operating systems.

# Updates: Nov 21, 2024
  • Fixed the unclickable window bug. Now the windows from which you clicked should be clickable
  • Improved the algorithm so that it processes the template image once at the beginning of the program instead of every screenshot
  • Added "settings.txt" which can be edited. Currently only have "Deaths:" font size.
  
