from selenium import webdriver
from selenium.webdriver import ActionChains

from Locators.Constants import Constants

driver = webdriver.Chrome(executable_path=Constants.driver)
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()

drag=driver.find_element_by_xpath("//*[@id='draggable']")
drop=driver.find_element_by_xpath("//*[@id='droppable']")

actions=ActionChains(driver)

actions.drag_and_drop(drag,drop).perform()