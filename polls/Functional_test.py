from selenium.webdriver.common.by import By

__author__ = 'Max'

from unittest import TestCase
from selenium import webdriver


class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()
        self.browser.implicitly_wait(3)

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Max')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Cruz')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrolador Web']").click()

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3192829171')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('mr.cruz@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('/Users/max/Downloads/profile.png')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('max_test')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()

        self.browser.implicitly_wait(3)
        span=self.browser.find_element(By.XPATH, '//span[text()="Max Cruz"]')

        self.assertIn('Max Cruz', span.text)


    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span=self.browser.find_element(By.XPATH, '//span[text()="Max Cruz"]')
        span.click()

        h2=self.browser.find_element(By.XPATH, '//h2[text()="Max Cruz"]')

        self.assertIn('Max Cruz', h2.text)