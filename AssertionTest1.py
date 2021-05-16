import unittest
from selenium import webdriver

from Locators.Constants import Constants


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path=Constants.driver)
        driver.get("https://www.google.com/")
        titleWeb=driver.title

        # assertEqual
        # self.assertEqual("Google", titleWeb, "webpage title is not the same ")
        self.assertNotEqual("Google", titleWeb, "this equal")

if __name__=="__main__" :
    unittest.main()