from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from Locators.Constants import Constants

driver = webdriver.Chrome(executable_path=Constants.driver)
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.find_element_by_id("RESULT_TextField-1").send_keys("testtt")
driver.find_element_by_id("RESULT_TextField-2").send_keys("testtt")
driver.find_element_by_xpath("/html/body/form/div[2]/div[7]/input").send_keys("apassihhh")
driver.find_element_by_xpath("/html/body/form/div[2]/div[15]/table/tbody/tr[1]/td/label").click()
print(driver.title)
# driver.get("https://www.linkedin.com/in/afinapd/")
# print(driver.title)
# driver.back()
# print(driver.title)
# driver.forward()
# print(driver.title)