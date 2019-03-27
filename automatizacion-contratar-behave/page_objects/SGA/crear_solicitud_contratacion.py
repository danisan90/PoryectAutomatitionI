from page_objects.base_page import BasePage
from page_objects.SGA.properties.crear_sco_locators import CrearSolicitudContratacionLocators
from page_objects.SGA.completar_solicitud_gasto import CompletarSolicitudGasto
from config.parameters import Parameters
import time

DEFAULT_TIMEOUT = 10


class CrearSolicitudContratacion(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.sco = Parameters.get_sco()

    def crear_solicitud_contratacion(self):
        self.find_element(CrearSolicitudContratacionLocators.NOMBRE).send_keys(self.sco['NOMBRE'])
        self.find_element(CrearSolicitudContratacionLocators.OBJETO).send_keys(self.sco['OBJETO'])
        self.find_select(CrearSolicitudContratacionLocators.TIPO).select_by_value(self.sco['TIPO'])
        self.buscar_analista_por_username(self.sco['ANALISTA_USERNAME'])
        self.wait_until_element_clickable(CrearSolicitudContratacionLocators.SIGUIENTE, DEFAULT_TIMEOUT)
        time.sleep(5)
        link_siguiente = self.find_element(CrearSolicitudContratacionLocators.SIGUIENTE)
        link_siguiente.click()

        return CompletarSolicitudGasto(self.driver)

    def buscar_analista_por_username(self, username):
        abrir_modal_button = self.find_element(CrearSolicitudContratacionLocators.ABRIR_MODAL_BUTTON)
        abrir_modal_button.click()
        self.wait_until_element_clickable(CrearSolicitudContratacionLocators.ANALISTA_USERNAME)
        username_input = self.find_element(CrearSolicitudContratacionLocators.ANALISTA_USERNAME)
        username_input.send_keys(username)

        self.wait_until_element_clickable(CrearSolicitudContratacionLocators.BUSCAR_ANALISTA_USERNAME)
        buscar_analista_button = self.find_element(CrearSolicitudContratacionLocators.BUSCAR_ANALISTA_USERNAME)
        buscar_analista_button.click()
        analista_radio_locator = CrearSolicitudContratacionLocators.ANALISTA_RADIO(username)
        print('xpath test: ', analista_radio_locator)
        self.wait_until_element_clickable(analista_radio_locator)
        analista_radio = self.find_element(analista_radio_locator)
        analista_radio.click()
        ingresar_analista_button = self.find_element(CrearSolicitudContratacionLocators.INGRESAR_ANALISTA)
        ingresar_analista_button.click()
        return self
