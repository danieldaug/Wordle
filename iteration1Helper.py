"""
File: iteration1Helper.py
Author: COMP 120 instructor
Date: April 25, 2021
Description: Code that illustrates working with frames.
"""
import random
import tkinter as tk

import tkinter.font as font
import time

from enum import Enum

class Iteration1Helper:
    def __init__(self):
        # Create window
        self.window = tk.Tk()
        self.window.title("Iteration1 Helper")

        # Create a frame.
        self.frame1 = tk.Frame(self.window, 
            borderwidth = 1, relief = 'solid',
            height = 300, width = 100)
        self.frame1.grid(row = 1, column = 1)
        self.frame1.grid_propagate(False)

        # Put a frame to the right of it.
        self.frame2 = tk.Frame(self.window, 
            borderwidth = 1, relief = 'solid',
            height = 300, width = 200)
        self.frame2.grid(row = 1, column = 2)
        self.frame2.grid_propagate(False)

        # Put a frame below the top two.
        self.frame3 = tk.Frame(self.window, 
            borderwidth = 1, relief = 'solid',
            height = 400, width = 100 + 200)
        self.frame3.grid(row = 2, column = 1, columnspan = 2)
        self.frame3.grid_propagate(False)

        # Start event loop
        self.window.mainloop()
        

if __name__ == "__main__":
   Iteration1Helper()