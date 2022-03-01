import creator_ui
import features
from tkinter import Tk

# Author: Jperez-94
# Version: v1.0.0

def main():

    appData = features.App()
    creator_ui.generate_selector_ui(appData)

    appData.ui_window.mainloop()
    
    appData.ui_window = Tk()
    creator_ui.generate_status_panel(appData)

    appData.ui_window.mainloop()


if __name__ == '__main__':
    main()