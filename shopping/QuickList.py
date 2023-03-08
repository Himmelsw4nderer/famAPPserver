from database import database


class DatabaseQuickList(database.Database):

    collums = {
        "Id": "TEXT PRIMARY KEY",
        "Name": "TEXT NOT NULL",
        "OwnerId": "INTEGER NOT NULL",
    }

    def __init__(self, sqliteFile) -> None:
        super().__init__(sqliteFile, "ShoppingQuickLists")


class QuickList():

    def __init__(self, database, id=None, name="unnamed", ownerId=-1, userIds=None) -> None:
        """create a quick list object of given values"""
        if id == None:
            id = database.generateId()
        self.id = id
        self.name = name
        self.ownerId = ownerId
        self.userIds = userIds

    def toDict(self):
        """returns dict of all Values"""
        return {
            "Id": self.id,
            "Name": self.name,
            "OwnerId": self.ownerId,
            "UserIds": self.userIds
        }
