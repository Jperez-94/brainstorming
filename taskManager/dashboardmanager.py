import json
from tkinter import messagebox
from default import PopupsConfig

class DashBoardManager():
    def __init__(self):
        self._json_filepath = f'{__file__[0:__file__.find("dashboardmanager.py")]}{"dashboards.json"}'
        self.dashboardJson = None
        self._read_json()

    def _read_json(self) -> None:
        with open(self._json_filepath) as file:
            self.dashboardJson = json.load(file)

        file.close()

    def write_json(self) -> None:
        with open(self._json_filepath, 'w') as file:
            json.dump(self.dashboardJson, file, indent= 4)

        file.close()

def createDashBoard(windowConfig, dashBoardName):
    if dashBoardName == '':
        print('Add detecction of only spaces name')
        messagebox.showinfo(
            title = PopupsConfig.warningTitle,
            message = PopupsConfig.emptyDashboardMessage
        )
        return

    dashBoard = DashBoardManager()
    dashBoard.dashboardJson[dashBoardName] = {}
    dashBoard.write_json()

    windowConfig.addDashboardFrame.dashBoardNameEntry.delete(0, 'end')
    windowConfig.unpackAllFrames()
    windowConfig.principalFrame.frame.pack()

def removeDashBoard(windowConfig, dashBoardName):
    if dashBoardName == '':
        print('Add detecction of only spaces name')
        messagebox.showinfo(
            title = PopupsConfig.warningTitle,
            message = PopupsConfig.emptyPickDashboardMessage
        )
        return

    dashBoard = DashBoardManager()
    dashBoard.dashboardJson.pop(dashBoardName)

    dashBoard.write_json()

    windowConfig.unpackAllFrames()
    windowConfig.principalFrame.frame.pack()

def setDashBoardsOnWidget(dashboardWidget):
    dashBoardNames = getAllDashBoards()
    
    if len(dashBoardNames) == 0:
        dashboardWidget.config(
            state = "disabled"
        )
        dashboardWidget.config(
            state = "disabled"
        )
        return
    else:
        dashboardWidget.config(
            state = "readonly"
        )
        dashboardWidget.config(
            state = "normal"
        )
    
    dashboardWidget.config(
        values = dashBoardNames
    )

def getAllDashBoards() -> list():
    dashBoard = DashBoardManager()
    dashBoardNames = list()
    for key in dashBoard.dashboardJson.keys():
        dashBoardNames.append(key)
    
    return dashBoardNames

def getDashBoardTasks(dashBoardName) -> list:
    dashBoard = DashBoardManager()
    tasksList = list()

    for task in dashBoard.dashboardJson[dashBoardName].keys():
        tasksList.append(task)
    
    return tasksList
    

def addTasktoDashboard(windowConfig, dashBoardName, newTask):
    if dashBoardName == '':
        messagebox.showinfo(
            title = PopupsConfig.warningTitle,
            message = PopupsConfig.emptyPickDashboardMessage
        )
        return

    elif newTask == '':
        print('Add detecction of only spaces name')
        messagebox.showinfo(
            title = PopupsConfig.warningTitle,
            message = PopupsConfig.emptyTaskMessage
        )
        return
    
    dashBoard = DashBoardManager()
    taskInDashboard = dashBoard.dashboardJson[dashBoardName].keys()

    newTaskKey = f"Task{len(taskInDashboard)}"
    dashBoard.dashboardJson[dashBoardName][newTaskKey] = newTask
    dashBoard.write_json()

    windowConfig.addTaskFrame.newTaskEntry.delete(0, 'end')
    windowConfig.unpackAllFrames()
    windowConfig.principalFrame.frame.pack()

def removeTaskFromDashboard(windowConfig, frame):
    dashBoardName = frame.dashBoardList.get()
    taskName = frame.taskList.get()

    if dashBoardName == '':
        messagebox.showinfo(
            title = PopupsConfig.warningTitle,
            message = PopupsConfig.emptyPickDashboardMessage
        )
        return

    elif taskName == '':
        print('Add detecction of only spaces name')
        messagebox.showinfo(
            title = PopupsConfig.warningTitle,
            message = PopupsConfig.emptyPickTaskMessage
        )
        return
    
    dashBoard = DashBoardManager()
    dashBoard.dashboardJson[dashBoardName].pop(taskName)

    dashBoard.write_json()

    windowConfig.unpackAllFrames()
    windowConfig.principalFrame.frame.pack()
    