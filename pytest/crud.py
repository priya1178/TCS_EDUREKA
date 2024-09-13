# crud.py
class Database:
    def create(self, item):
        pass

    def read(self, item_id):
        pass

    def update(self, item_id, item):
        pass

    def delete(self, item_id):
        pass

class ItemService:
    def __init__(self, db):
        self.db = db

    def create_item(self, item):
        self.db.create(item)

    def get_item(self, item_id):
        return self.db.read(item_id)

    def update_item(self, item_id, item):
        self.db.update(item_id, item)

    def delete_item(self, item_id):
        self.db.delete(item_id)
