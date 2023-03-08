import sqlite3
import uuid


class Connection():

    collums = {
        "Id": "TEXT",
        "Name": "TEXT"
    }

    def __init__(self, sqliteFile, sqliteTable) -> None:
        """create a Database Object linked to SQLite file"""
        # saving variables in class
        self.sqliteFile = sqliteFile
        self.sqliteTable = sqliteTable
        # connecting to database and create curser
        self.sqliteDatabase = sqlite3.connect(sqliteFile)
        self.sqliteCursor = self.sqliteDatabase.cursor()
        # create Table
        self.createTable()
        pass

    def create(self, data):
        """
        Adding an object to list

        :param Object data: The object to be created
        :return: The object on sucess
        """
        # create execute string
        executeString = f"""INSERT INTO {self.sqliteTable}({', '.join(data.toDictWithoutConnections().keys())}) VALUES(?{(", ?" * (len(data.toDictWithoutConnections().values())-1))})"""
        self.sqliteCursor.execute(
            executeString, tuple(data.toDictWithoutConnections().values()))
        self.sqliteDatabase.commit()

    def remove(self, objectId):
        """
        Removes an object from list
        
        :param str objectId: The id of the object to be removed
        :return: The object on sucess
        """
        # TODO create execute string
        executeString = f""
        self.sqliteDatabase.execute(executeString)

    def change(self, objectId, collumId, value):
        """
        Change an object on the list

        :param str objectId: The id of the object to be changed
        :param str collumId: The id of the collum whos value changes
        :param value: The new value to which it should be changed
        :return: The new objet on success
        """
        # TODO create execute string
        executeString = f""
        self.sqliteDatabase.execute(executeString)

    def load(self, objectId):
        """
        adding an object to list#

        :param str objectId: The id of the object to be loaded
        :param Object object: The object to put the vars in
        :return: The new objet on success
        """
        # TODO create execute string
        executeString = f""
        self.sqliteDatabase.execute(executeString)
        
    def createTable(self):
        """creates the fitting Table if it does not Exist"""
        # create execution String
        executionString = f"CREATE TABLE IF NOT EXISTS {self.sqliteTable}({','.join(' '.join((key,val)) for (key,val) in self.collums.items())})"
        self.sqliteDatabase.execute(executionString)

    def generateId(self):
        """
        Generate a not used id as primary key
        
        :return: The free id
        :rtype: str
        """
        # random generated uuid
        newUUID = str(uuid.uuid4())
        # check if uuid exists in Tabel
        self.sqliteCursor.execute(
            f"SELECT Id FROM {self.sqliteTable} WHERE Id = '{newUUID}'")
        data = self.sqliteCursor.fetchall()
        if len(data) == 0:
            # return newUUID
            return newUUID
        # recursivly testing new uuid
        return self.generateId()

class Object():

    def __init__(self, databaseConnection, ...):
        """
        Creates a Object

        :param Connection database: The corresponding database connection
        """
        pass

    def __init__(self, databaseConnection, id):
        """
        Loads an Object by id from Database

        :param Connection database: The corresponding database connection object
        :param str id: The id to load the object by
        """
        self = databaseConnection.load(self, id)

     def toDictWithoutConnections(self):
        """
        Convert object to dict without connections

        :return: all Values without connections to other Lists
        :rtype: dict
        """
        pass