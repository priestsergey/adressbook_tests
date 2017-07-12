from selenium import webdriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_group_create(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(15)
    
    def test_test_group_create(self):
        wd = self.wd
        self.open_main_page()
        self.login("admin", "secret")
        self.open_group_page()
        self.create_group("test170710", "TEST170710_1", "comment170710_1")
        # TODO: Verify group page

    def create_group(self, group_name, group_header, group_footer):
        # Creat
        wd = self.wd
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group_footer)
        wd.find_element_by_name("submit").click()

    def open_group_page(self):
        # Open group page
        wd = self.wd
        wd.find_element_by_link_text("Групи").click()

    def login(self, username, password):
        # Login
        wd = self.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_main_page(self):
        self.wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
