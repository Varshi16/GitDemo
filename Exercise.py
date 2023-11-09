import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
expectedlist = ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actuallist = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
products = driver.find_elements(By.XPATH,"//div[@class='product']")
for product in products:
    actuallist.append(product.find_element(By.XPATH, "h4").text)
    product.find_element(By.XPATH,"div/button").click()
assert expectedlist == actuallist
driver.find_element(By.CLASS_NAME,"cart-icon").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()
time.sleep(10)
discountedamount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
totalamt = float(driver.find_element(By.CLASS_NAME,"totAmt").text)
assert totalamt > discountedamount
