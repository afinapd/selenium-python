from selenium import  webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\afinapd\PycharmProjects\HelloWorld\chromedriver\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(3)
# driver.switch_to_alert().accept() #closes alert using ok button
driver.switch_to_alert().dismiss() #closes alert using cancel button