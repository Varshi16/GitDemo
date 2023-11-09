import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element(By.XPATH,"//a[contains(@href,'shop')]").click()
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()  #-- using regular expression in href for css
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in products:
    productname = product.find_element(By.XPATH,"div/h4/a").text
    if productname == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()
        break
driver.find_element(By.CSS_SELECTOR,".nav-link.btn.btn-primary").click()
driver.find_element(By.CSS_SELECTOR,".btn.btn-success").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
driver.find_element(By.CLASS_NAME,"btn.btn-success.btn-lg").click()
successText = driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible").text
assert "Success! Thank you!" in successText
driver.close()
