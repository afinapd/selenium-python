from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from Locators.Constants import Constants

driver = webdriver.Chrome(executable_path=Constants.driver)
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

driver.implicitly_wait(10)

assert driver.title == "Selenium Practice Form", "thats wrong"

driver.find_element_by_id("RESULT_TextField-1").send_keys("afina")
