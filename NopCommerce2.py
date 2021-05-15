import os
import unittest
import time
import HtmlTestRunner
from selenium import webdriver

#
import sys
sys.path.append("C:/Users/NB01/PycharmProjects/HelloWorld")
from LoginPage import LoginPage


class TestLogin(unittest.TestCase):
    baseURL = "https://admin-demo.nopcommerce.com/"
    email = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")

    @classmethod
    def setup_method(self, method):
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

    @classmethod
    def tearDown_method(self, method):
        self.driver.quit()

    def test_login(self):
        self.driver.get(self.baseURL)
        lp=LoginPage(self.driver)
        lp.setEmail(self.email)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)

    def test_login2(self):
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.setEmail(self.email)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\NB01\\PycharmProjects\\HelloWorld\\Reports"))

