
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class AddCustomer:
    # Add customer page locators
    lnkCustomermain_Lnktext = "Customers"
    lnkCustomerSubmain_xpath =  "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    BtnAddcustomer_cssSelector = "i[class='fas fa-plus-square']"
    txtEmail_ID = "Email"
    txtPassword_ID = "Password"
    txtFirstname_ID = "FirstName"
    txtLastname_ID = "LastName"
    rdGeneder_ID = "Gender_Male"
    Dob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyname_ID = "Company"
    chTax_xpath = "//input[@id='IsTaxExempt']"
    IstNewsletters_dropDown_xpath = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[2]"
    IstNewsletter_xpath = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div/input"
    IstCustomerroles_xpath = "//li[@class='k-button']"
    IstDeleterole_xpath = "(//span[@title='delete'])[2]"
    IstSelectCustomerRole_xpath = "//li[@id='e03ce2c3-44cc-43bd-87a0-f6d73ba4d5f4']"
    IstManagerofVendors_ID = "VendorId"
    txtAdmincomment_ID= "AdminComment"
    btnSave_xpath = "//button[@name='save']"
    SmConfirmationMessage_tagname = "body"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):

        self.driver.find_element_by_link_text(self.lnkCustomermain_Lnktext).click()

    def clickOnCustomerSubmenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomerSubmain_xpath).click()

    def ClickOnAddcustomer(self):
        self.driver.find_element_by_css_selector(self.BtnAddcustomer_cssSelector).click()

    def SetEmail(self, email):
        self.driver.find_element_by_id(self.txtEmail_ID).send_keys(email)

    def SetPassword(self, password):
        self.driver.find_element_by_id(self.txtPassword_ID).send_keys(password)

    def SetFirstname(self, firstname):
        self.driver.find_element_by_id(self.txtFirstname_ID).send_keys(firstname)

    def SetLastname(self, lastname):
        self.driver.find_element_by_id(self.txtLastname_ID).send_keys(lastname)

    def Setgender(self):
        self.driver.find_element_by_id(self.rdGeneder_ID).click()

    def SetDateofbirth(self, dateofBirth):
        self.driver.find_element_by_xpath(self.Dob_xpath).send_keys(dateofBirth)

    def SetCompanyname(self, company):
        self.driver.find_element_by_id(self.txtCompanyname_ID).send_keys(company)

    def SetTaxexcemption(self):
        self.driver.find_element_by_xpath(self.chTax_xpath).click()

    def SetNewsletter(self):
        dropdown = self.driver.find_element_by_xpath(self.IstNewsletter_xpath)
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(dropdown).click(dropdown).perform()

        option = self.driver.find_element_by_xpath(self.IstNewsletters_dropDown_xpath)
        ActionChains(self.driver).move_to_element(option).click(option).perform()


    def SetCustomerRole(self):
        Rolevalue = self.driver.find_element_by_xpath(self.IstCustomerroles_xpath)
        if (Rolevalue == "Registered"):
            self.driver.implicitly_wait(10)
            deleteIcon = Rolevalue.find_element_by_xpath(self.IstDeleterole_xpath)
            ActionChains(self.driver).move_to_element(deleteIcon).click(deleteIcon).perform()
            self.driver.implicitly_wait(10)
            selectItem = self.driver.find_element_by_xpath(self.IstSelectCustomerRole_xpath)
            ActionChains(self.driver).move_to_element(selectItem).click(selectItem).perform()

    def SetVendor(self, vendor):
        select = Select(self.driver.find_element_by_id(self.IstManagerofVendors_ID))
        # select by visible text
        select.select_by_visible_text(vendor)

    def SetAdmincomment(self, comment):
        self.driver.find_element_by_id(self.txtAdmincomment_ID).send_keys(comment)

    def SaveCustomerdata(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()

    def ConfirmationMessage(self):
       return self.driver.find_element_by_tag_name(self.SmConfirmationMessage_tagname).text
