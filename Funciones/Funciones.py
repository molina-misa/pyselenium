import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class Funciones:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def tiempo(tiempo):
        return time.sleep(tiempo)

    def navegar(self, url, t):
        self.driver.get(url)
        self.driver.maximize_window()
        print("Pagina abierta: " + str(url))
        return time.sleep(t)

    def selector_xpath(self, elemento):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val = self.driver.find_element(By.XPATH, elemento)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", val)
        return val

    def selector_id(self, elemento):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, elemento)))
        val = self.driver.find_element(By.ID, elemento)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", val)
        return val

    def text_mix_validate(self, tipo , selector, text, t):
        if tipo == "xpath":
            try:
                val = self.selector_xpath(selector)
                val.clear()
                val.send_keys(text)
                print("Escribiendo en el campo {} el texto {}".format(selector, text))
                return time.sleep(t)
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
        elif tipo == "id":
            try:
                val = self.selector_id(selector)
                val.clear()
                val.send_keys(text)
                print("Escribiendo en el campo {} el texto {}".format(selector, text))
                return time.sleep(t)
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)

    def click_mix_validate(self, tipo, selector , t):
        if tipo == "xpath":
            try:
                val = self.selector_xpath(selector)
                val.click()
                print("Hemos dado click en el campo {}".format(selector))
                return time.sleep(t)
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return time.sleep(t)
        elif tipo == "id":
            try:
                val = self.selector_id(selector)
                val.click()
                print("Hemos dado click en el campo {}".format(selector))
                return time.sleep(t)
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return time.sleep(t)

    def select_xpath_text(self, xpath, text, t):
        try:
            val = self.selector_xpath(xpath)
            val = Select(val)
            val.select_by_visible_text(text)
            print("El campo seleccionado es {}".format(text))
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + xpath)
            return time.sleep(t)

    #busca y elige selectores por el XPATH
    def select_xpath_type(self, xpath, tipo , data,  t):
        try:
            val = self.selector_xpath(xpath)
            val = Select(val)
            if tipo == "text":
                val.select_by_visible_text(data)
            elif tipo == "index":
                val.select_by_index(data)
            elif tipo == "value":
                val.select_by_value(data)
            print("El campo seleccionado es {}".format(data))
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + xpath)
            return time.sleep(t)

    #busca y elige selectores por el ID
    def select_id_type(self, ide , data,  t):
        try:
            val = self.selector_id(ide)
            val = Select(val)
            if type == "text":
                val.select_by_visible_text(data)
            elif type == "index":
                val.select_by_index(data)
            elif type == "value":
                val.select_by_value(data)
            print("El campo seleccionado es {}".format(data))
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + ide)
            return time.sleep(t)


    def upload_xpath(self, xpath, ruta, t):
        try:
            val = self.selector_xpath(xpath)
            val.send_keys(ruta)
            print("Se ha cargado la imagen {}".format(ruta))
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + xpath)
            return time.sleep(t)

    def upload_id(self, ide, ruta, t):
        try:
            val = self.selector_id(ide)
            val.send_keys(ruta)
            print("Se ha cargado la imagen {}".format(ruta))
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + ide)
            return time.sleep(t)

    def check_xpath(self, xpath, t):
        try:
            val = self.selector_xpath(xpath)
            val.click()
            print("Se ha cargado la imagen {}".format(xpath))
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + xpath)
            return time.sleep(t)

    def check_id(self, ide, t):
        try:
            val = self.selector_id(ide)
            val.click()
            print("Se ha cargado la imagen {}".format(ide))
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + ide)
            return time.sleep(t)

    def exists(self, tipo, selector, t ):
        if tipo == "xpath":
            try:
                val = self.selector_xpath(selector)
                print("El elemento {} -> existe".format(selector))
                time.sleep(t)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento " + selector)
                return "No existe"
        elif tipo == "id":
            try:
                val = self.selector_id(selector)
                print("El elemento {} -> existe".format(selector))
                time.sleep(t)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento " + selector)
                return "No existe"


    def salida(self):
        print("Se terminó la prueba exitosamente")