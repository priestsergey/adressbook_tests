from models.group import Group

def test_group_create(app, init_login):
    group = Group("test170710", "TEST170710_1", "comment170710_1")
    app.open_group_page()
    app.create_group(group)
    # TODO: Verify group page
    assert "A new group has been entered into the address book" in app.message()
    app.return_group_page()

