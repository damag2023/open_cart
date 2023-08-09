from selenium.webdriver.common.by import By


class Registration:
    first_name= (By.CSS_SELECTOR, "#input-firstname")
    last_name = (By.CSS_SELECTOR, "#input-lastname")
    email =(By.CSS_SELECTOR, "#input-email")
    telephone=(By.CSS_SELECTOR, "#input-telephone")
    password= (By.CSS_SELECTOR, "#input-password")
    confirm_password = (By.CSS_SELECTOR, "#input-confirm")
    continue_button = (By.XPATH,'//*[@id="content"]/form/div/div/input[2]')
    terms_checkbox = (By.XPATH, '//*[@id="content"]/form/div/div/input[1]')
    confirmation_text = (By.CSS_SELECTOR, "#content > h1")
    continue_registration = (By.CSS_SELECTOR, "#content > div > div > a")
    first_name_error = (By.CSS_SELECTOR, '#account > div:nth-child(3) > div > div')
    last_name_error = (By.CSS_SELECTOR, "#account > div:nth-child(4) > div > div")
    email_error = (By.CSS_SELECTOR, "#account > div:nth-child(5) > div > div")
    telephone_error = (By.CSS_SELECTOR, "#account > div:nth-child(6) > div > div")
    password_error = (By.CSS_SELECTOR, "#content > form > fieldset:nth-child(2) > div.form-group.required.has-error > div > div")
    terms_error = (By.CSS_SELECTOR, "#account-register > div.alert.alert-danger.alert-dismissible")
    password_mismatch_error=(By.CSS_SELECTOR, "#content > form > fieldset:nth-child(2) > div.form-group.required.has-error > div > div")


    def __init__(self, driver):
        self.driver=driver

    def get_firstName_element(self):
        return self.driver.find_element(*Registration.first_name)

    def get_lastName_element(self):
        return self.driver.find_element(*Registration.last_name)

    def get_email_element(self):
        return self.driver.find_element(*Registration.email)

    def get_telephone_element(self):
        return self.driver.find_element(*Registration.telephone)

    def get_firstPassword_element(self):
        return self.driver.find_element(*Registration.password)

    def get_confirmPassword_element(self):
        return self.driver.find_element(*Registration.confirm_password)

    def get_agreeterms_element(self):
        return self.driver.find_element(*Registration.terms_checkbox)

    def get_continuebutton_element(self):
        return self.driver.find_element(*Registration.continue_button)

    def get_confirmation_text_element(self):
        return self.driver.find_element(*Registration.confirmation_text)

    def get_continue_homepage_element(self):
        return self.driver.find_element(*Registration.continue_registration)


    def get_fnameError_element(self):
        return self.driver.find_element(*Registration.first_name_error)

    def get_lnameError_element(self):
        return self.driver.find_element(*Registration.last_name_error)

    def get_emailError_element(self):
        return self.driver.find_element(*Registration.email_error)

    def get_telephoneError_element(self):
        return self.driver.find_element(*Registration.telephone_error)

    def get_passwordError_element(self):
        return self.driver.find_element(*Registration.password_error)

    def get_termsError_element(self):
        return self.driver.find_element(*Registration.terms_error)

    def get_passwordMismatchError_element(self):
        return self.driver.find_element(*Registration.password_mismatch_error)


