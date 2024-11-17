import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()



driver.find_element(By.XPATH,"//input[@type='text' and @id='userName']").send_keys("Rodrigo")
time.sleep(2)
driver.find_element(By.ID,"userEmail").send_keys("nombre123@gmail.com")
time.sleep(2)
driver.find_element(By.ID,"currentAddress").send_keys("Dirección 1")
time.sleep(2)
driver.find_element(By.ID,"permanentAddress").send_keys("Dirección 2")
time.sleep(2)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)
driver.find_element(By.ID,"submit").click()

time.sleep(2)
driver.close()
