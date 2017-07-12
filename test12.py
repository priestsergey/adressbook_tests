# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test12(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test12(self):
        success = True
        wd = self.wd
        wd.get("http://software-testing.ru/edu/3-online/234-functional-test-automation")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
