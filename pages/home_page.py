import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By


class HomePage:

    load_dotenv()

    REGISTER = (By.LINK_TEXT, "Register")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(os.getenv('URL'))

    def open_reg_page(self):
        payments = self.browser.find_element(*self.REGISTER)
        payments.click()
