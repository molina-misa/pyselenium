import time
import unittest
from Funciones_ex import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones.Funciones import Funciones
from Funciones.Page_Login import Page_Login

tg = 0.1
class BaseTest (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Firefox()

    def test1(self):
        driver = self.driver
        f = Funciones(driver)
        fe = ExcelFunction(driver)
        f.navegar("https://demoqa.com/text-box",tg)
        ruta = "C://Users//amane//PycharmProjects//curso-selenium//pyselenium//Excel//Datos_ok.xlsx"
        filas = fe.getRowCount(ruta,"Hoja 1")

        for r in range(2,filas+1):
            nombre = fe.readData(ruta,"Hoja 1",r,1)
            email = fe.readData(ruta, "Hoja 1", r, 2)
            dir1 = fe.readData(ruta, "Hoja 1", r, 3)
            dir2 = fe.readData(ruta, "Hoja 1", r, 4)

            f.text_mix_validate("id","userName",nombre,tg)
            f.text_mix_validate("id", "userEmail", email, tg)
            f.text_mix_validate("id", "currentAddress", dir1, tg)
            f.text_mix_validate("id", "permanentAddress", dir2, tg)
            f.click_mix_validate("id", "submit", tg)

            e = f.exists("id","name",tg)
            if e == "Existe":
                print("El elemento se inserto correctamente")
                fe.writeData(ruta,"Hoja 1",r,5,"Insertado")
            else:
                print("No se inserto")
                fe.writeData(ruta,"Hoja 1",r,5,"Error")



    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()