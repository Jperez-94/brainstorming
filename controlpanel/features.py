from tkinter import Tk

class App():
    numOfWords = 0
    ui_window = Tk()

def set_wordSelection(appData, button_id):
    appData.numOfWords = button_id
    print(appData.numOfWords)

