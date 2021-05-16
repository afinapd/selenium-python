from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from Locators.Constants import Constants

driver = webdriver.Chrome(executable_path=Constants.driver)
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

test = driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[1]/td/label")
print(test.is_enabled())
print(test.is_displayed())
print(test.is_selected())
test.click()
time.sleep(2)
print(test.is_enabled())
print(test.is_displayed())
print(test.is_selected())
