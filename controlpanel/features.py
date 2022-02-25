from tkinter import Tk


class App():
    numOfWords = 0
    ui_window = Tk()
    ui_items = []
    words = []
    flag_warning = False
    error_msg = ''

    def set_wordSelection(self, button_id) -> None:
        self.numOfWords = button_id
        self.destroy_all_items()
        self.destroy_ui_window()
        

    def destroy_all_items(self) -> None:
        for item in self.ui_items:
            item.destroy()
        
        self.ui_items = []

    def destroy_ui_window(self) -> None:
        self.ui_window.destroy()

    def getAndCheckWords(self):
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

    def refresh_panel(self):
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
                    self.ui_items[bit + self.numOfWords + 2 + counter * 32].config(fg = '#DC0000')
                else:
                    self.ui_items[bit + self.numOfWords + 2 + counter * 32].config(fg = '#00920D')
            
            counter += 1
        
        self.words = []
