from tkinter import *
from default import WindowConfig, PrincipalFrame, AddFrame, ChooseFrame


class Main_Window():
    def __init__(self):
        self.mainwindow = Tk()
        self._principalFrame = Frame(self.mainwindow)
        self._addEntryFrame = Frame(self.mainwindow)
        self._chooseFrame = Frame(self.mainwindow)
        self.mainwindow.title(WindowConfig.mainWindowTitle)
        self.mainwindow.geometry(WindowConfig.mainWindowGeometry)
        self.mainwindow.config(
            bg = WindowConfig.mainWindowBgColor
        )
        self._configPrincipalFrame()
        self._configAddEntryFrame()
        self._configChooseFrame()
        self._principalFrame.pack()

    def _configPrincipalFrame(self):
        chooseButton = Button(
            self._principalFrame,
            text= PrincipalFrame.chooseButtonText,
            command= lambda:(
                self._unpackAllFrames(),
                self._chooseFrame.pack()
            )
        )
        showButton = Button(
            self._principalFrame,
            text = PrincipalFrame.showButtonText,
            command = lambda:(
                self._unpackAllFrames()
            )
        )
        addButton = Button(
            self._principalFrame,
            text = PrincipalFrame.addButtonText,
            command = lambda:(
                self._unpackAllFrames(),
                self._addEntryFrame.pack()
            )
        )
        checkButton = Button(
            self._principalFrame,
            text = PrincipalFrame.checkButtonText,
            command = lambda:(
                self._unpackAllFrames()
            )
        )

        chooseButton.pack()
        showButton.pack()
        addButton.pack()
        checkButton.pack()

    def _configAddEntryFrame(self):
        cancelButton = Button(
            self._addEntryFrame,
            text = AddFrame.cancelButtonText,
            command = lambda:(
                self._unpackAllFrames(),
                self._principalFrame.pack()
            )
        )

        cancelButton.pack()
    
    def _configChooseFrame(self):
        cancelButton = Button(
            self._chooseFrame,
            text = ChooseFrame.cancelButtonText,
            command = lambda:(
                self._unpackAllFrames(),
                self._principalFrame.pack()
            )
        )
        
        cancelButton.pack()
    
    def _unpackAllFrames(self):
        self._principalFrame.pack_forget()
        self._addEntryFrame.pack_forget()
        self._chooseFrame.pack_forget()

