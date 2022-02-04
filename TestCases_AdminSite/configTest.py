import pytest
from selenium import webdriver


@pytest.fixture()
def SETUP(Browser):
    if Browser == "chrome":
        driver = webdriver.Chrome(r"C:\Users\anass\Desktop\Files\Seleium\Driver\LastVersion\chromedriver.exe")
    elif Browser == 'firfox':
        driver = webdriver.Firefox(r"C:\Users\anass\Desktop\Files\Seleium\Driver\LastVersion\geckodriver.exe")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def Browser(request):
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'ECommerce Website'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Anas Satti'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
