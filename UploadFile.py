from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.automationtesting.in/FileUpload.html")
driver.maximize_window()

driver.find_element_by_id("input-4").send_keys("C://Users/NB01/Pictures/ancol.png")