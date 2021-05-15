from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\ProgramData\chromedriver_win32\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()
driver.find_element_by_id("txtUsername").send_keys("admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

admin=driver.find_element_by_id("menu_admin_viewAdminModule")
userManagement=driver.find_element_by_id("menu_admin_UserManagement")
user= driver.find_element_by_id("menu_admin_viewSystemUsers")
actions=ActionChains(driver)

actions.move_to_element(admin).move_to_element(userManagement).move_to_element(user).click().perform()