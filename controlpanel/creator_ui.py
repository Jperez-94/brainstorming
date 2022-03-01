from tkinter import Button, Label, Entry
from config.ui_Config import  *
from config.words_cfg import *

# Author: Jperez-94
# Version: v1.0.0


def generate_selector_ui(app) -> None:
    app.ui_window.title(ui_config.SELECTOR_TITLE)
    app.ui_window.geometry(ui_config.SELECTOR_GEOMETRY)
    app.ui_window.resizable(0,0)
    app.ui_window.config(
        bg = '#C5C5C5'
    )

    bt1 = Button(
        app.ui_window,
        command = lambda: app.set_wordSelection(1),
        text= button_cfg.BUTTON_1_NAME,
        width = button_cfg.WIDTH,
        height= button_cfg.HEIGHT)

    bt2 = Button(
        app.ui_window,
        command = lambda: app.set_wordSelection(2),
        text= button_cfg.BUTTON_2_NAME,
        width = button_cfg.WIDTH,
        height= button_cfg.HEIGHT)

    bt3 = Button(
        app.ui_window,
        command = lambda: app.set_wordSelection(3),
        text= button_cfg.BUTTON_3_NAME,
        width = button_cfg.WIDTH,
        height= button_cfg.HEIGHT)

    bt4 = Button(
        app.ui_window,
        command = lambda: app.set_wordSelection(4),
        text= button_cfg.BUTTON_4_NAME,
        width = button_cfg.WIDTH,
        height= button_cfg.HEIGHT)
    
    app.ui_items.append(bt1)
    app.ui_items.append(bt2)
    app.ui_items.append(bt3)
    app.ui_items.append(bt4)
    app.noServiceItems += 4

    bt1.pack(padx= button_cfg.BUTTON_1_PADX, pady= button_cfg.BUTTON_1_PADY)
    bt2.pack(padx= button_cfg.BUTTON_2_PADX, pady= button_cfg.BUTTON_2_PADY)
    bt3.pack(padx= button_cfg.BUTTON_3_PADX, pady= button_cfg.BUTTON_3_PADY)
    bt4.pack(padx= button_cfg.BUTTON_4_PADX, pady= button_cfg.BUTTON_4_PADY)


def generate_status_panel(app) -> None:
    app.ui_window.title(ui_config.PANEL_TITLE)

    if app.numOfWords == 1:
        geometry = "300x800"
    else:
        geometry = f"{200 * app.numOfWords}x800"

    app.ui_window.geometry(geometry)
    app.ui_window.resizable(0,0)
    app.ui_window.config(
        bg = '#C5C5C5'
    )

    # Entry boxes, one to each word. Position in the array ui_items[0:(numOfWords -1)]
    for _ in range(app.numOfWords):
        app.ui_items.append(
            Entry()
        )

    app.noServiceItems += app.numOfWords
    
    # Button to refresh the panel. Position in the array ui_items[numOfWords]
    app.ui_items.append(
        Button(text= button_cfg.BUTTON_REFRESH_NAME, command = lambda: app.refresh_panel())
    )

    app.noServiceItems += 1

    # Error message label. Position in the array ui_items[numOfWords + 1]
    app.ui_items.append(
        Label(text = '')
    )

    app.noServiceItems += 1

    # Label generator, one label to each enable service
    numOfServicies = app.numOfWords * service_cfg.WORD_LENGTH
    for _ in range(numOfServicies):
        app.ui_items.append(
            Label(text= service_cfg.serviceNameList[_])
        )
    
    # Add columns form by Entry and the services of the word
    counter = 0
    for column in range(app.numOfWords):
        app.ui_items[column].grid(padx = ui_config.ITEM_PADX, row = 0, column = column)
        for row in range(len(app.ui_items) - app.numOfWords - 1):
            if ((row) % service_cfg.WORD_LENGTH) == 0 and row != 0:
                counter += 1
                break
            
            app.ui_items[row + app.noServiceItems + counter * service_cfg.WORD_LENGTH].grid(row = row + 1, column = column)

    # Add Refresh button to the grid
    app.ui_items[app.noServiceItems - 2].grid(padx = ui_config.ITEM_PADX, row = 0, column = app.noServiceItems - 1)
    # Add Label message error to the grid
    app.ui_items[app.noServiceItems - 1].grid(padx = ui_config.ITEM_PADX, row = 1, column =  app.noServiceItems - 1)
