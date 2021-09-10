
class ResultPage:

    def __init__(self, browser):
        self.browser = browser

    def text(self, locator):
        element = self.browser.find_element(*locator)
        return element.text