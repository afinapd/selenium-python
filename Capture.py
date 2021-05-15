from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in/")

# test = driver.get_screenshot_as_png()
# test.save("D:\Timesheet SMM\test.png")

driver.save_screenshot("D:\\Timesheet SMM\\test.png")
# driver.get_screenshot_as_file("D:\\Timesheet SMM\\test2.png")