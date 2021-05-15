from selenium import webdriver
import time
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# driver.find_element_by_id("RESULT_TextField-1").send_keys("afina")
# time.sleep(2)
wait = WebDriverWait(driver,10)
element=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='q26']/table/tbody/tr[2]/td/label")))
element.click()