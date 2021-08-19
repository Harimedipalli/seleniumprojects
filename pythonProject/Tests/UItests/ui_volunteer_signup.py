

from PageActions.Commonfunction import CommonFunctions
from PageObjects.volunteer_signup_objectlocators import Signup
from selenium.webdriver.common.by import By

import yaml
import time


with open(r'/home/srikanth/Desktop/selenium_project/pythonProject/Tests/TestData/signup_creds.yaml', 'r') as file:
    f_creds = yaml.load(file)


cfunction = CommonFunctions()
g_objects = Signup()

driver=cfunction.open_url('https://testautomationpractice.blogspot.com/?m=1')
cfunction.maximize_browser()
time.sleep(2)

print(cfunction.get_page_title())
time.sleep(2)
print("enter the name")

cfunction.switch_to_frame(g_objects.frame_text_xpath)
print("helo")
time.sleep(2)


cfunction.click_on_inputs_send_keys(g_objects.fname_txt_xpath, f_creds["firstname"])
print("done")
cfunction.click_on_inputs_send_keys(g_objects.lname_text_xpath, f_creds["lasttname"])
print("lastname")
cfunction.click_on_inputs_send_keys(g_objects.phoneno_xpath, f_creds["phoneno"])
print("phone")
cfunction.click_on_inputs_send_keys(g_objects.country_xpath, f_creds["country"])
print("country")
cfunction.click_on_inputs_send_keys(g_objects.city_xpath, f_creds["city"])
print("city")
cfunction.click_on_inputs_send_keys(g_objects.email_xpath, f_creds["mail"])
print("mail")


cfunction.click_on_element(g_objects.gender_xpath)
print("gender")
cfunction.click_on_element(g_objects.tues_xpath)
cfunction.click_on_element(g_objects.thus_xpath)


cfunction.click_on_element(g_objects.timetocontact_xpath)


