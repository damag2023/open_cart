import time

from pageObjects.HomePage import Homepage
from testCases.BaseClass import BaseClass
from utilities.log import LogGen
from utilities.readConfigFile import ReadConfig


class TestLogin(BaseClass):

    def test_TC_LF_001(self):
        """this test case validates logging into the Application using valid credentials"""
        log = LogGen.getLogger()
        log.info("Navigate to the login page")
        self.driver.get(ReadConfig.get_url())
        homepage = Homepage(self.driver)
        homepage.get_myaccount().click()
        loginpage = homepage.get_login()
        loginpage.get_email_element().send_keys("johndoe@gmail.com")
        loginpage.get_password_element().send_keys(ReadConfig.get_password())
        myAccountPage= loginpage.click_submit()
        if myAccountPage.driver.title == "Account Login":
            log.info("Log in successful")
            log.info(myAccountPage.driver.title)
            assert True
        else:
            log.info(myAccountPage.driver.title)
            log.error("log in not successful")
            assert False

