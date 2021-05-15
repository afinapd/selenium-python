from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\afinapd\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()

#scroll by pixel
# driver.execute_script("window.scrollBy(0,1000)","")

#scroll till the element is visible
# flag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[47]")
# driver.execute_script("arguments[0].scrollIntoView();",flag)

#scroll page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

