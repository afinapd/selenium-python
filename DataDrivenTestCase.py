import  XLUtils
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")

driver.get("http://ipstgf.sinarmasmining.com/logout")
# driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
path="D:\\Timesheet SMM\\test.xlsx"

rows=XLUtils.getRowCount(path,"Sheet1")
for r in range(2,rows+1):
    email = XLUtils.readData(path,"Sheet1",r,1)
    # password = XLUtils.readData(path,"Sheet1",r,2)
    # driver.find_element_by_name("userName").send_keys(email)
    # driver.find_element_by_name("password").send_keys(password)
    # driver.find_element_by_name("login").click()
    # print(driver.title)
    driver.find_element_by_xpath("//*[contains(@type,'email')]").send_keys(email)
    driver.find_element_by_xpath("//*[text()='Login']").click()
    print(driver.title)
    time.sleep(3)

    if driver.current_url=="http://ipstgf.sinarmasmining.com/my-approval-list":
        print("sukses")
        XLUtils.writeData(path,"Sheet1",r,3,"test pass")
    else:
        print("gagal")
        XLUtils.writeData(path, "Sheet1", r, 3, "test failed")
    time.sleep(3)

    # driver.find_element_by_link_text("Home").click()

    driver.find_element_by_xpath("//*[@id='app']/div[1]/header/div/button[2]").click()
    driver.find_element_by_xpath("//*[text()='Logout']").click()