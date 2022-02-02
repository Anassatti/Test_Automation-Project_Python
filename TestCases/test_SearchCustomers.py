import pytest
from PageObjects.LoginPage import LoginPage
from selenium import webdriver
from Uitilities.readProperties import ReadConfig
from Uitilities.CustomeLogger import LogGen
from PageObjects.SearchCustomersPage import SearchCustomer


class Test_004_SearchCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUsername()
    password = ReadConfig.getApplicationPassword()
    logger = LogGen.loggen()  # log

    @pytest.fixture()
    def setup(self):
        driver = webdriver.Chrome(r"C:\Users\anass\Desktop\Files\Seleium\Driver\LastVersion\chromedriver.exe")
        return driver

    def test_searchCustomers(self, setup):
        self.logger.info("*************** Test_004_SearchCustomers*****************")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        ##Login to E-commerce website
        self.loginPage = LoginPage(self.driver)
        self.loginPage.clickLogin()

        self.logger.info("****Login Successfully****")
        self.logger.info("****Search customers by using email ****")

        self.searchCustomers = SearchCustomer(self.driver)
        self.searchCustomers.clickOnCustomerMenu()
        self.driver.implicitly_wait(10)
        self.searchCustomers.clickOnCustomerSubmenu()

        # Search by Emial
        self.searchCustomers.SetSearchEmail("admin@yourStore.com")
        self.driver.implicitly_wait(10)
        self.searchCustomers.clickSearch()

        self.logger.info("****Verify the searching result ****")
        verify= self.searchCustomers.verifySearchResult("admin@yourStore.com")
        assert True == verify
        self.logger.info("****customers existed within customers list ****")

