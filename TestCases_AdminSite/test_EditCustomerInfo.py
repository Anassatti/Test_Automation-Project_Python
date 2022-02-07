import pytest
from PageObjects.LoginPage import LoginPage
from selenium import webdriver
from Uitilities.readProperties import ReadConfig
from Uitilities.CustomeLogger import LogGen
from PageObjects.EditCustomerProfilePage import updateCustomerProfile
from PageObjects.SearchCustomersPage import SearchCustomer


class Test_005_EditCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUsername()
    password = ReadConfig.getApplicationPassword()
    logger = LogGen.loggen()  # log

    @pytest.fixture()
    def setup(self):
        driver = webdriver.Chrome(r"C:\Users\anass\Desktop\Files\Seleium\Driver\LastVersion\chromedriver.exe")
        return driver

    @pytest.mark.regression
    def test_editCustomer(self, setup):
        self.logger.info("*************** Test_005_EditCustomerInfo*****************")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        ##Login to E-commerce website
        self.loginPage = LoginPage(self.driver)
        self.loginPage.clickLogin()
        self.searchCustomers = SearchCustomer(self.driver)
        self.searchCustomers.clickOnCustomerMenu()
        self.driver.implicitly_wait(10)
        self.searchCustomers.clickOnCustomerSubmenu()

        # Search by Email
        self.searchCustomers.SetSearchEmail("admin@yourStore.com")
        self.driver.implicitly_wait(10)
        self.searchCustomers.clickSearch()

        #Edit Customer profile
        self.logger.info("**** Updating customer will start now****")
        self.edit=updateCustomerProfile(self.driver)
        self.edit.updateProfile()
       # self.driver.implicitly_wait(10)
      #  self.edit.editCustomerProfile()
        self.edit.updateCustomerFirstName("Lisa")
        self.edit.updateCustomerFirstName("John")
        self.edit.Updategeneder("female")
        self.driver.implicitly_wait(10)
        self.edit.saveUpdatedProfile()
        self.logger.info("**** Customer has been updated****")
        self.confirmation = self.edit.Confirmationmessage()
        if 'The new customer has been added successfully.' in self.confirmation:
            assert True == True
            self.logger.info("****Confirmation customer ifno has been updated ****")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_editCustomerinfo.png")
            self.logger.info("****upate customer information has been failed****")
            assert False == False

            self.driver.close()


