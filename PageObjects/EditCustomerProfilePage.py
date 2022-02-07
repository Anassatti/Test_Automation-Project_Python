class updateCustomerProfile:
    # locater

    btnEdit_linktext = "Edit"
    btnEditCustomerProfile_linktext = "Edit"
    txtFirstname_xpath = "//input[@id='FirstName']"
    txtLastname_xpath = "//input[@id='LastName']"
    rdFemaleGeneder_ID = "Gender_Female"
    rdMaleGeneder_ID = "Gender_Male"
    btnSave_xpath = "//button[@name='save']"
    SmConfirmationMessage_tagname = "body"
     #Initialize the driver
    def __init__(self, driver):
        self.driver = driver

    def updateProfile(self):
        self.driver.find_element_by_link_text(self.btnEdit_linktext).click()

    #def editCustomerProfile(self):
     #   self.driver.find_element_by_link_text(self.btnEditCustomerProfile_linktext).click()

    def updateCustomerFirstName(self, firstname):
        self.driver.find_element_by_xpath(self. txtFirstname_xpath).clear()
        self.driver.find_element_by_xpath(self. txtFirstname_xpath).send_keys(firstname)

    def updateCustomerLastName(self, lastname):
        self.driver.find_element_by_xpath(self.txtLastname_xpath).clear()
        self.driver.find_element_by_xpath(self.txtLastname_xpath).send_keys(lastname)

    def saveUpdatedProfile(self):
            self.driver.find_element_by_xpath(self.btnSave_xpath).click()

    def Confirmationmessage(self):
            return self.driver.find_element_by_tag_name(self.SmConfirmationMessage_tagname).text

    def Updategeneder(self, genederName):
        if genederName == "female":
            self.driver.find_element_by_id(self.rdFemaleGeneder_ID).click()

        else:
            self.driver.find_element_by_id(self.rdMaleGeneder_ID).click()




