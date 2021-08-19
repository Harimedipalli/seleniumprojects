
from PageActions.Commonfunction import CommonFunctions
from PageObjects.double_click_objectloators import Double
from selenium.webdriver.common.by import By




import yaml
import time


with open(r'/home/srikanth/Desktop/selenium_project/pythonProject/Tests/TestData/doubleclick_creds.yaml', 'r') as file:
    f_creds = yaml.load(file)



cfunction = CommonFunctions()
d_objects = Double()


driver=cfunction.open_url('https://testautomationpractice.blogspot.com/?m=1')
cfunction.maximize_browser()
time.sleep(2)
print(cfunction.get_page_title())

cfunction.clear_on_element(d_objects.field_text_xpath)
cfunction.click_on_inputs_send_keys(d_objects.field_text_xpath, f_creds["feild1"])
copytextbox = cfunction.browser.find_element(By.XPATH, d_objects.copy_btn_xpath)
cfunction.double_click(copytextbox)