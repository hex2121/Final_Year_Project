from selenium.webdriver import ActionChains


class MouseUtilitiesMethod:

    def __init__(self, driver):
        self._driver = driver
        self.action = ActionChains(self._driver)

    def move_to_specific_element(self, element):
        self.action.move_to_element(element)
        self.action.perform()

