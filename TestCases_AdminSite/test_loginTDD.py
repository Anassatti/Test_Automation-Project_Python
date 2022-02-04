
import pytest
from PageObjects.LoginPage import LoginPage
from selenium import webdriver
from Uitilities.readProperties import ReadConfig
from Uitilities.CustomeLogger import LogGen
from Uitilities import XLUitlities
import time


class Test_002_TDD_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/Testdata.xlsx"
    username = ReadConfig.getApplicationUsername()
    password = ReadConfig.getApplicationPassword()
    logger = LogGen.loggen()

    @pytest.fixture()
    def setup(self):
        driver = webdriver.Chrome(r"C:\Users\anass\Desktop\Files\Seleium\Driver\LastVersion\chromedriver.exe")
        return driver

    @pytest.mark.regression
    def test_homePageTitle_ddt(self, setup):

        self.logger.info("*************** Test_002_Login_DDT *****************")
        self.logger.info("****Verify Home page title test ****")

        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.logger.info("**** Verified passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitleTDD.png")
            self.driver.close()
            assert False
    #Test if login & logout works
    @pytest.mark.regression
    def test_login_TDD(self, setup):

        self.logger.info("****Start Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        #Reading test login data from excel sheet
        self.rows = XLUitlities.getRowCount(self.path, 'Sheet1')
        print("Number of rows is:", self.rows)
        list_status = []
        for r in range(2, self.rows + 1):
            self.username = XLUitlities.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUitlities.readData(self.path, 'Sheet1', r, 2)
            self.result = XLUitlities.readData(self.path, 'Sheet1', r, 3)
         #Verifying page title
        self.loginpage = LoginPage(self.driver)
      ##  self.loginpage.setUsername(self.username)
       ## self.loginpage.setPassword(self.password)
        self.loginpage.clickLogin()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            if self.result == "Pass":
                self.logger.info("**** passed ****")
                self.loginpage.clickLogout()
                list_status.append("pass")
           # self.driver.close()
            assert True
        elif self.result == "fail":
            self.logger.error("**** failed ****")
            self.loginpage.clickLogout()
            list_status.append("fail")

        if "fail" not in list_status:
            self.logger.info("**passed_testloginTDD**")
            self.driver.close()
            assert True
        else:
            self.logger.info("**Fail_TDD**")
            self.driver.close()
            assert False

