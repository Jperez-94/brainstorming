
from numpy import empty


class WindowConfig():
    mainWindowTitle = "Pantalla principal"
    mainWindowGeometry = "200x200"
    mainWindowBgColor = "#C5C5C5"

class PopupsConfig():
    warningTitle = "Aviso"

    emptyDashboardMessage = "Nombre de nuevo DashBoard incorrecto\nDebe tener un mínimo de 1 caracter"
    emptyTaskMessage = "Nueva task vacía.\nDescribe la tarea que quieres dejar anotada"
    emptyPickDashboardMessage = """Selecciona en el desplegable la Dashboard a la que quieres añadir la tarea.
    Si no hay dashboards disponibles, por favor añade una antes de querer añadir tareas"""

class PrincipalFrameConfig():
    showButtonText = "Show Dashboard"
    addTaskButtonText = "Add task"
    addDashboardButtonText = "Add DashBoard"
    checkButtonText = "Check task"

class AddTaskFrameConfig():
    addButtonText = "Añadir"
    cancelButtonText = "Cancel"

class AddDashboardFrameConfig():
    addButtonText = "Añadir"
    cancelButtonText = "Cancel"
