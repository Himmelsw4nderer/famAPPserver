from database import Database


class KategoryDatabaseConnection(Database.Connection):

    collums = {
        "Id": "TEXT PRIMARY KEY",
        "Name": "TEXT NOT NULL",
        "OwnerId": "TEXT NOT NULL",
    }

    def __init__(self, sqliteFile) -> None:
        super().__init__(sqliteFile, "DatabaseShoppingKategory")


class Kategory():

    def __init__(self, databaseCOnnection, id=None, name, ownerId, userIds=None) -> None:
        """
        Create a ShoppingKategory
        
        :param ListDatabaseConnection databaseConnection: The corresponding shopping kategory database connection object
        :param str id: The id of the shopping kategory
        :param str name: The name of the shopping kategory
        :param str ownerId: The id of the shopping kategory owner
        :param str[] userIds: A list of users with access to the kategory
        """
        if id == None:
            id = databaseConnection.generateId()
        self.id = id
        self.name = name
        self.ownerId = ownerId
        self.userIds = userIds

    def toDictWithoutConnections(self):
        """
        Convert object to dict without connections

        :return: all Values without connections to other tables
        :rtype: dict
        """
        return {
            "Id": self.id,
            "Name": self.name,
            "OwnerId": self.ownerId,
        }
