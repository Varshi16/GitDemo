import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
windowsopened = driver.window_handles
driver.switch_to.window(windowsopened[1])
username = driver.find_element(By.CSS_SELECTOR,"a[href='mailto:mentor@rahulshettyacademy.com']").text
driver.switch_to.window(windowsopened[0])
driver.find_element(By.ID,"username").send_keys(username)
driver.find_element(By.ID,"password").send_keys("12345")
driver.find_element(By.ID,"signInBtn").click()
time.sleep(2)
print(driver.find_element(By.CSS_SELECTOR,".alert.alert-danger.col-md-12").text)
