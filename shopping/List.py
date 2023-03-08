from database import database


class DatabaseList(database.Database):

    collums = {
        "Id": "TEXT PRIMARY KEY",
        "Name": "TEXT NOT NULL",
        "OwnerId": "INTEGER NOT NULL",
    }

    def __init__(self, sqliteFile) -> None:
        super().__init__(sqliteFile, "ShoppingLists")


class List():

    def __init__(self, database, id=None, name="unnamed", ownerId=-1, userIds=None) -> None:
        """creates a shopping list out of given data"""
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
