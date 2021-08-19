from PageActions.Commonfunction import CommonFunctions
from PageObjects.menu_objectlocators import Menu

import yaml
import time


with open(r'/home/srikanth/Desktop/selenium_project/pythonProject/Tests/TestData/wiki_creds.yaml', 'r') as file:
    f_creds = yaml.load(file)


cfunction = CommonFunctions()
g_objects = Menu()

driver=cfunction.open_url('https://testautomationpractice.blogspot.com/?m=1')
cfunction.maximize_browser()
time.sleep(2)

print(cfunction.get_page_title())

cfunction.click_on_element(g_objects.speed_xpath)
cfunction.click_on_element(g_objects.file_xpath)
cfunction.click_on_element(g_objects.number_xpath)
cfunction.click_on_element(g_objects.product_xpath)
cfunction.click_on_element(g_objects.animal_xpath)

