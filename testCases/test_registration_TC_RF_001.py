import os
import time

import pytest

from pageObjects.HomePage import Homepage
from pageObjects.Registration import Registration
from testCases.BaseClass import BaseClass
from utilities.log import LogGen


class TestRegistration(BaseClass):
    @pytest.mark.skip
    def test_TC_RF_001(self):
        """This test case validates a user is able to register a new account."""
        log =LogGen.getLogger()
        log.debug(" Open the browser")
        self.driver.get("https://opencart.antropy.co.uk/index.php?route=common/home")
        log.info("Navigated to the homepage")
        homepage = Homepage(self.driver)
        homepage.get_myaccount().click()
        registration = homepage.get_register()
        log.info("Navigated to the account registration page")
        registration.get_firstName_element().send_keys("Dave")
        registration.get_lastName_element().send_keys("Thomas")
        registration.get_telephone_element().send_keys("457-895-8965")
        registration.get_email_element().send_keys("")
        registration.get_firstPassword_element().send_keys("Password#1")
        registration.get_confirmPassword_element().send_keys("Password#1")

        time.sleep(10)
        registration.get_agreeterms_element().click()
        registration.get_continuebutton_element().click()
        confirmation_msg = "Your Account Has Been Created!"
        if confirmation_msg == registration.get_confirmation_text_element().text:
            log.debug("Registered ned user successfully")
            assert True
            registration.get_continue_homepage_element().click()
        else:
            log.error("Unable to register the account")
            self.driver.save_screenshot(os.path.dirname(os.getcwd()) + "\\screenshots"
                                                                       "\\test_register.png")
            assert False
        time.sleep(3)
