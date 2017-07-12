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

class test56(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test56(self):
        success = True
        wd = self.wd
        wd.get("http://f-clust-crm.mts.com.ua/telcrm/gui/MainPage.aspx")
        wd.find_element_by_link_text("Абонент").click()
        wd.find_element_by_id("smiCustomerSearch").click()
        wd.find_element_by_id("fiCustomerSearch").click()
        wd.find_element_by_id("smiCustomer_create").click()
        wd.find_element_by_xpath("//li[@id='TerminalDevice']//a[.='Приложение обслуживания']").click()
        wd.find_element_by_link_text("Корпоративный бюджет").click()
        wd.find_element_by_link_text("Единый счет").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
