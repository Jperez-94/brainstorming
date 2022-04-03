
from numpy import empty


class WindowConfig():
    mainWindowTitle = "Pantalla principal"
    mainWindowGeometry = "200x200"
    mainWindowBgColor = "#C5C5C5"

class ReserveWord():
    configKey = "config"
    taskListKey = "taskList"

class PopupsConfig():
    warningTitle = "Aviso"

    emptyDashboardMessage = "Nombre de nuevo DashBoard incorrecto\nDebe tener un mínimo de 1 caracter"
    emptyTaskMessage = "Nueva task vacía.\nDescribe la tarea que quieres dejar anotada"
    emptyPickDashboardMessage = "Selecciona un Dashboard del desplegable"
    emptyPickTaskMessage = "Selecciona una tarea del desplegable"

class PrincipalFrameConfig():
    showButtonText = "Show Dashboard"
    addTaskButtonText = "Add task"
    addDashboardButtonText = "Add DashBoard"
    removeDashboardButtonText = "Remove DashBoard"
    removeTaskButtonText = "Borrar task"

class AddTaskFrameConfig():
    addButtonText = "Añadir"
    cancelButtonText = "Cancel"

class AddDashboardFrameConfig():
    addButtonText = "Añadir"
    cancelButtonText = "Cancel"

class RemoveDashBoardFrameConfig():
    removeButtonText = "Borrar"
    cancelButtonText = "Cancel"

class RemoveTaskFrameConfig():
    removeButtonText = "Borrar"
    cancelButtonText = "Cancel"