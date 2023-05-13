import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import sys
import json


class DriverBase:

    driver_run = None

    def __init__(self):
        self.driver_run = 'chrome'

    def initiate_driver(self, download_dir_path=None):
        print("the driver is {}".format(self.driver_run))
        if self.driver_run.lower() == 'chrome':

            op = webdriver.ChromeOptions()

            settings = {
                "recentDestinations": [{
                    "id": "Save as PDF",
                    "origin": "local",
                    "account": "",
                }],
                "selectedDestinationId": "Save as PDF",
                "version": 2
            }

            preference = {'printing.print_preview_sticky_settings.appState': json.dumps(settings),
                          'savefile.default_directory': f'{download_dir_path}'}

            op.add_experimental_option("prefs", preference)
            op.add_argument('--kiosk-printing')
            # for initiating driver in chrome
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)

        elif self.driver_run.lower() == 'firefox':
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        elif self.driver_run.lower() == 'edge':
            driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        else:
            print("Currently {} driver is not supported".format(self.driver_run))
            sys.exit(2)
        return driver

    @staticmethod
    def close_driver_instance(driver_instance, all_tab=False):
        if not all_tab:
            driver_instance.close()
        else:
            driver_instance.quit()
