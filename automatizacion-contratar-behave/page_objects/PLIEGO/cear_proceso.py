from page_objects.base_page import BasePage
from config.parameters import Parameters
from page_objects.PLIEGO.indice_proceso import CompletarIndicesProceso
from page_objects.PLIEGO.properties.crear_proceso_locators import CrearProcesoLocators
from time import *

class CrearProcesoDeContratacion(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.pliego = Parameters.get_pliego()

    def crear_pc(self):
        self.wait_until_element_clickable(CrearProcesoLocators.NOMBRE_PROCESO_CONTRATACION).send_keys(self.pliego['NOMBREOBRA'])
        self.find_element(CrearProcesoLocators.LICITACION_PUBLICA).click()
        self.wait_until_element_clickable(CrearProcesoLocators.TIPO_CONTRATACION).click()
        self.find_element(CrearProcesoLocators.TIPO_CONTRATACION_OBRA).click()
        self.wait_until_element_clickable(CrearProcesoLocators.ENCUADRE_LEGAL).click()
        self.find_element(CrearProcesoLocators.BUTTON_AGREGAR_ENCUADRE).click()
        sleep(4)
        self.find_element(CrearProcesoLocators.SIGUIENTE_PASO)
        self.find_element(CrearProcesoLocators.SIGUIENTE_PASO).click()
        sleep(4)
        return CompletarIndicesProceso(self.driver)

