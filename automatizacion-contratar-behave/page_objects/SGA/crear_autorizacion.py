from page_objects.base_page import BasePage
from page_objects.SGA.properties.crear_autorizador_locator import SeleccionarAutorizadoresLocators
import page_objects.SGA.completar_solicitud_gasto as completar_solicitud_gasto


class CrearAutorizacionSco(BasePage):
    def seleccionar_autorizadores(self):
        self.wait_for_element(SeleccionarAutorizadoresLocators.SELECCION_ANALISTA).click()
        self.find_element(SeleccionarAutorizadoresLocators.BUTTON_SELECCIONAR).click()
        self.wait_for_element_visibility(SeleccionarAutorizadoresLocators.AUTORIZADOR_SELECCIONADO)
        self.find_element(SeleccionarAutorizadoresLocators.GUARDAR_Y_VOLVER).click()
        return completar_solicitud_gasto.CompletarSolicitudGasto(self.driver)
