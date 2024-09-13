# test_crud.py
import unittest
from unittest.mock import MagicMock
from crud import ItemService, Database

class TestItemService(unittest.TestCase):
    def setUp(self):
        self.mock_db = MagicMock(spec=Database)
        self.service = ItemService(self.mock_db)

    def test_create_item(self):
        item = {"name": "Test Item"}
        self.service.create_item(item)
        self.mock_db.create.assert_called_once_with(item)

    def test_get_item(self):
        item_id = 1
        expected_item = {"name": "Test Item"}
        self.mock_db.read.return_value = expected_item
        
        result = self.service.get_item(item_id)
        self.mock_db.read.assert_called_once_with(item_id)
        self.assertEqual(result, expected_item)

    def test_update_item(self):
        item_id = 1
        item = {"name": "Updated Item"}
        self.service.update_item(item_id, item)
        self.mock_db.update.assert_called_once_with(item_id, item)

    def test_delete_item(self):
        item_id = 1
        self.service.delete_item(item_id)
        self.mock_db.delete.assert_called_once_with(item_id)

if __name__ == '__main__':
    unittest.main()
