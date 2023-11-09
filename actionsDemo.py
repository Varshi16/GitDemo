import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
#action.click_and_hold()
#action.double_click()
#action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#performs right click
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
time.sleep(2)
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()

