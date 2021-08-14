"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CommonFunctions:
    """

    """

    def __init__(self):
        """

        """
        self.browser = webdriver.Chrome("../AppDrivers/chromedriver.exe")

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