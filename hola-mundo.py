from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.webdriver import WebDriver

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
print("Bienvenido a Selenium")
print(driver.title)
