from page_objects.base_page import BasePage
import page_objects.SGA.completar_solicitud_gasto as completar_solicitud_gasto
from page_objects.SGA.properties.completar_tabla_vnr_locators import CompletarTablaVNRLocators
from config.parameters import Parameters

from time import *


class TablaVNRSco(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.sco = Parameters.get_sco()

    def tabla_vnr_po(self):
        #creala tabla
        self.find_element(CompletarTablaVNRLocators.NUEVA_TABLA).click()
        #ingresa al modal nueva tabla
        sleep(5)
        self.find_element(CompletarTablaVNRLocators.NOMBRE_TABLA).send_keys(self.sco['NOMBRE_TABLA'])
        sleep(3)
        self.find_element(CompletarTablaVNRLocators.SELECCIONAR_INSUMO).click()
        self.find_elements(CompletarTablaVNRLocators.SELECCIONAR_PRODUCTO)[1].click()
        sleep(3)
        self.find_element(CompletarTablaVNRLocators.PORCENTAJE).send_keys(self.sco['PORCENTAJE'])
        self.find_element(CompletarTablaVNRLocators.RANDOM_CLICK).click()
        sleep(2)
        self.find_element(CompletarTablaVNRLocators.GUARDAR_TABLA).click()
        sleep(4)
        #selecciona la tabla
        for indice in range(0, len(self.sco['NOMBRE_FO'])):
            self.find_select(CompletarTablaVNRLocators.seleccionar_tabla(self.sco['NOMBRE_FO'][indice])).select_by_visible_text('Tabla 1')
            #self.find_elements(CompletarTablaVNRLocators.SELECCIONAR_TABLA_CREADA)[0].click()
            sleep(2)
        self.find_element(CompletarTablaVNRLocators.GUARDAR_TABLA_VOLVER).click()

        return completar_solicitud_gasto.CompletarSolicitudGasto(self.driver)
