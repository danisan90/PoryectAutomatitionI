from page_objects.base_page import BasePage
from page_objects.SGA.completar_informacion_basica import CompletarInformacionBasica
from page_objects.SGA.properties.completar_solicitud_contratacion_locator import CompletarSolicitudContratacionLocators
from page_objects.SGA.properties.enviar_autorizar_locators import EnviarAAutorizacionLocators
from page_objects.SGA.items import Items
from page_objects.SGA.datos_obra_solicitud import DatosObraSco
from page_objects.SGA.tabla_vnr import TablaVNRSco
import page_objects.SGA.envio_solicitud as envio_solicitud
import page_objects.SGA.completar_imputacion2 as completar_imputaciones
import page_objects.SGA.crear_autorizacion as seleccionar_autorizadores
from page_objects.SGA.enviar_autorizar_solicitud import EnviarAutorizarSco
DEFAULT_TIMEOUT = 10


class CompletarSolicitudGasto(BasePage):
    def obtener_numero_sco(self):
        self.wait_for_element(CompletarSolicitudContratacionLocators.NUMERO)
        return self.find_element(CompletarSolicitudContratacionLocators.NUMERO).text

    def obtener_estado_sco(self):
        self.wait_for_element(CompletarSolicitudContratacionLocators.ESTADO)
        return self.find_element(CompletarSolicitudContratacionLocators.ESTADO).text

    def obtener_nombre_sco(self):
        self.wait_for_element(CompletarSolicitudContratacionLocators.NOMBRE)
        return self.find_element(CompletarSolicitudContratacionLocators.NOMBRE).text

    def indice_informacion_basica(self):
        self.find_element(CompletarSolicitudContratacionLocators.INFO_BASICA).click()
        return CompletarInformacionBasica(self.driver)

    def indice_items(self):
        self.find_element(CompletarSolicitudContratacionLocators.ITEMS).click()
        return Items(self.driver)

    def datos_obra(self):
        self.wait_for_element(CompletarSolicitudContratacionLocators.DATOS_OBRA).click()
        return DatosObraSco(self.driver)

    def tabla_vnr(self):
        self.wait_for_element(CompletarSolicitudContratacionLocators.VNR).click()
        return TablaVNRSco(self.driver)

    def enviar_analista(self):
        self.find_element(CompletarSolicitudContratacionLocators.ENVIAR_ANALISTA).click()
        return envio_solicitud.EnvioSolicitud(self.driver)

    def informacion_presupuestaria_fuentes_internas(self):
        self.wait_for_element(CompletarSolicitudContratacionLocators.INFO_PRESUPUESTARIA).click()
        return completar_imputaciones.CompletarImputacionSco(self.driver)

    def lista_autorizadores(self):
        self.wait_for_element(CompletarSolicitudContratacionLocators.LISTA_AUTORIZADORES).click()
        return seleccionar_autorizadores.CrearAutorizacionSco(self.driver)

    def enviar_autorizar(self):
        self.wait_for_element(CompletarSolicitudContratacionLocators.SIGUIENTE_PASO).click()
        self.wait_until_element_clickable(EnviarAAutorizacionLocators.ENVIAR_A_AUTORIZAR).click()
        return EnviarAutorizarSco(self.driver)
