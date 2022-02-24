from tkinter import Tk

class App():
    numOfWords = 0
    ui_window = Tk()
    ui_items = []

def set_wordSelection(app, button_id) -> None:
    app.numOfWords = button_id
    destroy_all_items(app)
    destroy_ui_window(app)
    

def destroy_all_items(app) -> None:
    for item in app.ui_items:
        item.destroy()
    
    app.ui_items = []

def destroy_ui_window(app) -> None:
    app.ui_window.destroy()
