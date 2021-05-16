from selenium import webdriver

from Locators.Constants import Constants

driver = webdriver.Chrome(executable_path=Constants.driver)

driver.get("http://testautomationpractice.blogspot.com/")

row = len(driver.find_elements_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr"))  # count number rows
column = len(driver.find_elements_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th"))  # count number column

print(row)
print(column)

print("Bookname"+"       "+"author"+"       "+"subject"+"       "+"price")

for r in range(2, row + 1):
    for c in range(1, column + 1):
        value = driver.find_element_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(value, end="       ")
    print()
