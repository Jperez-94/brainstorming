from dashboardmanager import *
import webbrowser

class Html_Parser():
    def __init__(self) -> None:
        self.filepath = f'{__file__[0:__file__.find("parser_html.py")]}temp/temporal.html'
        self.template = None
        self.getTemplate()

    def formatBody(self, dashBoardJson):
        htmlDashBoard = ""
        if len(dashBoardJson.keys()) == 0:
            htmlDashBoard += "<h1>NO HAY DASHBOARDS DISPONIBLES</h1>\n"
        else:
            for dashBoard in dashBoardJson.keys():
                htmlDashBoard += "<h2>{}</h2>\n".format(dashBoard)
                htmlDashBoard += "<ul>\n"
                if len(dashBoardJson[dashBoard].keys()) == 0:
                    htmlDashBoard += "<li><h3>NO HAY TASKS DISPONIBLES</h3></li>\n"
                else:
                    for task in dashBoardJson[dashBoard].keys():
                        htmlDashBoard += "<li>{}</li>\n".format(dashBoardJson[dashBoard][task])

                htmlDashBoard += "</ul>\n"

        self.template = self.template.format(htmlDashBoard)

    def getTemplate(self):
        template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboards</title>
</head>
<body>
    {}
</body>
</html>
"""

        self.template = template

def showHtlmDashBoard():
    html_parser = Html_Parser()
    dashboard = DashBoardManager()

    html_parser.formatBody(dashboard.dashboardJson)

    with open(html_parser.filepath, 'w') as file:
            file.write(html_parser.template)

    file.close()

    webbrowser.open_new(html_parser.filepath)


