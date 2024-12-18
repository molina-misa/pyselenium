import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones.Funciones import Funciones

class PageLogin:

    def __init__(self, driver):
        self.driver = driver

    def login_master(self, url, name, password, t):
        driver = self.driver
        f = Funciones(driver)
        f.navegar(url, t)
        f.text_mix_validate("xpath","//input[contains(@id,'user-name')]", name , t)
        f.text_mix_validate("xpath","//input[contains(@id,'password')]", password, t)
        f.click_mix_validate("id","login-button", t)
        f.salida()