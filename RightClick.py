from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

rc=driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
actions=ActionChains(driver)
#mouse right click action
actions.context_click(rc).perform()