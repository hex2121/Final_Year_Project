from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class DriverUtilitiesMethod:

    def __init__(self, driver, explicit_timeout):
        self.driver = driver
        self.explicit_timeout = explicit_timeout

    def navigate_to_url(self, url):
        self.driver.get(url)

    def set_browser_window_size(self, width=0, height=0):
        if not width or not height:
            self.driver.maximize_window()
        else:
            self.driver.set_window_size(width=width, height=height)

    def explicitly_wait_till_presence_of_element_located(self, element_locator: str, find_by="xpath",
                                                         explicit_wait_multiplier=1):

        if find_by.lower() == "css":
            WebDriverWait(driver=self.driver, timeout=self.explicit_timeout * explicit_wait_multiplier). \
                until(EC.presence_of_element_located((By.CSS_SELECTOR, element_locator)))

        elif find_by.lower() == "xpath":
            WebDriverWait(driver=self.driver, timeout=self.explicit_timeout * explicit_wait_multiplier). \
                until(EC.presence_of_element_located((By.XPATH, element_locator)))

        else:
            raise 'The value of Find By is Apart from XPATH and CSS so please create either XPATH or CSS'

    def explicitly_wait_till_visibility_of_element_located(self, element_locator: str, find_by="xpath",
                                                           explicit_wait_multiplier=1):

        if find_by.lower() == "css":
            WebDriverWait(driver=self.driver, timeout=self.explicit_timeout * explicit_wait_multiplier). \
                until(EC.visibility_of_element_located((By.CSS_SELECTOR, element_locator)))

        elif find_by.lower() == "xpath":
            WebDriverWait(driver=self.driver, timeout=self.explicit_timeout * explicit_wait_multiplier). \
                until(EC.visibility_of_element_located((By.XPATH, element_locator)))

        else:
            raise 'The value of Find By is Apart from XPATH and CSS so please create either XPATH or CSS'

    def explicitly_wait_till_element_is_clickable(self, element_locator: str, find_by="xpath",
                                                  explicit_wait_multiplier=1):

        if find_by.lower() == "css":
            WebDriverWait(driver=self.driver, timeout=self.explicit_timeout * explicit_wait_multiplier). \
                until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_locator)))

        elif find_by.lower() == "xpath":
            WebDriverWait(driver=self.driver, timeout=self.explicit_timeout * explicit_wait_multiplier). \
                until(EC.element_to_be_clickable((By.XPATH, element_locator)))

        else:
            raise 'The value of Find By is Apart from XPATH and CSS so please create either XPATH or CSS'

    def scroll_to_webelement(self, element_locator: str, find_by="xpath", explicit_wait_multiplier=1):

        self.explicitly_wait_till_presence_of_element_located(element_locator=element_locator,
                                                              find_by=find_by,
                                                              explicit_wait_multiplier=explicit_wait_multiplier)
        if find_by.lower() == "css":
            element = self.driver.find_element(by=By.CSS_SELECTOR, value=element_locator)
            element.location_once_scrolled_into_view

        elif find_by.lower() == "xpath":
            element = self.driver.find_element(by=By.XPATH, value=element_locator)
            element.location_once_scrolled_into_view

        else:
            raise 'The value of Find By is Apart from XPATH and CSS so please create either XPATH or CSS'

    def click_element(self, element_locator: str, find_by="xpath", explicit_wait_multiplier=1):

        self.explicitly_wait_till_element_is_clickable(element_locator=element_locator,
                                                       find_by=find_by,
                                                       explicit_wait_multiplier=explicit_wait_multiplier)

        if find_by.lower() == "css":
            self.driver.find_element(by=By.CSS_SELECTOR, value=element_locator).click()

        elif find_by.lower() == "xpath":
            self.driver.find_element(by=By.XPATH, value=element_locator).click()

        else:
            raise 'The value of Find By is Apart from XPATH and CSS so please create either XPATH or CSS'

    def input_text_in_field(self, element_locator: str, text: str, find_by="xpath", explicit_wait_multiplier=1):

        self.explicitly_wait_till_visibility_of_element_located(element_locator=element_locator,
                                                                find_by=find_by,
                                                                explicit_wait_multiplier=explicit_wait_multiplier)
        if find_by.lower() == "css":
            self.driver.find_element(by=By.CSS_SELECTOR, value=element_locator).send_keys(text)
        elif find_by.lower() == "xpath":
            self.driver.find_element(by=By.XPATH, value=element_locator).send_keys(text)
        else:
            raise 'The value of Find By is Apart from XPATH and CSS so please create either XPATH or CSS'

    def get_text(self, element_locator: str, find_by="xpath", explicit_wait_multiplier=1) -> str:

        self.explicitly_wait_till_visibility_of_element_located(element_locator=element_locator,
                                                                find_by=find_by,
                                                                explicit_wait_multiplier=explicit_wait_multiplier)

        if find_by.lower() == "css":

            return self.driver.find_element(by=By.CSS_SELECTOR, value=element_locator).text

        elif find_by.lower() == "xpath":
            return self.driver.find_element(by=By.CSS_SELECTOR, value=element_locator).text

        else:
            raise 'The value of Find By is Apart from XPATH and CSS so please create either XPATH or CSS'

    def press_keyboard_key(self, key: Keys):
        actions = ActionChains(self.driver)
        actions = actions.send_keys(key)
        actions.perform()

    def press_tab(self) -> None:
        self.press_keyboard_key(key=Keys.TAB)

    def verify_presence_of_element_in_dom(self, element_locator: str, find_by='xpath', explicit_wait_multiplier=4):

        try:
            self.explicitly_wait_till_presence_of_element_located(element_locator=element_locator,
                                                                  find_by=find_by,
                                                                  explicit_wait_multiplier=explicit_wait_multiplier)
            return True

        except:
            return False

    def count_number_of_elements(self, element_locator: str, find_by="xpath", explicit_wait_multiplier=1):

        self.explicitly_wait_till_presence_of_element_located(element_locator=element_locator,
                                                              find_by=find_by,
                                                              explicit_wait_multiplier=explicit_wait_multiplier)

        if find_by.lower() == "css":
            return len(self.driver.find_elements(by=By.CSS_SELECTOR, value=element_locator))

        elif find_by.lower() == "xpath":
            return len(self.driver.find_elements(by=By.XPATH, value=element_locator))

        else:
            raise 'The value of Find By is Apart from XPATH and CSS so please create either XPATH or CSS'

    def select_from_dropdown_using_visible_text(self, element_locator: str, visible_text: str,
                                                find_by="xpath", explicit_wait_multiplier=1):

        self.explicitly_wait_till_visibility_of_element_located(element_locator=element_locator,
                                                                find_by=find_by,
                                                                explicit_wait_multiplier=explicit_wait_multiplier)

        if find_by.lower() == "css":
            select = Select(self.driver.find_element(by=By.CSS_SELECTOR, value=element_locator))
            select.select_by_visible_text(text=visible_text)

        elif find_by.lower() == "xpath":
            select = Select(self.driver.find_element(by=By.XPATH, value=element_locator))
            select.select_by_visible_text(text=visible_text)

        else:
            raise 'The value of Find By is Apart from XPATH and CSS so please create either XPATH or CSS'

    def select_from_dropdown_using_index(self, element_locator: str, index: int, find_by="xpath",
                                         explicit_wait_multiplier=1):

        self.explicitly_wait_till_visibility_of_element_located(element_locator=element_locator,
                                                                find_by=find_by,
                                                                explicit_wait_multiplier=explicit_wait_multiplier)

        if find_by.lower() == "css":
            select = Select(self.driver.find_element(by=By.CSS_SELECTOR, value=element_locator))
            select.select_by_index(index=index)

        elif find_by.lower() == "xpath":
            select = Select(self.driver.find_element(by=By.XPATH, value=element_locator))
            select.select_by_index(index=index)

        else:
            raise 'The value of Find By is Apart from XPATH and CSS so please create either XPATH or CSS'

    def switch_to_alert(self):
        return self.driver.switch_to().alert()

    def accept_alert(self):
        self.switch_to_alert().accept()
        # Alert(driver=self.driver).accept()

    def dismiss_alert(self):
        self.switch_to_alert().dismiss()

    def switch_to_iframe(self, iframe_locator: str, find_by="xpath", explicit_wait_multiplier=2):

        self.explicitly_wait_till_presence_of_element_located(element_locator=iframe_locator,
                                                              find_by=find_by,
                                                              explicit_wait_multiplier=explicit_wait_multiplier)

        if find_by.lower() == "css":
            self.driver.switch_to.frame(self.driver.find_element(by=By.CSS_SELECTOR, value=iframe_locator))

        elif find_by.lower() == "xpath":
            self.driver.switch_to.frame(self.driver.find_element(by=By.XPATH, value=iframe_locator))

        else:
            raise 'The value of Find By is Apart from XPATH and CSS so please create either XPATH or CSS'

    # need to ask question
    # it should be named switch_to_tab or switch_to_window
    def switch_to_tab(self, tab_index: int = None, tab_id=None):

        if tab_index is not None:
            tabs = self.driver.window_handles
            self.driver.switch_to.window(tabs[tab_index])

        elif tab_id is not None:
            self.driver.switch_to.window(tab_id)

        else:
            raise 'The value of tab_index or tab_id is not provided'

    def switch_to_parent_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def switch_to_main_content(self):
        self.driver.switch_to.default_content()

    def close_current_window(self):
        self.driver.close()

    def close_all_opened_windows(self):
        self.driver.quit()
