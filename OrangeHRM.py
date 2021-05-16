import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By

from Locators.Constants import Constants


class TestLogin(unittest.TestCase):
    def setup_method(self, method):
        self.driver = webdriver.Chrome(executable_path=Constants.driver)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()
        print("testing close")

    def test_login(self):
        self.driver = webdriver.Chrome(executable_path=Constants.driver)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title is not matching")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\NB01\\PycharmProjects\\HelloWorld\\Reports"))



