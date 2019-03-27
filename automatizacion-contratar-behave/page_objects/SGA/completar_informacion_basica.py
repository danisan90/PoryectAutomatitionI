from page_objects.base_page import BasePage
from page_objects.SGA.properties.completar_informacion_basica_locator import CompletarInformacionBasicaLocators
import page_objects.SGA.completar_solicitud_gasto as completar_solicitud_gasto
from config.parameters import Parameters
from time import *


class CompletarInformacionBasica(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.sco = Parameters.get_sco()

    def completar_informacion_basica(self):
        self.find_element(CompletarInformacionBasicaLocators.UNIDAD_SOLICITANTE_INPUT).send_keys(self.sco['UNIDAD_SOLICITANTE'])

        self.wait_until_element_clickable(CompletarInformacionBasicaLocators.ACEPTA_ANTICIPO_FINANCIERO_RADIO)
        af_radio_btn = self.find_element(CompletarInformacionBasicaLocators.ACEPTA_ANTICIPO_FINANCIERO_RADIO)
        af_radio_btn.click()
        sleep(3)

        af_input = self.find_element(CompletarInformacionBasicaLocators.PORCENTAJE_AF)
        af_input.click()
        af_input.send_keys(self.sco['PORCENTAJE_AF'])

        self.find_element(CompletarInformacionBasicaLocators.ANEXO_SCO_INPUT).send_keys(self.sco['RUTA_ANEXO'])
        self.find_element(CompletarInformacionBasicaLocators.ANEXO_SCO_BTN).click()
        self.find_element(CompletarInformacionBasicaLocators.GUARDAR_VOLVER_BTN).click()

        return completar_solicitud_gasto.CompletarSolicitudGasto(self.driver)
