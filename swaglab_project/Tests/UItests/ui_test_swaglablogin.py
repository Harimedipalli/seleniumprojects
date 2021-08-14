


from pageactions.CommonFunction import CommonFunction
from pageobjects.Swaglab_objectlocators import SwaglabLogin
import time
import yaml

with open(r'/home/srikanth/Desktop/selenium_project/fb_login_poject/Tests/TestData/f_creds.yaml', 'r') as file:
    f_creds = yaml.load(file)


cfunction = CommonFunction()
g_objects = SwaglabLogin()

cfunction.open_url('https://www.saucedemo.com/')
cfunction.maximize_browser()
time.sleep(2)

