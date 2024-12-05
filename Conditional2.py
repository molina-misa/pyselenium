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

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

btn = driver.find_element(By.XPATH,"//button[contains(@id,'submit')]")
print(btn.is_enabled())
if btn.is_enabled():
    print("Puedes dar clic")
else:
    print("No puedes dar clic")
driver.close()
