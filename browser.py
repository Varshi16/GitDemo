from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#--invoking chrome browser--
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
#--invoking firefox browser--
#service_obj = Service()
#driver = webdriver.Firefox(service=service_obj)
#--microsoft edge browser--
#service_obj = Service()
#driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()