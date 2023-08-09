from pageObjects.HomePage import Homepage
from testCases.BaseClass import BaseClass
from utilities.log import LogGen


class Test_TC_RF_008(BaseClass):

    def test_TC_RF_008(self):
        """This test case validates that the user is unable to register an account when the password doesnt match the
        confirmation password"""
        log =LogGen.getLogger()
        log.debug(" Open the browser")
        self.driver.get("https://opencart.antropy.co.uk/index.php?route=common/home")
        log.debug("Navigated to the homepage")
        homepage = Homepage(self.driver)
        homepage.get_myaccount().click()
        registration = homepage.get_register()
        log.debug("Navigated to the account registration page")
        registration.get_firstName_element().send_keys("Dave")
        registration.get_lastName_element().send_keys("Thomas")
        registration.get_telephone_element().send_keys("457-895-8965")
        registration.get_email_element().send_keys("afhlks@gmail.com")

        registration.get_firstPassword_element().send_keys("Password#1")
        registration.get_confirmPassword_element().send_keys("Password#2")
        log.info("Provided password that doesnt match")
        registration.get_continuebutton_element().click()
        if registration.get_passwordMismatchError_element().text == "Password confirmation does not match password!":
            log.info("Password mismatch error message displayed")
            assert True
        else:
            log.error("Password mismatch error message not displayed")
            assert False


