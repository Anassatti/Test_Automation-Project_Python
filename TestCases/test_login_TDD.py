
import pytest
from PageObjects.LoginPage import LoginPage
from selenium import webdriver
from Uitilities.readProperties import ReadConfig
from Uitilities.CustomeLogger import LogGen
from Uitilities import XLUitlities
import time


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/Testdata.xlsx"
    username = ReadConfig.getApplicationUsername()
    password = ReadConfig.getApplicationPassword()
    logger = LogGen.loggen()

    @pytest.fixture()
    def setup(self):
        driver = webdriver.Chrome(r"C:\Users\anass\Desktop\Files\Seleium\Driver\LastVersion\chromedriver.exe")
        return driver

    def test_homePageTitle_ddt(self, setup):

        self.logger.info("*************** Test_002_Login_DDT *****************")
        self.logger.info("****Started Home page title test ****")

        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    ## @pytest.mark.sanity

    ##@pytest.mark.regression

    def test_login(self, setup):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.rows = XLUitlities.getRowCount(self.path, 'Sheet1')
        print("Number of rows is:", self.rows)
        list_status = []
        for r in range(2, self.rows + 1):
            self.username = XLUitlities.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUitlities.readData(self.path, 'Sheet1', r, 2)
            self.result = XLUitlities.readData(self.path, 'Sheet1', r, 3)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            if self.result == "Pass":
                self.logger.info("**** passed ****")
                self.clickLogout()
                list_status.append("pass")
            self.driver.close()
            assert True
        elif self.result == "fail":
            self.logger.error("**** failed ****")
            self.clickLogout()
            list_status.append("fail")

        if "fail" not in list_status:
            self.logger.info("###passed_DDT##")
            self.driver.close()
            assert True
        else:
            self.logger.info("###Fail_DDT##")
        assert False
