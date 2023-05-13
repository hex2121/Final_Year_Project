from AutomationController.DriverUtilities.DriverUtils import DriverUtilitiesMethod
from Locators.HomePageLocators import *
from Config.Credentials import *
from App.SignInPage import SignInPage


class HomePage(DriverUtilitiesMethod):

    def sign_in(self, driver):
        self.click_element(element_locator=sign_in_button, find_by='xpath')
        SignInPage(driver, explicit_timeout=10).sign_in_flow()

    def search_item(self, item):
        self.input_text_in_field(element_locator=search_field, find_by='css', text=item)
        self.click_element(element_locator=search_button, find_by='css')
