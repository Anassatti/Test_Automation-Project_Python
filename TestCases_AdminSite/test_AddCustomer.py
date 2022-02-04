import pytest
from PageObjects.LoginPage import LoginPage
from selenium import webdriver
from Uitilities.readProperties import ReadConfig
from Uitilities.CustomeLogger import LogGen
from PageObjects.AddCustomerPage import AddCustomer
import time
import random
import string
from selenium.webdriver.support.ui import WebDriverWait




class Test_003_Addcustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUsername()
    password = ReadConfig.getApplicationPassword()
    logger = LogGen.loggen()  # log

    @pytest.fixture()
    def setup(self):
        driver = webdriver.Chrome(r"C:\Users\anass\Desktop\Files\Seleium\Driver\LastVersion\chromedriver.exe")
        return driver

    @pytest.mark.sainty
    def test_addCustomer(self, setup):

        self.logger.info("*************** Test_003_addCustomer*****************")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        ##Login to E-commerce website
        self.loginPage = LoginPage(self.driver)
        ##  self.loginPage.setUsername(self.username)
        ## self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()

        self.logger.info("****Login Successfully****")
        self.logger.info("****Adding New Customer ****")

        self.addcustomer = AddCustomer(self.driver)
        self.addcustomer.clickOnCustomerMenu()
        self.driver.implicitly_wait(10)
        self.addcustomer.clickOnCustomerSubmenu()

        self.addcustomer.ClickOnAddcustomer()
        # time.sleep(2000)
        self.logger.info("****Adding New Customer Details ****")
        self.email = get_random_characters(6) + "@yahoo.com"
        self.addcustomer.SetEmail(self.email)
        self.addcustomer.SetPassword("123455667")
        self.addcustomer.SetFirstname("Anas")
        self.addcustomer.SetLastname("Satti")
        self.addcustomer.Setgender()
        self.addcustomer.SetDateofbirth("09/08/1985")
        self.addcustomer.SetCompanyname("DeepInsights")
        self.addcustomer.SetTaxexcemption()
        self.addcustomer.SetNewsletter()
        self.addcustomer.SetCustomerRole()
        self.addcustomer.SetVendor("Vendor 2")
        self.addcustomer.SetAdmincomment("My new company")

        ##Saving customer data
        self.logger.info("****Adding New Customer Details ****")
        self.addcustomer.SaveCustomerdata()
        self.logger.info("****Validation Customer has been added****")
        self.confirmation = self.addcustomer.ConfirmationMessage()
        if 'The new customer has been added successfully.' in self.confirmation:
            assert True == True
            self.logger.info("****Add new customer done successfully ****")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Addcustomer.png")
            self.logger.info("****Add new customer failed ****")
            assert False == False

            self.driver.close()

    ##Function for generate data for the email

def get_random_characters(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str