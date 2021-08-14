from PageActions.Commonfunctions import CommonFunctions
from PageObjects.Facebook_objectlocators import FacebookLogin
import time
import yaml


with open('TestData/f_creds.yaml', 'r') as file:
    f_creds = yaml.load(file)

cfunction = CommonFunctions()
g_objects = FacebookLogin()

cfunction.open_url('https://www.facebook.com/')
cfunction.maximize_browser()
time.sleep(5)

print(cfunction.get_page_title())

cfunction.click_on_inputs_send_keys(g_objects.username_xpath,f_creds['username'])
cfunction.click_on_inputs_send_keys(g_objects.password_xpath,f_creds['password'])
cfunction.click_on_element(g_objects.login_btn_xpath)