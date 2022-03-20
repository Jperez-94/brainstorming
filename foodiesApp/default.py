
class ErrorMessage():
    strTypeError = "Parameter is not string type. Type received: {}"
    dataBaseKeyNotFound = "Requested key not found in Database. Request: {}"
    frameNotConfigured = "Not able to parse the data frame. Need to get data from DataBase"
    frameWrongFormat = "Wrong data frame format. Frame must contain keys: name, direction, foodtype"
    emptyDataBase = "Database is empty. Add items to it before asking for a random place"
    newEntryRepeat = "New entry already exists in database. New entry: {}"
    dataFrameTypeError = "Unexpected new entry type. Expected type DataFrame. Current type: {}"
    indexEntryNotFound = "Requested index not found. Request: {}"

class DataBaseKey():
    name = "name"
    direction = "direction"
    foodtype = "foodtype"