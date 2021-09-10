from selenium.webdriver.common.by import By


class RegistrationPage:

    # register inputs and button locators
    FEMALE = (By.ID, "gender-female")
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    CONFIRM_PASS = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")
    CONFIRM_ERROR = (By.ID, "ConfirmPassword-error")
    RESULT = (By.CLASS_NAME, "result")

    def __init__(self, browser):
        self.browser = browser

    def user_registration(self, firstname, lastname, email, password, confirm_pass):
        username = self.browser.find_element(*self.FIRST_NAME)
        username.send_keys(firstname)
        username = self.browser.find_element(*self.LAST_NAME)
        username.send_keys(lastname)
        username = self.browser.find_element(*self.EMAIL)
        username.send_keys(email)
        password_ = self.browser.find_element(*self.PASSWORD)
        password_.send_keys(password)
        password_ = self.browser.find_element(*self.CONFIRM_PASS)
        password_.send_keys(confirm_pass)
        sign_in = self.browser.find_element(*self.REGISTER_BUTTON)
        sign_in.click()