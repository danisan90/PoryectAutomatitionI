from page_objects.base_page import BasePage
from page_objects.PLIEGO.properties.informacion_contrato_locators import InformacionContratoLocators
import page_objects.PLIEGO.indice_proceso as indice_proceso
from config.parameters import Parameters
from time import *
class InformacionContrato(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.pliego = Parameters.get_pliego()
        self.sco = Parameters.get_sco()

    def monto_y_plazos_de_la_contratacion(self):
        self.wait_until_element_clickable(InformacionContratoLocators.CANTIDAD_DIAS).send_keys(self.pliego['cantidaddias'])
        for indice in range(0, len(self.sco['NOMBRE_FO'])):
            self.find_element(InformacionContratoLocators.duracion_de_la_obra(self.sco['NOMBRE_FO'][indice])).click()
            sleep(5)
            self.wait_until_element_clickable(InformacionContratoLocators.DIAS_DURACION_OBRA).send_keys(self.pliego['diasduracionobra'])
            self.find_select(InformacionContratoLocators.UNIDAD_DE_TIEMPO).select_by_visible_text(self.pliego['unidaddetiempo'])
            self.find_element(InformacionContratoLocators.GUARDAR).click()
            sleep(4)

        self.find_element(InformacionContratoLocators.GUARDAR_Y_VOLVER).click()
        sleep(4)
        return indice_proceso.CompletarIndicesProceso(self.driver)
