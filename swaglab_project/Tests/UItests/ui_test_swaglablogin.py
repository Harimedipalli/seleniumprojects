

from pageactions.CommonFunction import CommonFunctions
from pageobjects.Swaglab_objectlocators import SwaglabLogin
import yaml
import time

with open(r'/home/srikanth/Desktop/selenium_project/swaglab_project/Tests/TestData/f_creds.yaml', 'r') as file:
    f_creds = yaml.load(file)


cfunction = CommonFunctions()
g_objects = SwaglabLogin()

cfunction.open_url('https://www.saucedemo.com/')
cfunction.maximize_browser()
time.sleep(2)

print(cfunction.get_page_title())
cfunction.click_on_inputs_send_keys(g_objects.username_xpath, f_creds['username'])
cfunction.click_on_inputs_send_keys(g_objects.password_xpath, f_creds['password'])
cfunction.click_on_element(g_objects.login_xpath)
time.sleep(3)
print("Login Succesfull")
cfunction.click_on_element(g_objects.backpack_xpath)
cfunction.click_on_element(g_objects.bikelight_xpath)
cfunction.click_on_element(g_objects.bolttshirt_xpath)
cfunction.click_on_element(g_objects.jacket_xpath)
cfunction.click_on_element(g_objects.onesie_xpath)
cfunction.click_on_element(g_objects.redtshort_xpath)
print("Items selected")
time.sleep(3)
cfunction.click_on_element(g_objects.cart_xpath)
time.sleep(3)
print("Cart opened")
cfunction.click_on_element(g_objects.checkout_xpath)
time.sleep(3)
cfunction.click_on_inputs_send_keys(g_objects.firstname_xpath, f_creds["firstname"])
cfunction.click_on_inputs_send_keys(g_objects.lastname_xpath, f_creds["lastname"])
cfunction.click_on_inputs_send_keys(g_objects.zipcode_xpath, f_creds["zipcode"])
time.sleep(2)
print("Delivery details entered")
cfunction.click_on_element(g_objects.continue_xpath)
cfunction.click_on_element(g_objects.finish_xpath)
print("Shopping done")
time.sleep(2)
cfunction.click_on_element(g_objects.menu_xpath)
cfunction.click_on_element(g_objects.logout_xpath)
print("Logout succesfull")
