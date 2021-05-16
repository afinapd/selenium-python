from selenium import webdriver
from selenium.webdriver import ActionChains

from Locators.Constants import Constants

driver = webdriver.Chrome(executable_path=Constants.driver)

driver.get("http://testautomationpractice.blogspot.com/")

driver.maximize_window()
dc=driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
actions=ActionChains(driver)
actions.double_click(dc).perform()