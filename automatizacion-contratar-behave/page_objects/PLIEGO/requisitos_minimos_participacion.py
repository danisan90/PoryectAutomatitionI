from page_objects.base_page import BasePage
from page_objects.PLIEGO.properties.requisitos_minimos_partic_locators import RequisitosMinimosParticipacionLocator
import page_objects.PLIEGO.indice_proceso as indice_proceso
from config.parameters import Parameters
from time import *

class RequisitosMinimosParticipacion(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.pliego = Parameters.get_pliego()

    def requisitos_participacion(self):
        self.find_element(RequisitosMinimosParticipacionLocator.REQUISITOS_ECONOMICOS_Y_FINANCIEROS).send_keys(self.pliego['requisitoseconomicos'])
        self.find_element(RequisitosMinimosParticipacionLocator.REQUISITO_TECNICOS).send_keys(self.pliego['requisitostecnicos'])
        self.find_element(RequisitosMinimosParticipacionLocator.REQUISITOS_ADMINISTRATIVOS).send_keys(self.pliego['requisitosadministrativos'])
        self.find_element(RequisitosMinimosParticipacionLocator.GUARDAR_Y_VOLVER).click()
        sleep(3)
        return indice_proceso.CompletarIndicesProceso(self.driver)
