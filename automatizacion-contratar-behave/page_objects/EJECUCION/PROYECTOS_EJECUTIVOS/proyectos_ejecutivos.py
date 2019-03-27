from page_objects.base_page import BasePage
from page_objects.EJECUCION.properties.proyecto_ejecutivo_locator import ProyectoDeObraLocators
from page_objects.EJECUCION.PROYECTOS_EJECUTIVOS.itemizado import Itemizado
from config.parameters import Parameters
from time import *


class ProyectoEjecutivo(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.proyectoEjecutivo = Parameters.get_proyectoEjecutivo()

    def copiar_proyecto_obra(self, nombre_po):
        self.wait_for_element(ProyectoDeObraLocators.COPIAR_PROYECTO).click()
        sleep(3)
        self.wait_for_element_visibility(ProyectoDeObraLocators.INPUT_NOMBRE_PROYECTO).clear()
        self.wait_for_element_visibility(ProyectoDeObraLocators.INPUT_NOMBRE_PROYECTO)
        self.find_element(ProyectoDeObraLocators.INPUT_NOMBRE_PROYECTO).send_keys(nombre_po)
        sleep(2)
        self.find_element(ProyectoDeObraLocators.CLICK_AUXILIAR).click()
        self.find_element(ProyectoDeObraLocators.COPIAR_BUTTON).click()
        sleep(10)
        self.wait_until_element_clickable(ProyectoDeObraLocators.editar_button(nombre_po)).click()
        self.wait_for_element(ProyectoDeObraLocators.PAG_PROYECTO_OBRA).click()
        sleep(3)
        return self

    def nuevo_proyecto(self):
        self.wait_until_element_clickable(ProyectoDeObraLocators.NUEVO_PROYECTO).click()
        sleep(1)
        self.wait_for_element(ProyectoDeObraLocators.INGRESAR_NOMBRE_NUEVO_PROYECTO).send_keys(self.proyectoEjecutivo['NOMBREPROYECTOEJECUTIVO'])
        self.wait_for_element(ProyectoDeObraLocators.GUARDAR_NP).click()
        sleep(2)
        return Itemizado(self.driver)


