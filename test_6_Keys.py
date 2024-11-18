import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()



nom =driver.find_element(By.XPATH,"//input[@type='text' and @id='userName']")
nom.send_keys("Rodrido")
nom.send_keys(Keys.TAB + "rodirgo@mail.com" + Keys.TAB + "Dirección 1" + Keys.TAB + "Dirección 2" + Keys.TAB + Keys.ENTER)
time.sleep(2)

driver.execute_script("window.scrollTo(0, 500);")
time.sleep(2)

driver.find_element(By.XPATH,"//li[@class='btn btn-light '][contains(.,'Check Box')]").click()
time.sleep(2)
driver.close()
