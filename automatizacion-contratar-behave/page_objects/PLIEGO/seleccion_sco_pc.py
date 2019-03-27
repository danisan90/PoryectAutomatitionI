from page_objects.base_page import BasePage
from page_objects.PLIEGO.properties.seleccion_sco_pc_locators import SeleccionSCOLocators
import page_objects.PLIEGO.indice_proceso as indice_proceso
from config.parameters import Parameters
from generated_data.data_manager import DataManager
from time import *

class SeleccionSolicitudGastoPliego(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.sco = Parameters.get_sco()

    def solicitudes_de_contratacion(self):
        self.find_element(SeleccionSCOLocators.NUMERO_SCO).send_keys(DataManager.get_numero_sco())
        self.find_element(SeleccionSCOLocators.BUTTON_AGREGAR).click()

        self.wait_for_element(SeleccionSCOLocators.NUMERO_SCO_INGRESADO)
        self.find_element(SeleccionSCOLocators.GUARDAR_Y_VOLVER).click()
        sleep(4)
        return indice_proceso.CompletarIndicesProceso(self.driver)

