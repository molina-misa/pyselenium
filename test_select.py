import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome()

t = 2

driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()
time.sleep(t)

try:
    optionSelect = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//select[contains(@id,'dropdown')]"))
    )
    option = Select(optionSelect)
    option.select_by_visible_text("Option 1")
    time.sleep(t)
    option.select_by_index(2)
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponbile")

