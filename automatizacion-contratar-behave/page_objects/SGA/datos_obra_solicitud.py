from page_objects.base_page import BasePage
import page_objects.SGA.completar_solicitud_gasto as completar_solicitud_gasto
from page_objects.SGA.properties.completar_datos_obra_locators import CompletarDatosObraLocators
from config.parameters import Parameters

from time import *


class DatosObraSco(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.sco = Parameters.get_sco()

    def plan_de_obra(self):
        # este plan de obra genera el proyecto en ejecucion, faltaria agarrar el select si no quieo que genere
        self.find_select(CompletarDatosObraLocators.SELECCIONAR_PLAN).select_by_visible_text(
            "Plan Nacional de Arquitectura")
        self.find_select(CompletarDatosObraLocators.SELECCIONAR_PROGRAMA).select_by_visible_text(
            "ME - Fortalecimiento Edilicio de Jardines Infantiles")
        self.find_select(CompletarDatosObraLocators.SELECCIONAR_GRUPO).select_by_visible_text("ARQUITECTURA")
        sleep(2)
        self.find_select(CompletarDatosObraLocators.SELECCIONAR_SUBGRUPO).select_by_visible_text(
            "Edificios educativos")
        sleep(2)
        self.find_select(CompletarDatosObraLocators.SELECCIONAR_TIPO_PROYECTO).select_by_visible_text(
            "Jardines de infantes")
        sleep(2)
        # desde aca ingresa la informacion geografica
        for indice in range(0, len(self.sco['NOMBRE_FO'])):
            self.find_element(CompletarDatosObraLocators.ingresar_ubicacion(self.sco['NOMBRE_FO'][indice])).click()
            sleep(5)
            self.wait_for_element(CompletarDatosObraLocators.SELECCIONAR_PROVINCIA)
            self.find_select(CompletarDatosObraLocators.SELECCIONAR_PROVINCIA).select_by_visible_text("CATAMARCA")
            self.find_element(CompletarDatosObraLocators.AGREGAR_UBICACION).click()
            sleep(4)
            self.find_element(CompletarDatosObraLocators.INGRESAR_LATITUD).send_keys(self.sco['LATITUD'])
            self.find_element(CompletarDatosObraLocators.INGRESAR_LONGITUD).send_keys(self.sco['LONGITUD'])
            self.find_element(CompletarDatosObraLocators.GUARDAR_DATOS).click()
            sleep(8)
        self.find_element(CompletarDatosObraLocators.GUARDAR_DATOS_OBRA).click()
        sleep(5)

        return completar_solicitud_gasto.CompletarSolicitudGasto(self.driver)
