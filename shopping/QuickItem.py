from database import database


class DatabaseQuickItem(database.Database):

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
        """creates a Quick item out of inputs"""
        if id == None:
            id = database.generateId()
        self.id = id
        self.name = name
        self.amount = amount
        self.unit = unit
        self.kategoryIds = kategoryIds
        self.quickListId = quickListId

    def toDict(self):
        """returns dict of all Values"""
        return {
            "Id": self.id,
            "Name": self.name,
            "Amount": self.amount,
            "Unit": self.unit,
            "KategoryIds": self.kategoryIds,
            "QuickListId": self.quickListId)
        }
