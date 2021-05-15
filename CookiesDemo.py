from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in/")

#capture all cookies
cookies = driver.get_cookies()
print(len(cookies)) #number cookies
print(cookies) #print all cookies

#adding new cookie to the browser
cookie={'name':'my cookie','value':'123'}
driver.add_cookie(cookie)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

#deleting cookie
driver.delete_cookie('my cookie')
cookies = driver.get_cookies()
time.sleep(1)
print(len(cookies))

#deleting cookie
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))

