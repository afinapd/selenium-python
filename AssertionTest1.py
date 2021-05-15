import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path=r"C:\Users\afinapd\PycharmProjects\HelloWorld\chromedriver\chromedriver.exe")
        driver.get("https://www.google.com/")
        titleWeb=driver.title

        # assertEqual
        # self.assertEqual("Google", titleWeb, "webpage title is not the same ")
        self.assertNotEqual("Google", titleWeb, "this equal")

if __name__=="__main__" :
    unittest.main()