from page_objects.base_page import BasePage
import page_objects.SGA.completar_solicitud_gasto as completar_solicitud_gasto
from page_objects.SGA.properties.items_sco_locator import CompletarItems
from config.parameters import Parameters
from time import *


class Items(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.sco = Parameters.get_sco()

    def completar_items(self):
        for indice in range(0, len(self.sco['CODIGO_ITEMS'])):
            self.wait_for_element(CompletarItems.INGRESAR_ITEM).clear()
            self.find_element(CompletarItems.INGRESAR_ITEM).send_keys(self.sco['CODIGO_ITEMS'][indice])
            self.find_element(CompletarItems.BOTON_CARGAR).click()
            sleep(8)
            self.find_element(CompletarItems.INGRESAR_NOMBRE_FO).send_keys(self.sco['NOMBRE_FO'][indice])
            self.find_element(CompletarItems.INGRESAR_CANTIDAD).send_keys(self.sco['CANTIDAD'])
            self.find_element(CompletarItems.INGRESAR_PRECIO).send_keys(self.sco['PRECIO_UNITARIO'])
            self.find_element(CompletarItems.INGRESAR_FECHA).send_keys(self.sco['FECHA_PREP_OFIC'])
            sleep(3)
            self.find_element(CompletarItems.SELECCIONAR_PO).click()
            sleep(2)
            self.find_elements(CompletarItems.INGRESAR_NOMBRE_PO)[1].click()
            sleep(5)
            self.find_element(CompletarItems.INGRESAR_ITEM_BUTTON).click()
            sleep(3)
        self.find_element(CompletarItems.GUARDAR_VOLVER).click()
        return completar_solicitud_gasto.CompletarSolicitudGasto(self.driver)
