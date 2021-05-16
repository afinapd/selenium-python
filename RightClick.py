from selenium import webdriver
from selenium.webdriver import ActionChains

from Locators.Constants import Constants

driver = webdriver.Chrome(executable_path=Constants.driver)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

rc=driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
actions=ActionChains(driver)
#mouse right click action
actions.context_click(rc).perform()