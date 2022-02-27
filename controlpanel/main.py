import creator_ui
import features
from tkinter import Tk

def main():

    appData = features.App()
    creator_ui.generate_selector_ui(appData)

    appData.ui_window.mainloop()
    
    appData.ui_window = Tk()
    creator_ui.generate_status_panel(appData)

    appData.ui_window.mainloop()


if __name__ == '__main__':
    main()