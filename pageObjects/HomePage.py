from selenium.webdriver.common.by import By

from pageObjects.Login import LoginPage
from pageObjects.Registration import Registration



class Homepage:

    my_account = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/span[1]')
    register = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[1]/a')
    login = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a')

    def __init__(self, driver):
        self.driver=driver

    def get_myaccount(self):
        return self.driver.find_element(*Homepage.my_account)

    def get_register(self):
        self.driver.find_element(*Homepage.register).click()
        register = Registration(self.driver)
        return register

    def get_login(self):
        self.driver.find_element(*Homepage.login).click()
        login_page = LoginPage(self.driver)
        return login_page


    def get_title(self):
        return self.driver.title