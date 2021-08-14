from selenium import webdriver
import time

browser = webdriver.Chrome('//chromedriver')

browser.get('https://www.instagram.com/accounts/login/')
print(browser.title)
try:
    assert "Instagram" == browser.title
except AssertionError:
    print(f'page tite is nt matched with expedted title,Actuval title {browser.title}But the expected title {"Instagram"}  ')

browser.maximize_window()
time.sleep(5)
browser.minimize_window()
time.sleep(5)
browser.close()
