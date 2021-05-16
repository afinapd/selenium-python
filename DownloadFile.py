from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Locators.Constants import Constants

ChromeOptions=Options()
ChromeOptions.add_experimental_option("prefs",{"download.default_directory":"C:\\Users\\NB01\\Pictures"})

driver = webdriver.Chrome(executable_path=Constants.driver)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

#download text
# driver.find_element_by_id("textbox").send_keys("hello world")
# driver.find_element_by_id("createTxt").click()
# driver.find_element_by_id("link-to-download").click()

#download pdf
driver.find_element_by_id("pdfbox").send_keys("hello world")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()