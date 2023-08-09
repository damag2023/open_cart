import time

from pageObjects.HomePage import Homepage
from testCases.BaseClass import BaseClass
from utilities.log import LogGen


class Test_TC_RF_004(BaseClass):


    def test_TC_RF_004(self):
        log = LogGen.getLogger()
        log.debug(" Open the browser")
        self.driver.get("https://opencart.antropy.co.uk/index.php?route=common/home")
        log.debug("Navigated to the homepage")
        homepage = Homepage(self.driver)
        homepage.get_myaccount().click()
        registration = homepage.get_register()
        registration.get_continuebutton_element().click()
        log.info("Navigated to the account registration page")

        if registration.get_firstName_element().text == "":
            log.info("Blank first name")
            if registration.get_fnameError_element().text =="First Name must be between 1 and 32 characters!":
                log.info("Error message displayed")
                assert True
            else:
                log.error("Error message not displayed")
                assert False


        if registration.get_firstName_element().text == "":
            print("Blank last name")
            if registration.get_lnameError_element().text =="Last Name must be between 1 and 32 characters!":
                assert True
            else:
                assert False

        if registration.get_termsError_element().get_attribute("checked") != "true":
            print("Terms box not checked")
            if registration.get_termsError_element().text =="Warning: You must agree to the Privacy Policy!":
                assert True
            else:
                assert False