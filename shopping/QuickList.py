from database import Database


class QuickListDatabaseConnection(Database.Connection):

    collums = {
        "Id": "TEXT PRIMARY KEY",
        "Name": "TEXT NOT NULL",
        "OwnerId": "TEXT NOT NULL",
    }

    def __init__(self, sqliteFile) -> None:
        super().__init__(sqliteFile, "ShoppingQuickLists")


class QuickList():

    def __init__(self, databaseConnection, id=None, name, ownerId, userIds=None) -> None:
        """
        Create a QuickList

        :param ListDatabaseConnection databaseConnection: The corresponding shopping quick list database connection object
        :param str id: The id of the shopping quick list
        :param str name: The name of the shopping quick list
        :param str ownerId: The id of the shopping quick lists owner
        :param str[] userIds: A list of users with access to the quick list
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
