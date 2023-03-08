from database import Database


class DatabaseItem(Database.Database):

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


class Item():

    def __init__(self, database, id=None, name="unnamed", amount=1, unit="stk.", kategoryIds=None, checked=False, listId=None) -> None:
        """
        Create a ShoppingItem
        
        :param DatabaseItem database: The corresponding database object
        :param str id: The id of the shopping item
        :param str name: The name of the shopping item
        :param int amount: The amount of the shopping item
        :param str unit: The unit of the shopping item
        :param str[] kategorysIds: The kategorys the shopping items has
        :param bool checked: If the item is checked
        :param str listId: The id of the corresponding list
        """
        if id == None:
            id = database.generateId()
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

        :return: all Values without connections to other tables
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
