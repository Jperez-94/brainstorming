import creator_ui
import features
# Parte gráfica del programa

def main():

    appData = features.App()
    creator_ui.generate_selector_ui(appData)

    appData.ui_window.mainloop()

    # Save number of words chosen

    # Clean window

    # Generate new window using saved number as parameter


if __name__ == '__main__':
    main()