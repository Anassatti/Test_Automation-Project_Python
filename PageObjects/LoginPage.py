class LoginPage:
    Textbox_username_id = "Email"
    Textbox_password_id = "Password"
    Button_login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    Link_logout_xpath = "//a[@href='/logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_id(self.Textbox_username_id).clear()
        self.driver.find_element_by_id(self.Textbox_username_id).send_keys(username)

    def setPassword(self, password):
       ## self.driver.find_element_by_id(self.Textbox_username_id).clear()
        self.driver.find_element_by_id(self.Textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.Button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.Link_logout_xpath).click()
