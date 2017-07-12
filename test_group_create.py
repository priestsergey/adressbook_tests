from models.group import Group

def test_group_create(app):
    group = Group("test170710", "TEST170710_1", "comment170710_1")
    app.open_main_page()
    app.login("admin", "secret")
    app.open_group_page()
    app.create_group(group)
    # TODO: Verify group page