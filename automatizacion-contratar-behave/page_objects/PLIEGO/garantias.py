from page_objects.base_page import BasePage
from page_objects.PLIEGO.properties.garantias_locators import GarantiasLocators
import page_objects.PLIEGO.indice_proceso as indice_proceso
from config.parameters import Parameters
from time import *


class Garantias(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.pliego = Parameters.get_pliego()

    def garantias_pco(self):
        self.wait_until_element_clickable(GarantiasLocators.PORCENTAJE_GARANTIA).send_keys(self.pliego['garantiadecumplimientodecontrato'])
        self.find_element(GarantiasLocators.GUARDAR_Y_VOLVER).click()
        sleep(3)
        return indice_proceso.CompletarIndicesProceso(self.driver)
