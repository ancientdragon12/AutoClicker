
"""
File: auto_clicker_macro.py
Author: Ancientdragon12
Date: 12-29-2023
Git repo: https://github.com/ancientdragon12/AutoClicker
Description: A program clicking the mouse repedativly with stop, start, and kill key presses
"""

import mouse
import keyboard
import threading
import time

# flag used to start/stop clicking
on_off = True
# flag used to kill program
kill_program = False

# This function does the clicking
def Auto_Click():
    mouse.click()
    #print("mouse click")
    time.sleep(0.1)

# this is checking key presses in another thread
def check_press():
    global on_off, kill_program
    while not kill_program:
        
        if keyboard.is_pressed('s') and on_off:
            on_off = False
            print("Auto Clicker Stopped")
        elif keyboard.is_pressed('r') and not on_off:
            on_off = True
            print("Auto Clicker Restarted")
        elif keyboard.is_pressed('k'):
            kill_program = True
            print("Auto Clicker is killed")
        time.sleep(0.1) #Check every 10th of a second
    
def main():
    global on_off,kill_program

    #starting thread
    check_thread = threading.Thread(target = check_press)
    check_thread.start()
    
    # Checks if you hit the kill button. If you did not hit the kill button, run the Auto_Click function.
    try:
        while not kill_program:
            while on_off:
                Auto_Click()
    except KeyboardInterrupt:
        kill_program = True

    #after kill his hit close all threads
    check_thread.join()
    print("stopped")

if __name__ == "__main__":
    main()