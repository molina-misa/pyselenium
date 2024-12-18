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
from Funciones.Page_Login import Page_Login


class BaseTest (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Firefox()
        time.sleep(2)

    def test1(self):
        driver = self.driver
        f = Funciones(driver)
        f.navegar("https://demoqa.com/text-box",0.3)
        f.text_mix_validate("id", "userName", "Agustina", 0.3)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()

