"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver import ActionChains

class CommonFunctions:
    """

    """

    def __init__(self):
        """

        """
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_experimental_option("prefs",
                                       {"profile.default_content_setting_values.notifications": 2
                                        })
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)

    def open_url(self, url):
        """

        :return:
        """
        self.browser.get(url)

    def minimize_browser(self):
        """

        :return:
        """
        self.browser.minimize_window()

    def maximize_browser(self):
        """

        :return:
        """
        self.browser.maximize_window()

    def get_page_title(self):
        """

        :return:
        """
        return self.browser.title

    def click_on_inputs_send_keys(self, x_path, value):
        """

        :param x_path:
        :param value:
        :return:
        """
        time.sleep(3)
        self.browser.find_element(By.XPATH, x_path).send_keys(value)

    def click_on_element(self, x_path):
        """

        :param x_path:
        :return:
        """
        time.sleep(3)
        self.browser.find_element(By.XPATH, x_path).click()

    def move_element(self,xpath):
        """

        :param x_path:
        :return:
        """
        time.sleep(3)
        move_action = ActionChains(self.browser)
        move_action.move_to_element(xpath)

    def change_window_tab(self, tab_number):

        change_window = self.browser.window_handles[tab_number]
        self.browser.switch_to.window(change_window)