"""
File: iteration2Helper.py
Author: COMP 120 instructor
Date: April 25, 2021
Description: Code that illustrates putting widgets in frames.
"""
import random
import tkinter as tk

import tkinter.font as font
import time

from enum import Enum

class Iteration2Helper:
    def __init__(self):
        """
        Initialize the window with frames and widgets.
        """
        # Constants
        self.PADDING = 10 # Padding around widgets
        self.ENTRY_SIZE = 10 # Size of entry widget

        # Create window
        self.window = tk.Tk()
        self.window.title("Iteration2 Helper")

        # Create top frame.
        self.top_frame = tk.Frame(self.window, 
            borderwidth = 1, relief = 'solid',
            height = 200, width = 300)
        self.top_frame.grid(row = 1, column = 1)
        self.top_frame.grid_propagate(False)

        # Create bottom frame.
        self.bottom_frame = tk.Frame(self.window, 
            borderwidth = 1, relief = 'solid',
            height = 200, width = 300)
        self.bottom_frame.grid(row = 2, column = 1)
        self.bottom_frame.grid_propagate(False)

         # Put a checkbox in the top frame.  Make the default
         # on.
        self.checkbox_var = tk.BooleanVar()
        self.checkbox_var.set(True)
        self.checkbox = tk.Checkbutton(self.top_frame, text="Checkbox", 
                            var = self.checkbox_var)
        self.checkbox.grid(row = 1, column = 1, sticky = tk.W, padx = self.PADDING)

        # Put an entry widget to the right
        self.entry_var = tk.StringVar()
        self.entry  = tk.Entry(self.top_frame, textvariable=self.entry_var, width = self.ENTRY_SIZE)
        self.entry.grid(row = 1, column=2, padx = self.PADDING)

        # Center row 1 in the frame.
        self.top_frame.grid_rowconfigure(1, weight = 1)

        # Arrange spread out (columnwise) the checkbox and entry box.
        self.top_frame.grid_columnconfigure(0, weight = 1)
        self.top_frame.grid_columnconfigure(1, weight = 1)
        self.top_frame.grid_columnconfigure(2, weight = 1)
        self.top_frame.grid_columnconfigure(3, weight = 1)

        # Put a button in the bottom frame
        button  = tk.Button(self.bottom_frame, text = "Button", command = self.button_handler)
        button.grid(row = 1, column=1)

        # Center the button in its frame
        self.bottom_frame.grid_rowconfigure(1, weight = 1)
        self.bottom_frame.grid_columnconfigure(1, weight = 1)
        
        # Start event loop
        self.window.mainloop()

    def button_handler(self):
        """
        Disables the checkbox and entry field.

        Prints out the state of the checkbox,
        and the contents of the entry field.
        """
        self.checkbox['state'] = 'disabled'
        self.entry['state'] = 'disabled'
        print(f"Button status = {self.checkbox_var.get()}")
        print(f"Entry = {self.entry_var.get()}")
        

if __name__ == "__main__":
   Iteration2Helper()