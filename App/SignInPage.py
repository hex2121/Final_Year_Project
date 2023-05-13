from AutomationController.DriverUtilities.DriverUtils import DriverUtilitiesMethod
from Locators.SignInPageLocators import *
from Config.Credentials import *


class SignInPage(DriverUtilitiesMethod):

    def sign_in_flow(self):
        self.input_text_in_field(element_locator=mail_field, find_by='xpath', text=mail_or_number_for_signin)
        self.click_element(element_locator=continue_btn, find_by='xpath')
        self.input_text_in_field(element_locator=password_field, find_by='css', text=password_for_sign_in)
        self.click_element(element_locator=sign_in_btn, find_by='css')


