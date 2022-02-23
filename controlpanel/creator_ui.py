from tkinter import Button
from config.ui_Config import  *

def generate_selector_ui(window_obj):
    window_obj.title(ui_config.TITLE)
    window_obj.geometry(ui_config.GEOMETRY)
    window_obj.resizable(0,0)
    window_obj.config(
        bg = '#C5C5C5'
    )

    b1 = Button(window_obj, text= buttom_cfg.BUTTOM_1_NAME).pack(padx= 0, pady= 0)
    b2 = Button(window_obj, text= buttom_cfg.BUTTOM_2_NAME).pack(padx= 10, pady= 0)
    b3 = Button(window_obj, text= buttom_cfg.BUTTOM_3_NAME).pack(padx= 0, pady= 10)
    b4 = Button(window_obj, text= buttom_cfg.BUTTOM_4_NAME).pack(padx= 10, pady= 10)