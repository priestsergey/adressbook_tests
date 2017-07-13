from selenium import webdriver

class AddressBook:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(15)
    def message(self):
        return self.wd.find_element_by_css_selector(".msgbox").text

    def return_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()



    def create_group(self, group):
        # Creat
        wd = self.wd
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
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

    def destroy(self):
        self.wd.quit()