from PageActions.Commonfunction import CommonFunctions
from PageObjects.windows_objectlocators import Searchbrowser

import yaml
import time


with open(r'/home/srikanth/Desktop/selenium_project/pythonProject/Tests/TestData/wiki_creds.yaml', 'r') as file:
    f_creds = yaml.load(file)


cfunction = CommonFunctions()
g_objects = Searchbrowser()

driver=cfunction.open_url('https://testautomationpractice.blogspot.com/?m=1')
cfunction.maximize_browser()
time.sleep(2)

print(cfunction.get_page_title())


cfunction.click_on_inputs_send_keys(g_objects.search_xpath, f_creds["wiki"])
cfunction.click_on_element(g_objects.click_btn_xpath)
cfunction.click_on_element(g_objects.selected_link_xpath)
cfunction.click_on_element(g_objects.alert_xpath)
time.sleep(1)
cfunction.alerts_browser()
cfunction.click_on_element(g_objects.date_picker_xpath)
cfunction.click_on_element(g_objects.prev_xpath)
cfunction.click_on_element(g_objects.month_xpath)
cfunction.click_on_element(g_objects.year_xpath)



