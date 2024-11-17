import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

driver.execute_script("window.scrollTo(0,500)")

driver.find_element(By.XPATH,"//input[contains(@id,'userName')]").send_keys("Rodrigo")
driver.find_element(By.XPATH,"//input[contains(@id,'userEmail')]").send_keys("nombre123@gmail.com")
driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys("Dirección 1")
driver.find_element(By.XPATH, "//textarea[contains(@id,'permanentAddress')]").send_keys("Dirección 2")
driver.find_element(By.XPATH, "//button[contains(@id,'submit')]").click()

time.sleep(2)
driver.close()