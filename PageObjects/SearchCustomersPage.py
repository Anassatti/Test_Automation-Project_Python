class SearchCustomer:
    # Search Page locators
    txtEmail_ID = "SearchEmail"
    btnSearch_ID = "search-customers"
    lnkCustomermain_Lnktext = "Customers"
    lnkCustomerSubmain_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    tableRow_xpath="//*[@id='customers-grid']/tbody/tr"
    table_xpath="//*[@id='customers-grid']"
    def __init__(self, driver):
        self.driver = driver

    def SetSearchEmail(self, email):
        self.driver.find_element_by_id(self.txtEmail_ID).send_keys(email)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btnSearch_ID).click()

    def clickOnCustomerMenu(self):

        self.driver.find_element_by_link_text(self.lnkCustomermain_Lnktext).click()

    def clickOnCustomerSubmenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomerSubmain_xpath).click()

    def numberOfRow(self):
        return len(self.driver.find_elements_by_xpath(self.tableRow_xpath))


    def verifySearchResult(self, email):
        flag=False
        for i in  range(1,self.numberOfRow()+1):
         table=self.driver.find_element_by_xpath(self.table_xpath)
          # to get all the cell data with text method
        emailsData= table.find_element_by_xpath ("//table[@id='customers-grid']/tbody/tr["+str(i)+"]/td[2]").text

        if emailsData == email:
            flag = True
            "break"
        return flag





