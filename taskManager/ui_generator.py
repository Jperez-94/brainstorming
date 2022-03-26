from tkinter import *
from tkinter import ttk
from default import WindowConfig, PrincipalFrameConfig, AddTaskFrameConfig, AddDashboardFrameConfig
from dashboardmanager import *


class Main_Window():
    def __init__(self):
        self.mainwindow = Tk()
        self.principalFrame = PrincipalFrame(self)
        self.addTaskFrame = AddTaskFrame(self)
        self.addDashboardFrame = AddDashBoardFrame(self)
        self.mainwindow.title(WindowConfig.mainWindowTitle)
        self.mainwindow.geometry(WindowConfig.mainWindowGeometry)
        self.mainwindow.config(
            bg = WindowConfig.mainWindowBgColor
        )

        self.principalFrame.frame.pack()
    
    def unpackAllFrames(self):
        self.principalFrame.frame.pack_forget()
        self.addTaskFrame.frame.pack_forget()
        self.addDashboardFrame.frame.pack_forget()


class PrincipalFrame():
    def __init__(self, MainWindow):
        self._mainwindow = MainWindow
        self.frame = Frame(MainWindow.mainwindow)
        self.showButton = None
        self.addTaskButton = None
        self.addDashboardButton = None
        self.checkButton = None

        self._configPrincipalFrame()

    def _configPrincipalFrame(self):
        self.showButton = Button(
            self.frame,
            text = PrincipalFrameConfig.showButtonText,
            command = lambda:(
                self._mainwindow.unpackAllFrames()
            )
        )

        self.addTaskButton = Button(
            self.frame,
            text = PrincipalFrameConfig.addTaskButtonText,
            command = lambda:(
                self._mainwindow.unpackAllFrames(),
                getAllDashBoards(self._mainwindow),
                self._mainwindow.addTaskFrame.frame.pack()
            )
        )

        self.addDashboardButton = Button(
            self.frame,
            text = PrincipalFrameConfig.addDashboardButtonText,
            command = lambda:(
                self._mainwindow.unpackAllFrames(),
                self._mainwindow.addDashboardFrame.frame.pack()
            )
        )

        self.checkButton = Button(
            self.frame,
            text = PrincipalFrameConfig.checkButtonText,
            command = lambda:(
                self._mainwindow.unpackAllFrames()
            )
        )

        self.showButton.pack()
        self.addTaskButton.pack()
        self.checkButton.pack()
        self.addDashboardButton.pack()


class AddDashBoardFrame():
    def __init__(self, MainWindow):
        self._mainwindow = MainWindow
        self.frame = Frame(MainWindow.mainwindow)
        self.addButton = None
        self.dashBoardNameEntry = None
        self.cancelButton = None

        self._configAddDashboardFrame()

    def _configAddDashboardFrame(self):
        newDashboard = StringVar()
        self.dashBoardNameEntry = Entry(
            self.frame,
            textvariable = newDashboard
        )

        self.addButton = Button(
            self.frame,
            text = AddDashboardFrameConfig.addButtonText,
            command = lambda:(
                createDashBoard(self._mainwindow, newDashboard.get())
            )
        )

        self.cancelButton = Button(
            self.frame,
            text = AddDashboardFrameConfig.cancelButtonText,
            command = lambda:(
                self._mainwindow.unpackAllFrames(),
                self._mainwindow.principalFrame.frame.pack()
            )
        )

        self.dashBoardNameEntry.pack()
        self.addButton.pack()
        self.cancelButton.pack()


class AddTaskFrame():
    def __init__(self, MainWindow):
        self._mainwindow = MainWindow
        self.frame = Frame(MainWindow.mainwindow)
        self.dashBoardList = None
        self.newTaskEntry = None
        self.newTaskButton = None
        self.cancelButton = None

        self._configAddTaskFrame()
    
    def _configAddTaskFrame(self):
        newTask_var = StringVar()

        self.dashBoardList = ttk.Combobox(
            self.frame,
            state = "readonly"
        )

        self.newTaskEntry = Entry(
            self.frame,
            textvariable = newTask_var
        )

        self.newTaskButton = Button(
            self.frame,
            text = AddTaskFrameConfig.addButtonText,
            command = lambda: (
                addTasktoDashboard(self._mainwindow, self.dashBoardList.get(), newTask_var.get())
            )
        )

        self.cancelButton = Button(
            self.frame,
            text = AddTaskFrameConfig.cancelButtonText,
            command = lambda:(
                self._mainwindow.unpackAllFrames(),
                self._mainwindow.principalFrame.frame.pack()
            )
        )

        self.dashBoardList.pack()
        self.newTaskEntry.pack()
        self.newTaskButton.pack()
        self.cancelButton.pack()