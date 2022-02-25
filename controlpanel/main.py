import creator_ui
import features
from tkinter import Tk
# Parte gráfica del programa

def main():

    appData = features.App()
    creator_ui.generate_selector_ui(appData)

    appData.ui_window.mainloop()
    
    appData.ui_window = Tk()
    creator_ui.generate_status_panel(appData)

    appData.ui_window.mainloop()

    # Generate new window using saved number as parameter


if __name__ == '__main__':
    main()