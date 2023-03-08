from database import Database


class ItemDatabaseConnection(Database.Connection):

    collums = {
        "Id": "TEXT PRIMARY KEY  ",
        "Name": "TEXT NOT NULL",
        "Amount": "INTEGER",
        "Unit": "TEXT",
        "Checked": "INTEGER",
        "ListId": "TEXT NOT NULL",
    }

    def __init__(self, sqliteFile) -> None:
        super().__init__(sqliteFile, "ShoppingItems")


class Item(Database.Object):

    def __init__(self, databaseConnection, id=None, name, amount, unit, kategoryIds=None, checked=False, listId=None) -> None:
        """
        Create a ShoppingItem
        
        :param ItemDatabaseConnection databaseConnection: The corresponding item database connection object
        :param str name: The name of the shopping item
        :param int amount: The amount of the shopping item
        :param str unit: The unit of the shopping item
        :param str[] kategorysIds: The kategorys the shopping items has
        :param bool checked: If the item is checked
        :param str listId: The id of the corresponding list
        """
        if id == None:
            id = databaseConnection.generateId()
        self.id = id
        self.name = name
        self.amount = amount
        self.unit = unit
        self.kategoryIds = kategoryIds
        self.checked = checked
        self.listId = listId

    def toDictWithoutConnections(self):
        """
        Convert object to dict without connections

        :return: all Values without connections to other Lists
        :rtype: dict
        """
        return {
            "Id": self.id,
            "Name": self.name,
            "Amount": self.amount,
            "Unit": self.unit,
            "Checked": self.checked,
            "ListId": self.listId
        }
