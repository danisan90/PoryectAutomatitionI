from page_objects.base_page import BasePage
from page_objects.PLIEGO.properties.ingresar_acto_administrativo_sade_locators import IngresarActoAdministrativoSadeLocators
import page_objects.PLIEGO.indice_proceso as indice_proceso
from config.parameters import Parameters
from time import *


class IngresarActoAdministrativoSade(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.pliego = Parameters.get_pliego()

    def pliego_bases_condiciones_generales(self):
        sleep(2)
        self.find_select(IngresarActoAdministrativoSadeLocators.TIPO_DOCUMENTO).select_by_visible_text(self.pliego['actoadministrativosade'])
        self.find_select(IngresarActoAdministrativoSadeLocators.ANIO).select_by_visible_text(self.pliego['anio'])
        self.find_element(IngresarActoAdministrativoSadeLocators.REPARTICION).send_keys(self.pliego['reparticion'])
        self.find_element(IngresarActoAdministrativoSadeLocators.NUMERO).send_keys(self.pliego['numero'])
        self.find_element(IngresarActoAdministrativoSadeLocators.BUTTON_BUSCAR).click()
        sleep(3)
        self.wait_until_element_clickable(IngresarActoAdministrativoSadeLocators.VINCULACION).click()
        self.wait_until_element_clickable(IngresarActoAdministrativoSadeLocators.VINCULAR).click()
        sleep(5)
        self.find_element(IngresarActoAdministrativoSadeLocators.GUARDAR_Y_VOLVER).click()
        return indice_proceso.CompletarIndicesProceso(self.driver)
