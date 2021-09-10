import os
from dotenv import load_dotenv
from pages.registration_page import RegistrationPage
from pages.result import ResultPage
from pages.home_page import HomePage


load_dotenv()


def test_register_success(browser):
    """ Test Register Page Elements """
    print(test_register_success.__doc__)

    register_page = RegistrationPage(browser)
    home_page = HomePage(browser)
    result_page = ResultPage(browser)

    home_page.load()
    home_page.open_reg_page()
    register_page.user_registration(os.getenv('FIRST_NAME'), os.getenv('LAST_NAME'), os.getenv('EMAIL'),
                                    os.getenv('PASSWORD'), os.getenv('PASSWORD'))

    result = result_page.text(register_page.RESULT)

    assert result == "Your registration completed"


def test_register_fail(browser):
    """ Test Register Page Elements """
    print(test_register_success.__doc__)

    register_page = RegistrationPage(browser)
    home_page = HomePage(browser)
    result_page = ResultPage(browser)

    home_page.load()
    register_page.user_registration(os.getenv('FIRST_NAME'), os.getenv('LAST_NAME'), os.getenv('EMAIL'),
                                    os.getenv('PASSWORD'), os.getenv('CONFIRM_PASSWORD'))

    result = result_page.text(register_page.CONFIRM_ERROR)

    assert result == "The password and confirmation password do not match."