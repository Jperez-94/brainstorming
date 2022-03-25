import json

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
        print('Add behaviour to an empty name or only space name')
        return

    dashBoard = DashBoardManager()
    dashBoard.dashboardJson[dashBoardName] = {}
    dashBoard.write_json()

    windowConfig.addDashboardFrame.dashBoardNameEntry.delete(0, 'end')
    windowConfig.unpackAllFrames()
    windowConfig.principalFrame.frame.pack()
    print('Add new dashboard')
