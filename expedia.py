from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import  time

from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.get("https://www.expedia.com/")

driver.implicitly_wait(5)

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Cars")))
element.click()
# driver.find_element_by_link_text("Cars")
driver.find_element_by_class_name("uitk-faux-input").click()
driver.find_element_by_xpath("//*[@id='app']/div[1]/div[2]/div[2]/div/header/section/div/input").send_keys("Jakarta")

# driver.find_element_by_id("tab-car-tab-hp").click()
# driver.find_element_by_id("car-pickup-hp-car").send_keys("Jakarta")
# driver.find_element_by_id("car-dropoff-hp-car").send_keys("Bandung")
# driver.find_element_by_id("car-pickup-date-hp-car").send_keys("12/06/2020")
# driver.find_element_by_id("car-pickup-time-hp-car").send_keys("20:00")
# driver.find_element_by_id("car-dropoff-date-hp-car").send_keys("13/06/2020")
# driver.find_element_by_id("car-dropoff-time-hp-car").send_keys("10:00")
# driver.find_element_by_id("car-age-of-driver-hp-car").send_keys("29")
# driver.find_element_by_id("gcw-submit-car").click()

