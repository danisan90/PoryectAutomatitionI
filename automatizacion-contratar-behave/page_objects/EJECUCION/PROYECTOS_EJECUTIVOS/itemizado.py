from page_objects.base_page import BasePage
from page_objects.EJECUCION.properties.itemizado_locators import ItemizadoPELocators
from config.parameters import Parameters
from time import *


class Itemizado(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.proyectoEjecutivo = Parameters.get_proyectoEjecutivo()

    def ingresar_items(self):
        for indice in range(0, len(self.proyectoEjecutivo['nombrerubro'])):
            sleep(4)
            self.wait_until_element_clickable(ItemizadoPELocators.AGREGAR_RUBRO).click()
            self.wait_until_element_clickable(ItemizadoPELocators.DESCRIPCION_RUBRO).send_keys(self.proyectoEjecutivo['nombrerubro'][indice])
            self.wait_for_element(ItemizadoPELocators.AGREGAR_NUEVO_RUBRO).click()
            self.wait_for_element(ItemizadoPELocators.CERRAR_MODAL).click()
        sleep(3)
        for indice in range(0, len(self.proyectoEjecutivo['nombrerubro'])):
            sleep(3)
            self.wait_until_element_clickable(ItemizadoPELocators.ingreso_items(indice)).click()
            self.wait_until_element_clickable(ItemizadoPELocators.agregar_item(indice)).click()
            sleep(3)
            self.wait_until_element_clickable(ItemizadoPELocators.NOMBRE_ITEM).send_keys(self.proyectoEjecutivo['NOMBREITEM'])
            self.wait_until_element_clickable(ItemizadoPELocators.AGREGAR_ITEM).click()
            self.find_element(ItemizadoPELocators.RANDOM_CLICK).click()
            sleep(3)
            self.find_element(ItemizadoPELocators.COMPUTO_Y_PRESUPUESTO).click()
            #TABLA DE INSUMOS
            self.wait_for_element(ItemizadoPELocators.TABLA_DE_INSUMOS).click()
        return CatalogoInsumos

