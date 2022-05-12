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
        """Initialize variables and window"""
        self.WORD_SIZE = 5  # number of letters in the hidden word
        self.NUM_GUESSES = 6 # number of guesses that the user gets
        self.LONG_WORDLIST_FILENAME = "long_wordlist.txt"
        self.SHORT_WORDLIST_FILENAME = "short_wordlist.txt"
 
       # Size of the frame that holds all guesses.  This is the upper left
       # frame in the window.
        self.PARENT_GUESS_FRAME_WIDTH = 750
        self.PARENT_GUESS_FRAME_HEIGHT = 500
 
       # Parameters for an individual letter in the guess frame
       # A guess frame is an individual box that contains a guessed letter.
        self.GUESS_FRAME_SIZE = 50  # the width and height of the guess box.
        self.GUESS_FRAME_PADDING = 3
        self.GUESS_FRAME_BG_BEGIN = 'white' # background color of a guess box
                                           # after the user enters the letter,
                                           # but before the guess is entered.
        self.GUESS_FRAME_TEXT_BEGIN = 'black' # color of text in guess box after the
                                           # user enters the letter, but before
                                           # the guess is entered.
        self.GUESS_FRAME_BG_WRONG = 'grey'  # background color of guess box
                                           # after the guess is entered, and the
                                           # letter is not in the hidden word.
        self.GUESS_FRAME_BG_CORRECT_WRONG_LOC = 'orange' # background color
                                           # guess box after the guess is entered
                                           # and the letter is in the hidden word
                                           # but in the wrong location.
        self.GUESS_FRAME_BG_CORRECT_RIGHT_LOC = 'green' # background color
                                           # guess box after the guess is entered
                                           # and the letter is in the hidden word
                                           # and in the correct location.
        self.GUESS_FRAME_TEXT_AFTER = 'white' # color of text in guess box after
                                           # the guess is entered.
        self.FONT_FAMILY = 'ariel'          # Font to use for letters in the guess boxes.
        self.FONT_SIZE_GUESS = 35           # Font size for letters in the guess boxes.
 
       # Parameters for the keyboard frame
        self.KEYBOARD_FRAME_HEIGHT = 200
        self.KEYBOARD_BUTTON_HEIGHT = 2
        self.KEYBOARD_BUTTON_WIDTH = 3  # width of the letter buttons.  Remember,
                                       # width of buttons is measured in characters.
        self.KEYBOARD_BUTTON_WIDTH_LONG = 5 # width of the enter and back buttons.
 
       # The following colors for the keyboard buttons
       # follow the same specifications as the colors defined above for the guess
       # boxes.  The problem is that if one or both of you have a mac, you will
       # not be able to change the background color of a button.  In this case,
       # just change the color of the text in the button, instead of the background color.
       # So the text color starts as the default (black), and then changes to grey, orange,
       # green depending on the result of the guess for that letter.
        self.KEYBOARD_BUTTON_BG_BEGIN = 'white'
        self.KEYBOARD_BUTTON_TEXT_BEGIN = 'black'
        self.KEYBOARD_BUTTON_BG_WRONG = 'grey' 
        self.KEYBOARD_BUTTON_BG_CORRECT_WRONG_LOC = 'orange'
        self.KEYBOARD_BUTTON_BG_CORRECT_RIGHT_LOC = 'green'
        self.KEYBOARD_BUTTON_TEXT_AFTER = 'white'
 
        self.KEYBOARD_BUTTON_NAMES = [  
           ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
           ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
           ["ENTER", "Z", "X", "C", "V", "B", "N", "M", "BACK"]]
      
       # Parameters for the control frame
        self.CONTROL_FRAME_HEIGHT = self.PARENT_GUESS_FRAME_HEIGHT + self.KEYBOARD_FRAME_HEIGHT
        self.CONTROL_FRAME_WIDTH = 300
        self.USER_SELECTION_PADDING = 10  # Horizontal padding on either side of the widgets in
                                           # the parameter frame.
 
        self.MESSAGE_DISPLAY_TIME_SECS = 5 # Length of time the message should be
                                           # displayed.
        self.PROCESS_GUESS_WAITTIME = 1  # When processing a guess (changing color
                                       # of the guess frames), time to wait between
                                       # updating successive frames.

        self.Iteration_1()
        # Start event loop
        self.window.mainloop()
      
    def Iteration_1(self):
       """ Implements all steps of Iteration 1"""
       # Create window
       self.window = tk.Tk()
       self.window.title("Wordy")
 
       # Create a frame.
       self.guess_frame = tk.Frame(self.window,
           borderwidth = 1, relief = 'solid',
           height = self.PARENT_GUESS_FRAME_HEIGHT, width = self.PARENT_GUESS_FRAME_WIDTH)
       self.guess_frame.grid(row = 0, column = 0)
       self.guess_frame.grid_propagate(False)
 
       # Put a frame to the right of it.
       self.control_frame = tk.Frame(self.window,
           borderwidth = 1, relief = 'solid',
           height = self.CONTROL_FRAME_HEIGHT, width = self.CONTROL_FRAME_WIDTH)
       self.control_frame.grid(row = 0, column = 1,rowspan=2)
       self.control_frame.grid_propagate(False)

       # Create parameter frame inside control frame
       self.parameter_frame = tk.Frame(self.control_frame,
           borderwidth = 1, relief = 'solid',
           height = self.CONTROL_FRAME_HEIGHT/3, width = self.CONTROL_FRAME_WIDTH)
       self.parameter_frame.grid(row = 1, column = 0)
       self.parameter_frame.grid_propagate(False)

       # Create message frame inside control frame
       self.message_frame = tk.Frame(self.control_frame,
           borderwidth = 1, relief = 'solid',
           height = self.CONTROL_FRAME_HEIGHT/3, width = self.CONTROL_FRAME_WIDTH)
       self.message_frame.grid(row = 0, column = 0)
       self.message_frame.grid_propagate(False)

       # Create button frame inside control frame
       self.button_frame = tk.Frame(self.control_frame,
           borderwidth = 1, relief = 'solid',
           height = self.CONTROL_FRAME_HEIGHT/3, width = self.CONTROL_FRAME_WIDTH)
       self.button_frame.grid(row = 2, column = 0)
       self.button_frame.grid_propagate(False)
 
 
       # Put a frame below the top two.
       self.keyboard_frame = tk.Frame(self.window,
           borderwidth = 1, relief = 'solid',
           height = self.KEYBOARD_FRAME_HEIGHT, width = self.PARENT_GUESS_FRAME_WIDTH)
       self.keyboard_frame.grid(row = 1, column = 0)
       self.keyboard_frame.grid_propagate(False)
 
if __name__ == "__main__":
  Iteration1Helper()
