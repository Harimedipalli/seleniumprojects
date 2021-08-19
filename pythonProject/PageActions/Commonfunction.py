"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.alert import Alert




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


    def change_window_tab(self, tab_number):

        change_window = self.browser.window_handles[tab_number]

        self.browser.switch_to.window(change_window)

    def switch_to_frame(self, xpath):
        """
            This function will do -
                - switch the frame
        :return:    
        """

        self.browser.switch_to.frame(self.browser.find_element_by_xpath(xpath))

    def move_element(self,xpath,x,y):
        """

        :param x_path:
        :return:
        """
        time.sleep(3)
        move_action = ActionChains(self.browser)
        move_action.click_and_hold(xpath).move_by_offset(x,y).release().perform()


    def double_click(self, xpath):
        """

        :return:
        """
        time.sleep(3)

        action_chains = ActionChains(self.browser)
        action_chains.double_click(xpath).perform()


    def clear_on_element(self, xpath):
        """
        :return:
        """
        time.sleep(3)
        self.browser.find_element_by_xpath(xpath).clear()

    def drag_and_drop(self, source, target):
        """

        :param source:
        :param target:
        :return:
        """
        auto_chains = ActionChains(self.browser)
        auto_chains.drag_and_drop(source, target).perform()


    def click_hold_move(self, source, target):
        """
        :param source:
        :param target:
        :return:
        """

        action_chains = ActionChains(self.browser)
        action_chains.click_and_hold(source).move_to_element(target).release().perform()



    def slider_element(self, source,xaxis,yaxis):
        """

        :return:
        """
        action_chains = ActionChains(self.browser)
        action_chains.drag_and_drop_by_offset(source,xaxis,yaxis)


    def scroll_down(self):
        """


        :return:
        """
        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()


    def alerts_browser(self):
        """
        :return:
        """
        self.browser.switch_to.alert.accept()
