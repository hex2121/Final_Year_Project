from AutomationController.DriverUtilities.DriverBasePage import DriverBase
from AutomationController.DriverUtilities.DriverUtils import DriverUtilitiesMethod
from App.SearchPage import SearchPage
from App.HomePage import HomePage
from App.ItemPage import ItemPage
from Config.Credentials import *
import time

def process():
    driver = DriverBase().initiate_driver()
    DriverUtilitiesMethod(driver, 10).navigate_to_url("https://www.amazon.in/")
    HomePage(driver, 10).sign_in(driver)
    HomePage(driver, 10).search_item(item=item_for_search)
    SearchPage(driver, 10).open_searched_item(driver, item_for_search)
    ItemPage(driver, 10).add_to_cart()
    ItemPage(driver, 10).proceed_to_checkout()
    time.sleep(10)
    driver.quit()



if __name__ == '__main__':
    process()

