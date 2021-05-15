from selenium import webdriver
import time
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
inputBoxes = driver.find_elements_by_class_name("text_field")
# print(len(inputBoxes))
for link in inputBoxes:
    print(link.get_attribute('text')) #text, href, xpath,id, value