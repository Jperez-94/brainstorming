from tkinter import Button
from config.ui_Config import  *
import features

def generate_selector_ui(app):
    app.ui_window.title(ui_config.TITLE)
    app.ui_window.geometry(ui_config.GEOMETRY)
    app.ui_window.resizable(0,0)
    app.ui_window.config(
        bg = '#C5C5C5'
    )

    Button(
        app.ui_window,
        command = lambda: features.set_wordSelection(app, 1),
        text= button_cfg.BUTTON_1_NAME,
        width = button_cfg.WIDTH,
        height= button_cfg.HEIGHT).pack(padx= button_cfg.BUTTON_1_PADX, pady= button_cfg.BUTTON_1_PADY)

    Button(
        app.ui_window,
        command = lambda: features.set_wordSelection(app, 2),
        text= button_cfg.BUTTON_2_NAME,
        width = button_cfg.WIDTH,
        height= button_cfg.HEIGHT).pack(padx= button_cfg.BUTTON_2_PADX, pady= button_cfg.BUTTON_2_PADY)

    Button(
        app.ui_window,
        command = lambda: features.set_wordSelection(app, 3),
        text= button_cfg.BUTTON_3_NAME,
        width = button_cfg.WIDTH,
        height= button_cfg.HEIGHT).pack(padx= button_cfg.BUTTON_3_PADX, pady= button_cfg.BUTTON_3_PADY)

    Button(
        app.ui_window,
        command = lambda: features.set_wordSelection(app, 4),
        text= button_cfg.BUTTON_4_NAME,
        width = button_cfg.WIDTH,
        height= button_cfg.HEIGHT).pack(padx= button_cfg.BUTTON_4_PADX, pady= button_cfg.BUTTON_4_PADY)