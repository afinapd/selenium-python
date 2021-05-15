class LoginPage():
    emailId = "Email"
    passwordId = "Password"
    submitXPath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input"
    logoutLinkText = "Logout"

    def __init__(self, driver):
        self.driver=driver

    def setEmail(self, email):
        self.driver.find_element_by_id(self.emailId).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.passwordId).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.submitXPath).click

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.logoutLinkText).click