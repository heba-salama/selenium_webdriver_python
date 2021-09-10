import pytest
import selenium.webdriver


@pytest.fixture
def browser():
    a = selenium.webdriver.Firefox()
    a.implicitly_wait(10)
    a.maximize_window()
    yield a
    a.quit()

