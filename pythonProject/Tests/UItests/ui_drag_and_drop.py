from PageActions.Commonfunction import CommonFunctions
from PageObjects.drag_and_drop_objectslocators import Drag_drop, Image_drag_drop, Slide, Resize
from selenium.webdriver.common.by import By
import time
import yaml

with open(r'/home/srikanth/Desktop/selenium_project/pythonProject/Tests/TestData/doubleclick_creds.yaml', 'r') as file:
    f_creds = yaml.load(file)

cfunction = CommonFunctions()
drag_drop_object = Drag_drop()
image_drag_drop_object = Image_drag_drop()
slide_object = Slide()
resize_object = Resize()

driver = cfunction.open_url('https://testautomationpractice.blogspot.com/?m=1')
cfunction.maximize_browser()
time.sleep(2)
print(cfunction.get_page_title())

drag_point = cfunction.browser.find_element(By.XPATH, drag_drop_object.source_xpath)
drop_point = cfunction.browser.find_element(By.XPATH, drag_drop_object.destination_xpath)
cfunction.click_hold_move(drag_point, drop_point)
time.sleep(3)
print("drag and drop done succesfully")
drag_image1 = cfunction.browser.find_element(By.XPATH, image_drag_drop_object.firstimage_xpath)
drop_image1 = cfunction.browser.find_element(By.XPATH, image_drag_drop_object.destination_xpath)
cfunction.click_hold_move(drag_image1, drop_image1)
time.sleep(3)
print("Mr john sent to trash")
drag_image2 = cfunction.browser.find_element(By.XPATH, image_drag_drop_object.secondimage_xpath)
drop_image2 = cfunction.browser.find_element(By.XPATH, image_drag_drop_object.destination2_xpath)
cfunction.click_hold_move(drag_image2, drop_image2)
print("Mary sent to trash")

slide_left = cfunction.browser.find_element(By.XPATH, slide_object.start_xpath)
cfunction.slider_element(slide_left, 120,0)
print("sliding done")
time.sleep(5)

resize_element = cfunction.browser.find_element(By.XPATH, Resize.size_xpath)
cfunction.scroll_down()
cfunction.scroll_down()
cfunction.move_element(resize_element, 50, 5)
print("resize done")
