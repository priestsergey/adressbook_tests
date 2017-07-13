def test_delete_group(app, init_login):
    app.open_group_page()
    app.delete_first_group()
    assert "Group has been removed." in app.message()
    app.return_group_page()
    # TODO: Verify group deleted

