from page_objects.base_page import BasePage
import page_objects.SGA.completar_solicitud_gasto as completar_solicitud_gasto
from page_objects.SGA.properties.buscar_solicitud_contratacion_locator import BuscarSolicitudContratacionLocators
from config.parameters import Parameters
from generated_data.data_manager import DataManager
from page_objects.MENU import menu
from time import *


class BuscarSolicitudContratacionPageObject(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.sco = Parameters.get_sco()
        self.menu = menu.MenuPageObject(self.driver)


    def buscar_solicitud_por_numero(self):
        self.find_element(BuscarSolicitudContratacionLocators.INPUT_NUMERO).send_keys(DataManager.get_numero_sco())
        self.find_element(BuscarSolicitudContratacionLocators.BUSCAR_BUTTON).click()
        return self

    def editar_sco(self):
        sleep(3)
        self.wait_until_element_clickable(BuscarSolicitudContratacionLocators.AGARRAR_SOLICITUD).click()

        return completar_solicitud_gasto.CompletarSolicitudGasto(self.driver)

    def autorizar_sco(self):
        sleep(4)
        self.wait_until_element_clickable(BuscarSolicitudContratacionLocators.AUTORIZAR_RECHAZAR_SOLICITUD).click()
        sleep(5)
        self.wait_until_element_clickable(BuscarSolicitudContratacionLocators.AUTORIZAR_SCO).click()
        sleep(5)
        return self

    def rechazar_sco(self):
        self.wait_until_element_clickable(BuscarSolicitudContratacionLocators.AUTORIZAR_RECHAZAR_SOLICITUD).click()
        self.wait_until_element_clickable(BuscarSolicitudContratacionLocators.RECHAZAR_SCO).click()
        return self

    def get_estado(self):
        return self.wait_for_element_visibility(BuscarSolicitudContratacionLocators.ESTADO_SG_LBL).text
