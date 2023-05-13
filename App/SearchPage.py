from selenium.webdriver.common.by import By
from AutomationController.DriverUtilities.DriverUtils import DriverUtilitiesMethod


class SearchPage(DriverUtilitiesMethod):

    def open_searched_item(self, driver, item):
        try:
            elements = driver.find_elements(value=f"//a/span[contains(text(),'{item}')]", by=By.XPATH)
            elements[0].click()
            self.switch_to_tab(0)
        except:
            print("item was not found")
