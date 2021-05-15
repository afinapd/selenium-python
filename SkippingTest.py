import unittest

class AppTesting(unittest.TestCase):
    @unittest.SkipTest #decorator
    def testSearch(self):
        print("this is search test")
    @unittest.skip("im skipping this method")
    def testAdvancedSearch(self):
        print("this is advanced search test")
    @unittest.skipIf(1==1,"number are not equals")
    def testPrepaidRecharge(self):
        print("this is prepaid recharge test")
    def testPostpaidRecharge(self):
        print("this is postpaid recharge test")
    def testLoginByGmail(self):
        print("login by gmail")
    def testLoginByTwitter(self):
        print("login by twitter")

if __name__=="__main__" :
    unittest.main()