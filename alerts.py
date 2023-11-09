import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
name="Varshitha"
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
#whenever we see java or javascript pop up boxes/browser based alerts we switch to alert
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
#clicks ok or positive mesage in pop up message
alert.accept()
#clicks cancel or negative message in pop up message
#alert.dismiss()