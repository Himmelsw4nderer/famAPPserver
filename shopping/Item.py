from database import database


class DatabaseItem(database.Database):

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
        """creates a Shopping item out of inputs"""
        if id == None:
            id = database.generateId()
        self.id = id
        self.name = name
        self.amount = amount
        self.unit = unit
        self.kategoryIds = kategoryIds
        self.checked = checked
        self.listId = listId

    def toDict(self):
        """returns dict of all Values"""
        return {
            "Id": self.id,
            "Name": self.name,
            "Amount": self.amount,
            "Unit": self.unit,
            "KategoryIds": self.kategoryIds,
            "Checked": self.checked,
            "ListId": self.listId
        }
