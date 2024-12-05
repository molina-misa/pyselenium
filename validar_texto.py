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

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

btn = driver.find_element(By.XPATH, "//button[contains(@id,'submit')]")
go = driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
btn.click()
time.sleep(t)

driver.close()
