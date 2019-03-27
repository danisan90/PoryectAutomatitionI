from page_objects.base_page import BasePage
from page_objects.MENU.properties.menu_locators import MenuPageLocators
from page_objects.SGA.crear_solicitud_contratacion import CrearSolicitudContratacion
from page_objects.EJECUCION.PROYECTOS_EJECUTIVOS.proyectos_ejecutivos import ProyectoEjecutivo
from page_objects.SGA.buscar_solicitud_contratacion import BuscarSolicitudContratacionPageObject
from page_objects.PLIEGO.cear_proceso import CrearProcesoDeContratacion

from time import *


class MenuPageObject(BasePage):
    def menu_proyecto_obra(self):
        self.wait_for_element(MenuPageLocators.PROYECTO_OBRA).click()
        return ProyectoEjecutivo(self.driver)

    def menu_crear_solicitud_contratacion(self):
        self.wait_for_element_visibility(MenuPageLocators.MENU_CLICK).click()
        self.wait_until_element_clickable(MenuPageLocators.SUBMENU_CREAR).click()
        sleep(5)
        return CrearSolicitudContratacion(self.driver)

    def menu_buscar_solicitud_contratacion(self):
        self.wait_until_element_clickable(MenuPageLocators.MENU_CLICK).click()
        self.wait_for_element_visibility(MenuPageLocators.SUBMENU_BUSCAR).click()
        sleep(4)
        return BuscarSolicitudContratacionPageObject(self.driver)

    def menu_crear_pliego(self):
        self.wait_until_element_clickable(MenuPageLocators.PROCESO_CONTRATACION).click()
        self.wait_until_element_clickable(MenuPageLocators.CREAR_PROCESO_CONTRATACION).click()
        return CrearProcesoDeContratacion(self.driver)
