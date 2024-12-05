import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome()

t = 3

driver.get("http://makeseleniumeasy.com/home/seleniumbytopic/")
driver.maximize_window()
time.sleep(t)

#Obteniendo todos los links de la página
links = driver.find_elements(By.TAG_NAME,"a")

print("El numero de Links que hay en la página son",len(links))


# Find the "API Testing" link and perform hover action
api_testing_link = driver.find_element(By.LINK_TEXT, "API Testing")
hover = ActionChains(driver).move_to_element(api_testing_link)  # Create hover action
hover.perform()  # Execute the hover action
driver.find_element(By.LINK_TEXT,"Kick Start API Testing").click()
time.sleep(t)
driver.quit()