import unittest

def setUpModule():
    print("set up module")

def tearDownModule():
    print("tear down module")

class AppTesting (unittest.TestCase):
    @classmethod #before
    def setUp(self):
        print("this is Set Up")
    @classmethod #after
    def tearDown(self):
        print("this is Tear Down")
    @classmethod  # execute before all test
    def setUpClass(cls):
        print("this is Set Up Class")
    @classmethod  # execute after all test
    def tearDownClass(cls):
        print("this is Tear Down Class")

    def testSearch(self):
        print("this is search test")
    def testAdvancedSearch(self):
        print("this is advanced search test")
    def testPrepaidRecharge(self):
        print("this is prepaid recharge test")
    def testPostpaidRecharge(self):
        print("this is postpaid recharge test")


if __name__=="__main__" :
    unittest.main()