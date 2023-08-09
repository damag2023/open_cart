

from selenium.webdriver.common.by import By

from pageObjects.MyAccount import My_Account


class LoginPage():

    login_email = (By.CSS_SELECTOR,"#input-email")
    login_password=(By.CSS_SELECTOR,"#input-password")
    login_submit = (By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
    invalid_login= (By.CSS_SELECTOR,"#account-login > div.alert.alert-danger.alert-dismissible")

    def __init__(self, driver):
        self.driver=driver

    def get_email_element(self):
        return self.driver.find_element(*LoginPage.login_email)

    def get_password_element(self):
        return self.driver.find_element(*LoginPage.login_password)

    def get_invalid_login_errorMsg_element(self):
        return self.driver.find_element(*LoginPage.invalid_login)

    def click_submit(self):
        self.driver.find_element(*LoginPage.login_submit).click()
        myAccountPage = My_Account(self.driver)
        return myAccountPage