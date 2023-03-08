import sqlite3
import uuid


class Database():

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
        adding an object to list
        returns object on sucess
        """
        # create execute string
        executeString = f"""INSERT INTO {self.sqliteTable}({', '.join(data.toDict().keys())}) VALUES(?{(", ?" * (len(data.toDict().values())-1))})"""
        self.sqliteCursor.execute(
            executeString, tuple(data.toDict().values()))
        self.sqliteDatabase.commit()

    def remove(self, objectId):
        """
        adding an object to list
        returns object on sucess
        """
        # TODO create execute string
        executeString = f""
        self.sqliteDatabase.execute(executeString)

    def change(self, objectId, collumId, value):
        """
        adding an object to list
        returns new value on success
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
        """generate a not used id as primary key"""
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
