from selenium import webdriver
from selenium.webdriver import ActionChains

from Locators.Constants import Constants

driver = webdriver.Chrome(executable_path=Constants.driver)
driver.get("http://demo.automationtesting.in/FileUpload.html")
driver.maximize_window()

driver.find_element_by_id("input-4").send_keys("C://Users/NB01/Pictures/ancol.png")