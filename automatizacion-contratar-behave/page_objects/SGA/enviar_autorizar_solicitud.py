from page_objects.base_page import BasePage
from page_objects.SGA.properties.enviar_a_autorizador_locators import EnviarAAutorizadorLocators
from page_objects.MENU import menu

class EnviarAutorizarSco(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.menu = menu.MenuPageObject(self.driver)

    def mensaje_exito_envio_autorizar(self):
        return self.find_element(EnviarAAutorizadorLocators.MENSAJE_EXITO).text

