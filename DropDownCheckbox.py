from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from Locators.Constants import Constants

driver = webdriver.Chrome(executable_path=Constants.driver)
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()

select = Select(driver.find_element_by_id('RESULT_RadioButton-9'))
select.select_by_visible_text('Morning')
# time.sleep(2)
driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[2]/td/label").click()
# print(select.options)
driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[1]/td/label").click()
driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[3]/td/label").click()
# driver.find_element_by_css_selector("select[id='speed'][visible_text='Medium']")