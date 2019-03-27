from page_objects.base_page import BasePage
from page_objects.PLIEGO.properties.ingresar_supervisor_locator import IngresarSupervisorLocators
from config.parameters import Parameters


class IngresarSupervisor(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.pliego = Parameters.get_pliego()

    def seleccionar_supervisor(self):
        self.wait_until_element_clickable(IngresarSupervisorLocators.SELECCIONO_SUPERVISOR).select_by_visible_text(self.pliego['supervisor'])
        self.find_element(IngresarSupervisorLocators.AGREGAR_SUPERVISOR).click()
        self.find_element(IngresarSupervisorLocators.CHEQUEAR_SUPERVISOR).select_by_visible_text(self.pliego['supervisor'])

