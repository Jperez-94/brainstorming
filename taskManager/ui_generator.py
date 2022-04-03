from tkinter import *
from tkinter import ttk
from default import WindowConfig, PrincipalFrameConfig, AddTaskFrameConfig, AddDashboardFrameConfig,RemoveTaskFrameConfig, RemoveDashBoardFrameConfig
from dashboardmanager import *
from parser_html import showHtlmDashBoard


class Main_Window():
    def __init__(self):
        self.mainwindow = Tk()
        self.principalFrame = PrincipalFrame(self)
        self.addTaskFrame = AddTaskFrame(self)
        self.removeTaskFrame = RemoveTaskFrame(self)
        self.addDashboardFrame = AddDashBoardFrame(self)
        self.removeDashboardFrame = RemoveDashBoardFrame(self)
        self.mainwindow.title(WindowConfig.mainWindowTitle)
        self.mainwindow.geometry(WindowConfig.mainWindowGeometry)
        self.mainwindow.config(
            bg = WindowConfig.mainWindowBgColor
        )

        self.principalFrame.frame.pack()
    
    def unpackAllFrames(self):
        self.principalFrame.frame.pack_forget()
        self.addTaskFrame.frame.pack_forget()
        self.removeTaskFrame.frame.pack_forget()
        self.addDashboardFrame.frame.pack_forget()
        self.removeDashboardFrame.frame.pack_forget()


class PrincipalFrame():
    def __init__(self, MainWindow):
        self._mainwindow = MainWindow
        self.frame = Frame(MainWindow.mainwindow)
        self.showButton = None
        self.addTaskButton = None
        self.addDashboardButton = None
        self.removeDashboardButton = None

        self._configPrincipalFrame()

    def _configPrincipalFrame(self):
        self.showButton = Button(
            self.frame,
            text = PrincipalFrameConfig.showButtonText,
            command = lambda:(
                showHtlmDashBoard()
            )
        )

        self.addTaskButton = Button(
            self.frame,
            text = PrincipalFrameConfig.addTaskButtonText,
            command = lambda:(
                self._mainwindow.unpackAllFrames(),
                setDashBoardsOnWidget(self._mainwindow.addTaskFrame.dashBoardList),
                self._mainwindow.addTaskFrame.frame.pack()
            )
        )

        self.addDashboardButton = Button(
            self.frame,
            text = PrincipalFrameConfig.addDashboardButtonText,
            command = lambda:(
                self._mainwindow.unpackAllFrames(),
                setAvailableConfigOnWidget(self._mainwindow.addDashboardFrame.dashBoardConfigList),
                self._mainwindow.addDashboardFrame.frame.pack()
            )
        )

        self.removeDashboardButton = Button(
            self.frame,
            text = PrincipalFrameConfig.removeDashboardButtonText,
            command = lambda: (
                self._mainwindow.unpackAllFrames(),
                setDashBoardsOnWidget(self._mainwindow.removeDashboardFrame.dashBoardList),
                self._mainwindow.removeDashboardFrame.frame.pack()
            )
        )

        self.removeTaskButton = Button(
            self.frame,
            text = PrincipalFrameConfig.removeTaskButtonText,
            command = lambda:(
                self._mainwindow.unpackAllFrames(),
                setDashBoardsOnWidget(self._mainwindow.removeTaskFrame.dashBoardList),
                self._mainwindow.removeTaskFrame.frame.pack()
            )
        )

        self.showButton.pack()
        self.addTaskButton.pack()
        self.removeTaskButton.pack()
        self.addDashboardButton.pack()
        self.removeDashboardButton.pack()


class AddDashBoardFrame():
    def __init__(self, MainWindow):
        self._mainwindow = MainWindow
        self.frame = Frame(MainWindow.mainwindow)
        self.addButton = None
        self.dashBoardNameEntry = None
        self.dashBoardConfigList = None
        self.cancelButton = None

        self._configAddDashboardFrame()

    def _configAddDashboardFrame(self):
        newDashboard = StringVar()
        self.dashBoardNameEntry = Entry(
            self.frame,
            textvariable = newDashboard
        )

        self.dashBoardConfigList = ttk.Combobox(
            self.frame,
            state = "readonly"
        )

        self.addButton = Button(
            self.frame,
            text = AddDashboardFrameConfig.addButtonText,
            command = lambda:(
                createDashBoard(self._mainwindow, newDashboard.get(), self.dashBoardConfigList.get())
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
        self.dashBoardConfigList.pack()
        self.addButton.pack()
        self.cancelButton.pack()

class RemoveDashBoardFrame():
    def __init__(self, MainWindow):
        self._mainwindow = MainWindow
        self.frame = Frame(MainWindow.mainwindow)
        self.dashBoardList = None
        self.removeDashboardButton = None
        self.cancelButton = None

        self._configRemoveDashBoardFrame()
    
    def _configRemoveDashBoardFrame(self):
        self.dashBoardList = ttk.Combobox(
            self.frame,
            state = "readonly"
        )

        self.removeDashboardButton = Button(
            self.frame,
            text = RemoveDashBoardFrameConfig.removeButtonText,
            command= lambda: (
                removeDashBoard(self._mainwindow, self.dashBoardList.get())
            )
        )

        self.cancelButton = Button(
            self.frame,
            text = RemoveDashBoardFrameConfig.cancelButtonText,
            command = lambda:(
                self._mainwindow.unpackAllFrames(),
                self._mainwindow.principalFrame.frame.pack()
            )
        )

        self.dashBoardList.pack()
        self.removeDashboardButton.pack()
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

class RemoveTaskFrame():
    def __init__(self, MainWindow):
        self._mainwindow = MainWindow
        self.frame = Frame(MainWindow.mainwindow)
        self.dashBoardList = None
        self.taskList = None
        self.removeButton = None
        self.cancelButton = None

        self._configRemoveTaskFrame()
    
    def _configRemoveTaskFrame(self):
        self.dashBoardList = ttk.Combobox(
            self.frame,
            state = "readonly"
        )

        self.taskList = ttk.Combobox(
            self.frame,
            state = "readonly"
        )

        self.removeButton = Button(
            self.frame,
            text = RemoveTaskFrameConfig.removeButtonText,
            command = lambda: (
                removeTaskFromDashboard(self._mainwindow, self._mainwindow.removeTaskFrame)
            )
        )

        self.cancelButton = Button(
            self.frame,
            text = RemoveTaskFrameConfig.cancelButtonText,
            command = lambda:(
                self._mainwindow.unpackAllFrames(),
                self._mainwindow.principalFrame.frame.pack()
            )
        )

        self.dashBoardList.bind(
            "<<ComboboxSelected>>",
            self._updateTaskList
        )

        self.dashBoardList.pack()
        self.taskList.pack()
        self.removeButton.pack()
        self.cancelButton.pack()

    def _updateTaskList(self, event):
        tasksList = getDashBoardTasks(self.dashBoardList.get())
        self.taskList.config(
            values = tasksList
        )