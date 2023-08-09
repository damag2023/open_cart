import time

from pageObjects.HomePage import Homepage
from testCases.BaseClass import BaseClass
from utilities.log import LogGen
from utilities.readConfigFile import ReadConfig


class TestLogin(BaseClass):

    def test_TC_LF_002(self):
        """this test case validates logging into the Application using invalid credentials"""
        log = LogGen.getLogger()
        log.info("Navigate to the login page")
        self.driver.get(ReadConfig.get_url())
        homepage = Homepage(self.driver)
        homepage.get_myaccount().click()
        loginpage = homepage.get_login()
        loginpage.get_email_element().send_keys("daveshawn@gmail.com")
        loginpage.get_password_element().send_keys("Password#2")
        myAccountPage= loginpage.click_submit()
        if loginpage.get_invalid_login_errorMsg_element().text == "Warning: No match for E-Mail Address and/or Password.":
            log.info("login error message displayed as expected")
            assert True
        else:
            log.error("log in error message nto displayed")
            assert False

