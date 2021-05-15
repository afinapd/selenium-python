from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()

drag=driver.find_element_by_xpath("//*[@id='draggable']")
drop=driver.find_element_by_xpath("//*[@id='droppable']")

actions=ActionChains(driver)

actions.drag_and_drop(drag,drop).perform()