from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

from Locators.Constants import Constants

driver = webdriver.Chrome(executable_path=Constants.driver)

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")

driver.switch_to_frame("packageListFrame") #first frame
driver.find_element_by_link_text("org.openqa.selenium.chrome").click()
time.sleep(3)

driver.switch_to_default_content()

driver.switch_to_frame("packageFrame") #second frame
driver.find_element_by_link_text("ChromeDriver").click()
time.sleep(3)

driver.switch_to_default_content()

driver.switch_to_frame("classFrame") #third frame
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]").click()
time.sleep(3)