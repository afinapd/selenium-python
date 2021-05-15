from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
print(driver.current_window_handle) #CDwindow-91ACEC4E424AE77C2A39E56792C08792 -parent

handles = driver.window_handles #return all the handle values of opened browser windows

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows" :
        driver.close() #close parent

# driver.quit()