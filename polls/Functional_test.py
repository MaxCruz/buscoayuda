# coding=utf-8
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

    def test_loginIndependiente(self):
        self.browser.get('http://localhost:8000')

        link = self.browser.find_element_by_id('id_login')
        link.click()
        self.browser.implicitly_wait(3)

        usuario = self.browser.find_element_by_id('usrname')
        usuario.send_keys('max_test')

        clave = self.browser.find_element_by_id('psw')
        clave.send_keys('clave123')

        ingresar = self.browser.find_element_by_id('id_ingresar')
        ingresar.click()
        self.browser.implicitly_wait(3)

        editarPerfil = self.browser.find_element_by_id('id_editar')
        self.assertIn('Editar', editarPerfil.text)

    def test_editIndependiente(self):
        self.browser.get('http://localhost:8000')

        link = self.browser.find_element_by_id('id_login')
        link.click()
        self.browser.implicitly_wait(3)

        usuario = self.browser.find_element_by_id('usrname')
        usuario.send_keys('max_test')

        clave = self.browser.find_element_by_id('psw')
        clave.send_keys('clave123')

        ingresar = self.browser.find_element_by_id('id_ingresar')
        ingresar.click()
        self.browser.implicitly_wait(3)

        editarPerfil = self.browser.find_element_by_id('id_editar')
        editarPerfil.click()
        self.browser.implicitly_wait(3)

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.clear()
        nombre.send_keys('Max Raul')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.clear()
        apellidos.send_keys('Cruz Rodriguez')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.clear()
        experiencia.send_keys('6')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Floristería']").click()

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.clear()
        telefono.send_keys('3192829172')

        correo = self.browser.find_element_by_id('id_correo')
        correo.clear()
        correo.send_keys('mr.cruz1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.clear()
        imagen.send_keys('/Users/max/Downloads/profile2.png')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)

        salir = self.browser.find_element_by_id('id_logout')
        salir.click()
        self.browser.implicitly_wait(3)

        span=self.browser.find_element(By.XPATH, '//span[text()="Max Raul Cruz Rodriguez"]')

        self.assertIn('Max Raul Cruz Rodriguez', span.text)

    def test_comentar(self):
        self.browser.get('http://localhost:8000')
        span=self.browser.find_element(By.XPATH, '//span[text()="Max Raul Cruz Rodriguez"]')
        span.click()

        correo = self.browser.find_element_by_id('correo')
        correo.send_keys('prueba@prueba.com')

        comentario = self.browser.find_element_by_id('comentario')
        comentario.send_keys('Comentario De Prueba')

        botonComentar = self.browser.find_element_by_id('id_comentar')
        botonComentar.click()
        self.browser.implicitly_wait(3)

        h4=self.browser.find_element(By.XPATH, '//h4[text()="prueba@prueba.com"]')

        self.assertIn('prueba@prueba.com', h4.text)

    def test_buscarIndependiente(self):
        self.browser.get('http://localhost:8000')

        buscar = self.browser.find_element_by_id('buscar')
        buscar.send_keys('Raul Rodriguez')

        span=self.browser.find_element(By.XPATH, '//span[text()="Max Raul Cruz Rodriguez"]')

        self.assertIn('Max Raul Cruz Rodriguez', span.text)