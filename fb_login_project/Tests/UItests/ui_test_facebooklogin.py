import os

from PageActions.Commonfunctions import CommonFunctions
from PageObjects.Facebook_objectlocators import FacebookLogin
import time
import yaml

with open('/home/srikanth/Desktop/selenium_project/fb_login_project/Tests/TestData/f_creds.yaml', 'r') as file:
    f_creds = yaml.load(file)

cfunction = CommonFunctions()
g_objects = FacebookLogin()

cfunction.open_url('https://www.facebook.com/')
cfunction.maximize_browser()
time.sleep(2)



print(cfunction.get_page_title())

cfunction.click_on_inputs_send_keys(g_objects.username_xpath, f_creds['username'])
cfunction.click_on_inputs_send_keys(g_objects.password_xpath, f_creds['password'])
cfunction.click_on_element(g_objects.login_btn_xpath)
cfunction.click_on_element(g_objects.account_btn_xpath)
time.sleep(2)
print("account opened")
cfunction.click_on_element(g_objects.pro_btn_xpath)
print("profile opened")
cfunction.click_on_element(g_objects.post_xpath)
print("post page opened")
cfunction.click_on_inputs_send_keys(g_objects.postarea_xpath, f_creds['postarea'])
print("postarea filled")
cfunction.click_on_element(g_objects.postdone_xpath)
cfunction.click_on_element(g_objects.edit_xpath)
print("edit page open")
time.sleep(2)
cfunction.click_on_element(g_objects.editbio_xpath)
print("edit Bio")
time.sleep(2)
cfunction.click_on_inputs_send_keys(g_objects.biotext_xpath, f_creds["Bio"])
print("passed text in Bio")
time.sleep(2)
cfunction.click_on_element(g_objects.savethebio_xpath)
print("Bio saved")
cfunction.click_on_element(g_objects.sharebio_xpath)
print("Bio shared succesfully")
cfunction.click_on_element(g_objects.return_account)
print("return to account")
cfunction.click_on_element(g_objects.logout_xpath)
print("log out succesfully")