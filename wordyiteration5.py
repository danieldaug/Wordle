"""
File: iteration4Helper.py
Author: COMP 120 instructor
Date: April 25, 2021
Description: Code that handles the word enter events.
"""
import random
import tkinter as tk

import tkinter.font as font
import time

from enum import Enum

class Iteration5Helper:
    def __init__(self):
        """
        Initialize the window with frames and widgets.
        """
        self.hidden_word = ""
        self.curr_guess_row=0
        self.curr_guess_box=0
        self.curr_guess_str=""
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
        self.KEYBOARD_BUTTON_WIDTH = 5  # width of the letter buttons.  Remember,
                                        # width of buttons is measured in characters.
        self.KEYBOARD_BUTTON_WIDTH_LONG = 7 # width of the enter and back buttons.
    
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
        # Constants
        self.PADDING = 10 # Padding around widgets
        self.ENTRY_SIZE = 10 # Size of entry widget

        self.FONT_FAMILY = 'ariel'
        

        # Create window
        
        self.Iteration_1()
        self.Iteration_2()
        self.Iteration_3()
        
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
       
    def Iteration_2(self):
        """ Implements all steps of iteration 2 """
        # Constants
        self.PADDING = 10 # Padding around widgets
        self.ENTRY_SIZE = 10 # Size of entry widget

        #Add words to short list and long list
        self.list_pop()
        # Call methods to create widgets 
        self.frame_configure()
        self.hard_mode_check_button_maker()
        self.guess_must_be_word_checkbox_maker()
        self.show_word_check_button_maker()
        self.specify_word_checkbox_maker()
        self.text_entry_maker()
        self.hidden_word_label_maker()
        self.message_label_maker()
        self.start_quit_button_maker()

    def frame_configure(self):
        """ Create blanks rows so widgets will be centered in each frame """
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



    def hard_mode_check_button_maker(self):
        """ Create hard mode check button """
        self.hard_mode_checkbox_var = tk.BooleanVar()
        self.hard_mode_checkbox_var.set(False)
        self.hard_mode_checkbutton = tk.Checkbutton(self.parameter_frame, text = "Hard Mode", var = self.hard_mode_checkbox_var)
        self.hard_mode_checkbutton.grid(row = 1, column = 0, padx = self.PADDING, sticky = "W")

    def guess_must_be_word_checkbox_maker(self):
        """ Create guesses must be words check button """
        self.guesses_must_be_words_checkbox_var = tk.BooleanVar()
        self.guesses_must_be_words_checkbox_var.set(True)
        self.guesses_must_be_words_checkbutton = tk.Checkbutton(self.parameter_frame, text = "Guesses must be words", var = self.guesses_must_be_words_checkbox_var)
        self.guesses_must_be_words_checkbutton.grid(row = 2, column = 0, padx = self.PADDING, sticky = "W")
    
    def show_word_check_button_maker(self):
        """ Create show word check button """
        self.show_word_checkbox_var = tk.BooleanVar()
        self.show_word_checkbox_var.set(False)
        self.show_word_checkbutton = tk.Checkbutton(self.parameter_frame, text = "Show word", var = self.show_word_checkbox_var, command = self.show_word_check)
        self.show_word_checkbutton.grid(row = 3, column = 0, padx = self.PADDING, sticky = "W")
    
    def specify_word_checkbox_maker(self):
        """ Create specify word check button """
        self.specify_word_checkbox_var = tk.BooleanVar()
        self.specify_word_checkbox_var.set(False)
        self.specify_word_checkbutton = tk.Checkbutton(self.parameter_frame, text = "Specify word", var = self.specify_word_checkbox_var)
        self.specify_word_checkbutton.grid(row = 4, column = 0, padx = self.PADDING, sticky = "W")

    def text_entry_maker(self):
        """ Create text entry for specify word """
        self.specify_word_entry_var = tk.StringVar()
        self.specify_word_entry = tk.Entry(self.parameter_frame, width = self.ENTRY_SIZE, textvariable = self.specify_word_entry_var)
        self.specify_word_entry.grid(row = 4, column = 1)

    def hidden_word_label_maker(self):
        """ Create label for hidden word """
        self.hidden_word_var=tk.StringVar()
        self.show_word_text=tk.Label(self.parameter_frame,textvariable=self.hidden_word_var)
        self.show_word_text.grid(row=3,column=1)
        
    def message_label_maker(self):
        """ Create label to display messages """
        self.message_var=tk.StringVar()
        self.message=tk.Label(self.message_frame,textvariable=self.message_var)
        self.message.grid(row=1,column=1)

    def start_quit_button_maker(self):
        """ Create start and quit buttons """
        self.start_button=tk.Button(self.button_frame,text="Start Game", command = self.start_button_handler)
        self.start_button.grid(row=1,column=1)
        self.quit_button=tk.Button(self.button_frame,text="Quit", command = self.quit)
        self.quit_button.grid(row=1,column=2)


    def Iteration_3(self):
        """ Implements all steps of iteration 3 """
        self.FONT = font.Font(family=self.FONT_FAMILY)
        self.button_text = [["Q", "W", "E","R","T","Y","U","I","O","P"],
                        ["A", "S", "D","F","G","H","J","K","L"],
                        ["ENTER","Z", "X", "C","V","B","N","M","BACK"]]
       
        self.keyboard_frame.rowconfigure(0, weight = 1)
        self.keyboard_frame.rowconfigure(len(self.button_text) + 1, weight = 1)
        self.keyboard_frame.columnconfigure(0, weight = 1)
        self.keyboard_frame.columnconfigure(len(self.button_text[0]) + 1, weight = 1)
        self.guess_frame.rowconfigure(0, weight = 1)
        self.guess_frame.rowconfigure(self.NUM_GUESSES + 1, weight = 1)
        self.guess_frame.columnconfigure(0, weight = 1)
        self.guess_frame.columnconfigure(self.WORD_SIZE + 1, weight = 1)
        self.buttons = {}
        self.button_text_color = self.KEYBOARD_BUTTON_TEXT_BEGIN
        self.create_keyboard_buttons()
        self.create_guess_widgets()

    def create_keyboard_buttons(self):
        """Creates all the keyboard button widgets in the button frame"""
        for r in range(len(self.button_text)):
            # Create frame for each row of buttons
            frame=tk.Frame(self.keyboard_frame,width=self.PARENT_GUESS_FRAME_WIDTH,height=self.KEYBOARD_FRAME_HEIGHT/3)
            frame.grid(row=r+1,column=1)
            frame.rowconfigure(0, weight = 1)
            frame.rowconfigure(len(self.button_text) + 1, weight = 1)
            frame.columnconfigure(0, weight = 1)
            frame.columnconfigure(len(self.button_text[0]) + 1, weight = 1)
            for c in range(len(self.button_text[r])):

                # Define a handler for this button.
                # Note that functions can be dynamically 
                # defined, as is happening here.  Each
                # button gets its own hander.  
                # But each handler calls the same method
                # (button_handler), but with a parameter
                # that specifies which button was pressed.

                # Special case for enter or back buttons
                if self.button_text[r][c]=="ENTER" or self.button_text[r][c]=="BACK":
                    if self.button_text[r][c]=="ENTER":
                        def handler(key = self.button_text[r][c]):
                            self.enter_handler(key)
                    else:
                        def handler(key = self.button_text[r][c]):
                            self.back_handler(key)
                    button = tk.Button(frame,
                        width = self.KEYBOARD_BUTTON_WIDTH_LONG,
                        text = self.button_text[r][c],
                        fg=self.button_text_color,bg=self.KEYBOARD_BUTTON_BG_BEGIN,
                        font=self.FONT,
                        command = handler)
                else:
                    def handler(key = self.button_text[r][c]):
                        self.button_handler(key)
                    button = tk.Button(frame,
                            width = self.KEYBOARD_BUTTON_WIDTH,
                            text = self.button_text[r][c],
                            fg=self.button_text_color, 
                            font=self.FONT,
                            command = handler)
                button.grid(row = r + 1, column = c + 1)
                button['state'] = 'disabled'
                #Put the button in a dictionary of buttons
                #where the key is the button text, and the
                #value is the button object.
                self.buttons[self.button_text[r][c]] = button

    def create_guess_widgets(self):
        """Creates the labels and frames widgets inside the guess frame"""
        self.guess_widget_list=[]
        for r in range(self.NUM_GUESSES):
            templist=[]
            for c in range(self.WORD_SIZE):
                # Create current frame in row (r) and column (c)
                guessframe = tk.Frame(self.guess_frame,
                            height = self.GUESS_FRAME_SIZE,
                            width = self.GUESS_FRAME_SIZE,
                            bg = self.GUESS_FRAME_BG_BEGIN, 
                            borderwidth = 1, relief = 'solid'
                            )
                guessframe.grid(row = r + 1, column = c + 1, padx = self.GUESS_FRAME_PADDING, pady = self.GUESS_FRAME_PADDING)
                guessframe.grid_columnconfigure(0,weight=1)
                guessframe.grid_columnconfigure(2,weight=1)
                
                guessframe.grid_propagate(False)
                # Create a stringvar and label to correspond to the current box
                temptext=tk.StringVar()
                letter=tk.Label(guessframe,height=1,
                textvariable=temptext,
                fg=self.GUESS_FRAME_TEXT_BEGIN,
                font=(self.FONT_FAMILY,self.FONT_SIZE_GUESS))
        
                letter.grid(row=1,column=1)

                templist.append((guessframe,letter,temptext))
            # Make list containing the frame,label, and stringvar
            self.guess_widget_list.append(templist)
              

    def enter_handler(self, text):
        """Handles the user input of the enter button being clicked"""
        print("Hit enter button")
        self.create_word_dict()
        # Make sure guess is correct length
        if len(self.curr_guess_str)!=self.WORD_SIZE:
            self.message_display("Word not finished")
            return
        # Make sure word is valid if the parameter is true
        elif self.guesses_must_be_words_parameter==True and self.curr_guess_str.lower() not in self.long_list:
            self.message_display(self.curr_guess_str+" is not in the word list")
        else:
            self.enter_events()
            # Check if guess is correct
            if self.curr_guess_str.lower() == self.hidden_word:
                self.message_display("Correct. Nice job. Game over")
                for (guessframe,letter,lettertext) in self.guess_widget_list[self.curr_guess_row]:
                    guessframe.configure(bg="green")
                    letter.configure(bg="green",fg=self.GUESS_FRAME_TEXT_AFTER)
            else:
                # Increment row and reset string and current box
                self.curr_guess_row+=1
                self.curr_guess_box=0
                self.curr_guess_str=""
        # Check if last guess was used
        if self.curr_guess_row == self.NUM_GUESSES and self.curr_guess_str.lower() != self.hidden_word:
            self.message_display("Guesses used up. Word was " + self.hidden_word + ". Game over")
    
    def create_word_dict(self):
        self.word_dict = {}
        for letter in self.curr_guess_str:
            self.word_dict[letter] = self.word_dict.get(letter,0) + 1

    def color_guess_boxes(self):
        pass
    
    def enter_events(self):
        for i in range(len(self.WORD_SIZE)):
            curr_letter = self.curr_guess_str[i]
            if curr_letter in self.hidden_word:
                print("a")
            else:
                self.guess_widget_list[self.curr_guess_row][i][1].configure(bg = self.GUESS_FRAME_BG_WRONG, fg = self.GUESS_FRAME_TEXT_AFTER)
                


    def back_handler(self, text):
        """Handles the user input of the back button being clicked"""
        print("Hit back button")
        if self.curr_guess_box>0:
            self.curr_guess_box-=1
            self.guess_widget_list[self.curr_guess_row][self.curr_guess_box][2].set("")
            
            self.curr_guess_str=self.curr_guess_str[:-1]
        elif self.curr_guess_box==0:
            self.guess_widget_list[self.curr_guess_row][self.curr_guess_box][2].set("")
            self.curr_guess_str=""

    def button_handler(self,text):
        """Handles the user input of the letter buttons being clicked"""
        print("Pushed the " + text + " button") 
        if self.curr_guess_box<self.WORD_SIZE:
            self.guess_widget_list[self.curr_guess_row][self.curr_guess_box][2].set(text)
            self.curr_guess_box+=1
            self.curr_guess_str+=text

    def list_pop(self):
        """ Populates the long_list and short_list from their respective text files """

        self.long_list=[]
        self.short_list=[]
        f=open("long_wordlist.txt")
        # Populates long list
        for lines in f:
            line=lines.strip()
            if len(line)==self.WORD_SIZE:
                self.long_list.append(line)
        f.close()
        # Populates short list
        f=open("short_wordlist.txt")
        for lines in f:
            line=lines.strip()
            if len(line)==self.WORD_SIZE:
                self.short_list.append(line)
        f.close()

    def message_display(self,message):
        """ Displays message in the message frame and clears it after amount of time """
        self.message_var.set(message)
        self.window.after(self.MESSAGE_DISPLAY_TIME_SECS*1000, self.message_clear)

    def message_clear(self):
        """ Clears the message label """
        self.message_var.set("")
    
    def start_button_handler(self):
        self.button_enabler()
        """ Checks to make sure the game can start when the button is clicked, also initializes
        all parameter variables and starts the game if valid """

        #Checks to see if user wants to specify word
        if self.specify_word_checkbox_var.get() == True:
            # Makes sure word if right length
            if len(self.specify_word_entry_var.get()) != self.WORD_SIZE:
                self.message_display("Incorrect specified word length")
                return
            # Checks to see if the guess must be word box is checked
            # If so, makes sure entry is valid
            elif self.guesses_must_be_words_checkbox_var.get() == True:
                if self.specify_word_entry_var.get() not in self.long_list:
                    self.message_display("specified word not a valid word")
                    return
            else:
                # Initialize parameter variables and disable checkboxes/entries
                self.hard_mode_parameter = self.hard_mode_checkbox_var.get()
                self.hard_mode_checkbutton['state'] = 'disabled'
                self.guesses_must_be_words_parameter = self.guesses_must_be_words_checkbox_var.get()
                self.guesses_must_be_words_checkbutton['state'] = 'disabled'
                self.show_word_parameter = self.show_word_checkbox_var.get()
                self.hidden_word = self.specify_word_entry_var.get()
                self.specify_word_checkbutton['state'] = 'disabled'
                self.start_button['state'] = 'disabled'
                self.specify_word_entry_var.set("")
        else:
            # Initialize parameter variables and disable checkboxes/entries
            self.hard_mode_parameter = self.hard_mode_checkbox_var.get()
            self.hard_mode_checkbutton['state'] = 'disabled'
            self.guesses_must_be_words_parameter = self.guesses_must_be_words_checkbox_var.get()
            self.guesses_must_be_words_checkbutton['state'] = 'disabled'
            self.show_word_parameter = self.show_word_checkbox_var.get()
            self.specify_word_checkbutton['state'] = 'disabled'
            self.start_button['state'] = 'disabled'
            # Takes random word from long_list
            self.hidden_word = self.long_list[random.randint(0, len(self.short_list))]

        if self.show_word_parameter == True:
            #display word if box is checked
            self.hidden_word_var.set(self.hidden_word)
        
        #Prints all conditions/parameters
        print("Hard Mode = " + str(self.hard_mode_parameter))
        print("Guesses must be word = " + str(self.guesses_must_be_words_parameter))
        print("Show word = " + str(self.show_word_checkbox_var.get()))
        print("Specify word = " + str(self.specify_word_checkbox_var.get()))
        print("Hidden word = " + self.hidden_word)

    def button_enabler(self):
        """Enables the keyboard buttons when the game starts"""
        for value in self.buttons.values():
            value['state'] = 'normal'

    def quit(self):
        """ Quits the window """
        self.window.destroy()

    def show_word_check(self):
        """ Checks to see if the user wants to show word """
        if self.show_word_checkbox_var.get() == True:
            self.hidden_word_var.set(self.hidden_word)
        else:
            self.hidden_word_var.set("")
if __name__ == "__main__":
   Iteration5Helper()