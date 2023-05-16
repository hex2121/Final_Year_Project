from selenium.webdriver.common.by import By
from AutomationController.DriverUtilities.DriverUtils import DriverUtilitiesMethod


class SearchPage(DriverUtilitiesMethod):

    def open_searched_item(self, driver, item):
        elements = driver.find_elements(value=f"//span[contains(text(),'{item}')]//parent::a", by=By.XPATH)
        try:
            elements[0].click()
            self.switch_to_tab(1)
        except:
            elements[1].click()
            self.switch_to_tab(1)