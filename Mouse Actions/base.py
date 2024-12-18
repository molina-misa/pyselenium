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
from selenium.webdriver import ActionChains


tg = 1
class BaseTest (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Firefox()

    def test1(self):
        driver = self.driver
        f = Funciones(driver)
        f.navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", tg)
        f.text_mix_validate("xpath","//input[contains(@name,'username')]","Admin",tg)
        f.text_mix_validate("xpath","//input[contains(@type,'password')]","admin123",tg)
        f.click_mix_validate("xpath","//button[contains(@type,'submit')]", 5)


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
