from selenium import webdriver

from Locators.Constants import Constants

driver = webdriver.Chrome(executable_path=Constants.driver)

driver.get("https://www.amazon.in/")

# test = driver.get_screenshot_as_png()
# test.save("D:\Timesheet SMM\test.png")

driver.save_screenshot("D:\\Timesheet SMM\\test.png")
# driver.get_screenshot_as_file("D:\\Timesheet SMM\\test2.png")