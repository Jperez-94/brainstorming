from tkinter import Tk
from config.words_cfg import *

# Author: Jperez-94
# Version: v1.0.0

class App():
    # Number of words selected
    numOfWords = 0
    # Instances Tkinter object
    ui_window = Tk()
    # Items added to Tkinter object related to services
    ui_items = []
    # Items added to Tkinter object not related to services
    noServiceItems = 0
    # Words inserted throught UI
    words = []
    # Flag to indicate something worked wrong
    flag_warning = False
    # Error message
    error_msg = ''

    def set_wordSelection(self, button_id) -> None:
        self.numOfWords = button_id
        self.destroy_all_items()
        self.destroy_ui_window()
        
    def destroy_all_items(self) -> None:
        for item in self.ui_items:
            item.destroy()
        
        self.ui_items = []
        self.noServiceItems = 0

    def destroy_ui_window(self) -> None:
        self.ui_window.destroy()

    def getAndCheckWords(self) -> None:
        for _ in range(self.numOfWords):
            try:
                word = int(self.ui_items[_].get())
            except:
                self.flag_warning = True
                self.error_msg = 'Input is not a number'
                break

            if word < 0 or word > 4294967295:
                self.flag_warning = True
                self.error_msg = 'Input number is out of range. Valid range 0 to 4294967295'
                break
            
            self.words.append(word)

    def refresh_panel(self) -> None:
        self.ui_items[self.numOfWords + 1].config(text = '')
        self.getAndCheckWords()

        if self.flag_warning:
            self.ui_items[self.numOfWords + 1].config(text = self.error_msg)
            self.error_msg = ''
            self.flag_warning = False
            return
        
        counter = 0
        for word in self.words:
            for bit in range(32):
                if (word >> bit) & 1:
                    self.ui_items[bit + self.noServiceItems + counter * service_cfg.WORD_LENGTH].config(
                        fg = service_cfg.BIT_1_COLOR, font = service_cfg.BIT_1_FONT)
                else:
                    self.ui_items[bit + self.noServiceItems + counter * service_cfg.WORD_LENGTH].config(
                        fg = service_cfg.BIT_0_COLOR, font = service_cfg.BIT_0_FONT)
            
            counter += 1
        
        self.words = []
