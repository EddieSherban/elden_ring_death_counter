# elden_ring_death_counter
 Image processing OpenCV Python program that automatically detects and shows number of deaths on the screen

 # Download and Setup

 ## Step 1: Download the Files
![Alt text](step1.png)

 ## Step 2: Extract the folder to desired location

 ## Step 3: Adjust settings and death count in "deaths.txt" and "settings.txt" and save the file. DO NOT DELETE "you_died.png"!!

 ## Step 4: Run the "death_counter_app.exe" from the dist folder (ignore warnings, they are because of pyinstaller)

 ## Step 5: Play Elden Ring and the app will count your deaths for you

 ## Step 6: EXIT THE PROGRAM by left-clicking the "Deaths: " text
**You can exit the program by control-clicking the "Deaths" text.**  
**NOTE: Game should be in borderless window**  

 # Note on Operating Systems
   Currently only tested on my windows computer, not sure if works with other operating systems.

# Updates: Nov 21, 2024
  • Fixed the unclickable window bug. Now the windows from which you clicked should be clickable.  
  • Improved the algorithm so that it processes the template image once at the beginning of the program instead of every screenshot.  
  • Added "settings.txt" which can be edited. Currently only have "Deaths:" font size.  
  
