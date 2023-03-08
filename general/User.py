from database import Database

class DatabaseUser(Database.Database):

    collums = {
        "Id": "TEXT PRIMARY KEY",
        "Name": "TEXT",
        "PasswordHash": "TEXT",
    }

    def __init__(self, sqliteFile) -> None:
        super().__init__(sqliteFile, "DatabaseShoppingQuickItems")

class User():

    def __init__(self, database, id=None, name="unnamed", passwordHash=None) -> None:
        """
        Creates a User
        
        :param DatabaseUser database: The corresponding database object
        :param str id: The id of the user
        :param str name: The name of the user
        :param str passwordHash: The password hash of the user
        """
        if id == None:
            id = database.generateId()
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
