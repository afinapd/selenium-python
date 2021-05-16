from selenium import webdriver;
import time
from  selenium.webdriver.common.keys import Keys

from Locators.Constants import Constants

driver=webdriver.Chrome(executable_path=Constants.driver)

driver.get("https://ipermit.beraucoal.co.id/")
print(driver.title)
username = driver.find_element_by_xpath("//input[@type='email']")
password= driver.find_element_by_xpath("//input[@type='password']")

print(username.is_displayed())
print(password.is_displayed())

username.send_keys("admin.itproject@beraucoal.co.id")
driver.find_element_by_class_name("v-btn__content").click()

# print(driver.current_url)

# driver.get("https://soundcloud.com/gitasav")
# print(driver.title)
# # time.sleep(2)
#
# driver.back()
# print(driver.title)
# # time.sleep(2)
#
# driver.forward()
# print(driver.title)
# time.sleep(2)
# # print(driver.page_source)
# driver.close()