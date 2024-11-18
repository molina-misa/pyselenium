import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

t = 2

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

driver.get("https://www.selenium.dev/documentation/webdriver/elements/")
time.sleep(t)

driver.get("https://www.grepper.com/search.php?q=selenium%t0documentation%t0python")
time.sleep(t)

driver.back()
time.sleep(t)

driver.back()
time.sleep(t)

driver.execute_script("window.history.go(2)")
time.sleep(t)

driver.close()

#otra opcion para volver atrás con un script de javascript
#driver.execute_script("window.history.go(-1)")