from database import Database

class UserDatabaseConnection(Database.Connection):

    collums = {
        "Id": "TEXT PRIMARY KEY",
        "Name": "TEXT",
        "PasswordHash": "TEXT",
    }

    def __init__(self, sqliteFile) -> None:
        super().__init__(sqliteFile, "DatabaseShoppingQuickItems")

class User():

    def __init__(self, databaseConnection, id=None, name, passwordHash) -> None:
        """
        Creates a User
        
        :param UserDatabaseConnection databaseConnection: The corresponding user database connection object
        :param str id: The id of the user
        :param str name: The name of the user
        :param str passwordHash: The password hash of the user
        """
        if id == None:
            id = databaseConnection.generateId()
        self.id = id
        self.name = name
        self.passwordHash = passwordHash

    def toDictWithoutConnections(self):
        """
        Convert object to dict without connections

        :return: all Values without connections to other tables
        :rtype: dict
        """
        return {
            "Id": self.id,
            "Name": self.name,
            "PasswordHash": self.passwordHash,
        }
