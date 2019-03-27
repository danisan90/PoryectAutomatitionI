from page_objects.base_page import BasePage
from page_objects.SGA.properties.envio_solicitud import EnvioSolicitudLocators
from page_objects.MENU import menu


class EnvioSolicitud(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.menu = menu.MenuPageObject(self.driver)

    def get_mensaje_exito(self):  # TODO Unificar IDs de alerts
        return self.find_element(EnvioSolicitudLocators.MENSAJE_EXITO).text
