from tkinter import Tk
import creator_ui
# Parte gráfica del programa

def main():

    ui_window = Tk()
    creator_ui.generate_selector_ui(ui_window)

    ui_window.mainloop()

    # Save number of words chosen

    # Clean window

    # Generate new window using saved number as parameter


if __name__ == '__main__':
    main()