import unittest
from selenium import webdriver

class SearchEngineTest(unittest.TestCase) :
    def testGoogle(self):
        self.driver=webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("title the package is :",self.driver.title)
        self.driver.close()

    def testBing(self):
        self.driver=webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        print("title the package is :",self.driver.title)
        self.driver.close()

if __name__=="__main__" :
    unittest.main()