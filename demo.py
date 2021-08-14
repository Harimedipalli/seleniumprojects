import time
#import os
from selenium import webdriver
#print(os.listdir(os.getcwd()))
browser = webdriver.Chrome('//chromedriver')

browser.get('https://www.youtube.com/')
print(browser.title)
try:
    assert "YouTube" == browser.title
except AssertionError:
    print(f"page title not matched with expected title,Actuval title{browser.title} But expected title is {'YouTube'}")
browser.maximize_window()
time.sleep(5)
browser.minimize_window()
time.sleep(5)
browser.maximize_window()
time.sleep(5)
browser.close()
