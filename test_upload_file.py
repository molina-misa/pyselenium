import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome()

t = 3

driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()
time.sleep(t)

try:
    search = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'file-upload')]")))
    search = driver.find_element(By.XPATH, "//input[contains(@id,'file-upload')]")
    search.send_keys("C://Users//amane//PycharmProjects//curso-selenium//pyselenium//imagen//imagen-demo.jpg")
    driver.find_element(By.XPATH, "//input[contains(@id,'file-submit')]").click()
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponbile")

time.sleep(t)
driver.close()