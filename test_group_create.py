from addressbook_api import AddressBook
from models.group import Group
import unittest

class test_group_create(unittest.TestCase):
    def setUp(self):
        self.app = AddressBook()
    
    def test_test_group_create(self):
        group = Group("test170710", "TEST170710_1", "comment170710_1")
        self.app.open_main_page()
        self.app.login("admin", "secret")
        self.app.open_group_page()
        self.app.create_group(group)
        # TODO: Verify group page

    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
