import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome()

t = 3

driver.get("https://pixabay.com/es/")
driver.maximize_window()
time.sleep(t)


try:
    search = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='label--Ngqjq'][contains(.,'Descubre más')]")))
    search = driver.find_element(By.XPATH, "//span[@class='label--Ngqjq'][contains(.,'Descubre más')]")
    go = driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", search)
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponbile")



time.sleep(t)
driver.close()