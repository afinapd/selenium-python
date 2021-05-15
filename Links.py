from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

links=driver.find_elements(By.TAG_NAME,"a")
print("total link yang ada di web : ", len(links))

for link in links :
    print(link.text)

# click link
# driver.find_element(By.LINK_TEXT,"REGISTER").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()