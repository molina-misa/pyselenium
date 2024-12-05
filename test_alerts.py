import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

'''
¿Qué son los dialogs, modals o alerts?
A las ventanas emergentes yo siempre las he llamado Modals 
porque es el nombre con el que primero las conocí. 
Sin embargo es cierto que gente más mayor que yo y los desarrolladores de Android
les suelen llamar Dialogs que es como se les nombra en Material 
y quienes trabajan diseñando o programando para los sistemas de Apple 
suelen estar influidos por el nombre de las Human Interface Guidelines, 
así que las llaman Alerts.
'''
driver = webdriver.Chrome()

t = 3

driver.get("https://webdriveruniversity.com/Popup-Alerts/index.html")
driver.maximize_window()
time.sleep(t)

#driver.switch_to_alert().accept()
#time.sleep(t)

#driver.switch_to_alert().dismiss()
#time.sleep(4)

#driver.find_element(By.XPATH,"//button[@type='button'][contains(.,'Close')]").click()
driver.find_element(By.XPATH,"//span[contains(@id,'button2')]").click()
time.sleep(t)
try:
    Buscar = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button'][contains(.,'Close')]")))
    Buscar = driver.find_element(By.XPATH,"//button[@type='button'][contains(.,'Close')]").click()
    time.sleep(2)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

time.sleep(t)
driver.close()