"""
File: iteration3Helper.py
Author: COMP 120 instructor
Date: April 25, 2021
Description: Code that illustrates creating a grid of buttons.
"""
import random
import tkinter as tk

import tkinter.font as font
import time

from enum import Enum

class Iteration3Helper:
    def __init__(self):
        """
        Initialize the window with frames and widgets.
        """
        # Constants
        self.PADDING = 10 # Padding around widgets
        self.ENTRY_SIZE = 10 # Size of entry widget

        self.FONT_FAMILY = 'ariel'
        

        # Create window
        self.window = tk.Tk()
        self.window.title("Iteration2 Helper")
        self.window.geometry("600x600") # make window big

        # Create font.
        self.FONT = font.Font(family=self.FONT_FAMILY)

        # Create frame for the buttons.
        self.button_frame = tk.Frame(self.window, 
            borderwidth = 1, relief = 'solid',
            height = 200, width = 300)
        self.button_frame.grid(row = 1, column = 1)
        self.button_frame.grid_propagate(False)

        # Center the frame in the window
        self.window.rowconfigure(0, weight = 1)
        self.window.rowconfigure(2, weight = 1)
        self.window.columnconfigure(0, weight = 1)
        self.window.columnconfigure(2, weight = 1)

        # Define text to go in the buttons
        self.button_text = [["a", "b", "c"],
                        ["d", "e", "f"],
                        ["g", "h", "i"],
                        ["j", "k", "l"]]
        self.buttons = {}
        self.button_width = 5
        self.button_text_color = 'blue'

        # Create the buttons.
        for r in range(len(self.button_text)):
            for c in range(len(self.button_text[r])):

                # Define a handler for this button.
                # Note that functions can be dynamically 
                # defined, as is happening here.  Each
                # button gets its own hander.  
                # But each handler calls the same method
                # (button_handler), but with a parameter
                # that specifies which button was pressed.
                def handler(key = self.button_text[r][c]):
                    self.button_handler(key)
                button = tk.Button(self.button_frame,
                        width = self.button_width,
                        text = self.button_text[r][c],
                        fg=self.button_text_color, 
                        font=self.FONT,
                        command = handler)
                button.grid(row = r + 1, column = c + 1)

                # Put the button in a dictionary of buttons
                # where the key is the button text, and the
                # value is the button object.
                self.buttons[self.button_text[r][c]] = button

        # Center the grid of buttons in the button frame
        self.button_frame.rowconfigure(0, weight = 1)
        self.button_frame.rowconfigure(len(self.button_text) + 1, weight = 1)
        self.button_frame.columnconfigure(0, weight = 1)
        self.button_frame.columnconfigure(len(self.button_text[0]) + 1, weight = 1)

        # Start event loop
        self.window.mainloop()

    def button_handler(self, text):
        """
        Changes the color of the button that was pressed
        """
        self.buttons[text]['fg'] = 'red'

if __name__ == "__main__":
   Iteration3Helper()