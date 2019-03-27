from page_objects.base_page import BasePage
import page_objects.SGA.completar_solicitud_gasto as completar_solicitud_gasto
from page_objects.SGA.properties.completar_imputacion_locator import CompletarImputacionLocators
from config.parameters import Parameters

from time import *


class CompletarImputacionSco(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.sco = Parameters.get_sco()

    def completar_imputaciones(self):
        for indice in range(0, len(self.find_elements(CompletarImputacionLocators.OBJETOS_DE_GASTO))):
            sleep(3)
            self.wait_until_element_clickable(
                CompletarImputacionLocators.OBJETO_PARTIDAS)
            self.find_select(CompletarImputacionLocators.OBJETO_PARTIDAS).select_by_visible_text(
                self.find_elements(CompletarImputacionLocators.OBJETOS_DE_GASTO)[indice].text)
            self.find_element(CompletarImputacionLocators.BUSCAR_PARTIDAS).click()
            self.wait_until_element_clickable(CompletarImputacionLocators.COMPLETAR_MONTO).send_keys\
                (self.find_elements(CompletarImputacionLocators.COLUMNA_TOTAL)[indice].text)
            self.find_element(CompletarImputacionLocators.CHECKBOX_PARTIDA).click()
            sleep(2)
            self.find_element(CompletarImputacionLocators.INGRESAR_IMPUTACION).click()
            sleep(2)
        self.find_element(CompletarImputacionLocators.GUARDAR_Y_VOLVER).click()
        return completar_solicitud_gasto.CompletarSolicitudGasto(self.driver)
