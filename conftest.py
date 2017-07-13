import pytest
from addressbook_api import AddressBook
from models.group import Group

@pytest.fixture(scope="session")
def app():
    app = AddressBook()
    app.open_main_page()
    yield app
    app.destroy()

@pytest.fixture()
def init_login(app):
    if not app.is_logged():
        app.login(username="admin", password="secret")
    yield
    app.logout()

@pytest.fixture()
def init_group(app):
    if not app.is_groups_present():
        app.open_group_page()
        app.create_group(Group(name="Test"))

groups = [
    Group("test170710", "TEST170710_1", "comment170710_1"),
    Group("test170710", "TEST170710_1")
]
@pytest.fixture(params=groups, ids=[str(g) for g in groups])
def group(request):
    return request.param

