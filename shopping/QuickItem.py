from database import Database


class DatabaseQuickItem(Database.Database):

    collums = {
        "Id": "TEXT PRIMARY KEY",
        "Name": "TEXT",
        "Amount": "INTEGER",
        "Unit": "TEXT",
        "QuickListId": "TEXT"
    }

    def __init__(self, sqliteFile) -> None:
        super().__init__(sqliteFile, "DatabaseShoppingQuickItems")


class QuickItem():

    def __init__(self, database, id=None, name="unnamed", amount=1, unit="stk.", kategoryIds=None, quickListId=None) -> None:
        """
        Create a ShoppingQuickItem
        
        :param DatabaseQuickItem database: The corresponding database object
        :param str id: The id of the shopping quick item
        :param str name: The name of the shopping quick item
        :param int amount: The amount of the shopping quick item
        :param str unit: The unit of the shopping quick item
        :param str[] kategorysIds: The kategorys the shopping quick items has
        :param str quickListId: The id of the corresponding quick list
        """
        if id == None:
            id = database.generateId()
        self.id = id
        self.name = name
        self.amount = amount
        self.unit = unit
        self.kategoryIds = kategoryIds
        self.quickListId = quickListId

    def toDictWithoutConnections(self):
        """
        Convert object to dict without connections

        :return: all Values without connections to other tables
        :rtype: dict
        """
        return {
            "Id": self.id,
            "Name": self.name,
            "Amount": self.amount,
            "Unit": self.unit,
            "QuickListId": self.quickListId
        }
