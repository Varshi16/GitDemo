import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chrome_Options = webdriver.ChromeOptions()
chrome_Options.add_argument("--start-maximized")
chrome_Options.add_argument("headless")
chrome_Options.add_argument("--ignore-certificate-errors")
service_obj = Service()
driver = webdriver.Chrome(service=service_obj,options=chrome_Options)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)