from tkinter import Button, Label, Entry
from config.ui_Config import  *
from config.words_cfg import *
import features

def generate_selector_ui(app):
    app.ui_window.title(ui_config.SELECTOR_TITLE)
    app.ui_window.geometry(ui_config.SELECTOR_GEOMETRY)
    app.ui_window.resizable(0,0)
    app.ui_window.config(
        bg = '#C5C5C5'
    )

    bt1 = Button(
        app.ui_window,
        command = lambda: features.set_wordSelection(app, 1),
        text= button_cfg.BUTTON_1_NAME,
        width = button_cfg.WIDTH,
        height= button_cfg.HEIGHT)

    bt2 = Button(
        app.ui_window,
        command = lambda: features.set_wordSelection(app, 2),
        text= button_cfg.BUTTON_2_NAME,
        width = button_cfg.WIDTH,
        height= button_cfg.HEIGHT)

    bt3 = Button(
        app.ui_window,
        command = lambda: features.set_wordSelection(app, 3),
        text= button_cfg.BUTTON_3_NAME,
        width = button_cfg.WIDTH,
        height= button_cfg.HEIGHT)

    bt4 = Button(
        app.ui_window,
        command = lambda: features.set_wordSelection(app, 4),
        text= button_cfg.BUTTON_4_NAME,
        width = button_cfg.WIDTH,
        height= button_cfg.HEIGHT)
    
    app.ui_items.append(bt1)
    app.ui_items.append(bt2)
    app.ui_items.append(bt3)
    app.ui_items.append(bt4)

    bt1.pack(padx= button_cfg.BUTTON_1_PADX, pady= button_cfg.BUTTON_1_PADY)
    bt2.pack(padx= button_cfg.BUTTON_2_PADX, pady= button_cfg.BUTTON_2_PADY)
    bt3.pack(padx= button_cfg.BUTTON_3_PADX, pady= button_cfg.BUTTON_3_PADY)
    bt4.pack(padx= button_cfg.BUTTON_4_PADX, pady= button_cfg.BUTTON_4_PADY)


def generate_status_panel(app):
    app.ui_window.title(ui_config.PANEL_TITLE)
    app.ui_window.geometry(ui_config.PANEL_GEOMETRY)
    app.ui_window.resizable(0,0)
    app.ui_window.config(
        bg = '#C5C5C5'
    )

    for _ in range(app.numOfWords):
        app.ui_items.append(
            Entry()
        )

    numOfServicies = app.numOfWords *32
    for _ in range(numOfServicies):
        app.ui_items.append(
            Label(text= service_cfg.serviceNameList[_])
        )
    
    counter = 0
    for column in range(app.numOfWords):
        app.ui_items[column].grid(row = 0, column = column)
        for row in range(len(app.ui_items) - app.numOfWords):
            if (row % 32) == 0 and row != 0:
                counter += 1
                break
            app.ui_items[row + app.numOfWords + counter * 32].grid(row = row + 1, column = column)
