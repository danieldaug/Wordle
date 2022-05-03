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
from tkinter.tix import Tree

class Iteration2Helper:
    def __init__(self):
        """
        Initialize the window with frames and widgets.
        """
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
        self.Iteration_2()
        
        self.window.mainloop()

    def Iteration_1(self):
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
    
        self.parameter_frame = tk.Frame(self.control_frame,
            borderwidth = 1, relief = 'solid',
            height = self.CONTROL_FRAME_HEIGHT/3, width = self.CONTROL_FRAME_WIDTH)
        self.parameter_frame.grid(row = 1, column = 0)
        self.parameter_frame.grid_propagate(False)
    
        self.message_frame = tk.Frame(self.control_frame,
            borderwidth = 1, relief = 'solid',
            height = self.CONTROL_FRAME_HEIGHT/3, width = self.CONTROL_FRAME_WIDTH)
        self.message_frame.grid(row = 0, column = 0)
        self.message_frame.grid_propagate(False)
    
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
       
    def Iteration_2(self):
        # Constants
        self.PADDING = 10 # Padding around widgets
        self.ENTRY_SIZE = 10 # Size of entry widget

        #Add words to short list and long list
        self.list_pop()

        self.parameter_frame.rowconfigure(0,weight=2)
        self.parameter_frame.rowconfigure(5,weight=2)
        
        self.message_frame.rowconfigure(0,weight=2)
        self.message_frame.rowconfigure(5,weight=2)
        self.message_frame.columnconfigure(0,weight=2)
        self.message_frame.columnconfigure(2,weight=2)
        
        self.button_frame.columnconfigure(0,weight=2)
        self.button_frame.columnconfigure(3,weight=2)
        self.button_frame.rowconfigure(0,weight=2)
        self.button_frame.rowconfigure(2,weight=2)
        # Create hard mode check button
        self.hard_mode_checkbox_var = tk.BooleanVar()
        self.hard_mode_checkbox_var.set(False)
        self.hard_mode_checkbutton = tk.Checkbutton(self.parameter_frame, text = "Hard Mode", var = self.hard_mode_checkbox_var)
        self.hard_mode_checkbutton.grid(row = 1, column = 0, padx = self.PADDING, sticky = "W")

        # Create guesses must be words check button
        self.guesses_must_be_words_checkbox_var = tk.BooleanVar()
        self.guesses_must_be_words_checkbox_var.set(True)
        self.guesses_must_be_words_checkbutton = tk.Checkbutton(self.parameter_frame, text = "Guesses must be words", var = self.guesses_must_be_words_checkbox_var)
        self.guesses_must_be_words_checkbutton.grid(row = 2, column = 0, padx = self.PADDING, sticky = "W")
        
        # Create show word check button
        self.show_word_checkbox_var = tk.BooleanVar()
        self.show_word_checkbox_var.set(False)
        self.show_word_checkbutton = tk.Checkbutton(self.parameter_frame, text = "Show word", var = self.show_word_checkbox_var)
        self.show_word_checkbutton.grid(row = 3, column = 0, padx = self.PADDING, sticky = "W")

        # Create specify word check button
        self.specify_word_checkbox_var = tk.BooleanVar()
        self.specify_word_checkbox_var.set(False)
        self.specify_word_checkbutton = tk.Checkbutton(self.parameter_frame, text = "Specify word", var = self.specify_word_checkbox_var)
        self.specify_word_checkbutton.grid(row = 4, column = 0, padx = self.PADDING, sticky = "W")

        # Create text entry for specify word 
        self.specify_word_entry_var = tk.StringVar()
        self.specify_word_entry = tk.Entry(self.parameter_frame, width = self.ENTRY_SIZE, textvariable = self.specify_word_entry_var)
        self.specify_word_entry.grid(row = 4, column = 1)

        self.hidden_word=tk.StringVar()
        self.show_word_text=tk.Label(self.parameter_frame,textvariable=self.hidden_word)
        self.show_word_text.grid(row=3,column=1)
        
        self.message_var=tk.StringVar()
        self.message=tk.Label(self.message_frame,textvariable=self.message_var)
        self.message.grid(row=1,column=1)

        self.start_button=tk.Button(self.button_frame,text="Start Game")
        self.start_button.grid(row=1,column=1)
        self.quit_button=tk.Button(self.button_frame,text="Quit")
        self.quit_button.grid(row=1,column=2)

    def list_pop(self):
        self.long_list=[]
        self.short_list=[]
        f=open("long_wordlist.txt")
        for lines in f:
            line=lines.strip()
            if len(line)==self.WORD_SIZE:
                self.long_list.append(line)
        f.close()
        f=open("short_wordlist.txt")
        for lines in f:
            line=lines.strip()
            if len(line)==self.WORD_SIZE:
                self.short_list.append(line)
        f.close()

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