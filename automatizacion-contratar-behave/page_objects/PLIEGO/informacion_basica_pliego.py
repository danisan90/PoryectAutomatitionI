from page_objects.base_page import BasePage
from page_objects.PLIEGO.properties.completar_informacion_basica_pc_locators import CompletarInfoBasicaPcLocators
import page_objects.PLIEGO.indice_proceso as indice_proceso
from config.parameters import Parameters
from time import *


class CompletarInfoBasicaPC(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.pliego = Parameters.get_pliego()

    def completar_informacion_basica(self):
        self.find_element(CompletarInfoBasicaPcLocators.etapa(self.pliego['tipoEtapa'])).click()
        for sistemaContratacion in self.pliego['sistemaDeContratacion']:
            sleep(4)
            self.find_element(CompletarInfoBasicaPcLocators.sistemaDeContratacion(sistemaContratacion)).click()
        self.find_element(CompletarInfoBasicaPcLocators.tipoDeAdjudicacion(self.pliego['tipoadjudicacion'])).click()
        sleep(2)
        self.wait_for_element(CompletarInfoBasicaPcLocators.tipoDeCotizacion(self.pliego['tipodecotizacion'])).click()
        self.find_select(CompletarInfoBasicaPcLocators.TIPO_MONEDA).select_by_visible_text(self.pliego['moneda'])
        self.wait_for_element_visibility(CompletarInfoBasicaPcLocators.BUTTON_AGREGAR_MONEDA).click()
        #self.wait_for_element_visibility(CompletarInfoBasicaPcLocators.tipo_moneda_seleccionada(self.pliego['moneda']))
        sleep(4)
        self.wait_for_element(CompletarInfoBasicaPcLocators.CANTIDAD_DIAS).clear()
        self.find_element(CompletarInfoBasicaPcLocators.CANTIDAD_DIAS).send_keys(self.pliego['plazoMantenimientoDePropuesta']["CANTIDADDEDIAS"])
        sleep(2)
        self.find_select(CompletarInfoBasicaPcLocators.PLAZO_MANTENIMIENTO_PROPUESTA).select_by_visible_text(self.pliego['plazoMantenimientoDePropuesta']['tipodedias'])
        sleep(4)
        self.find_select(CompletarInfoBasicaPcLocators.RECEPCION_DOCUMENTACION_FISICA).select_by_visible_text(self.pliego['direccion'])
        self.find_element(CompletarInfoBasicaPcLocators.GUARDAR_Y_VOLVER).click()
        return indice_proceso.CompletarIndicesProceso(self.driver)
