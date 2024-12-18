import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(10)
t = 3

time.sleep(t)

driver.close()