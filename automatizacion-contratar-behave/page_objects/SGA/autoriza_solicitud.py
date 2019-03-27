from page_objects.base_page import BasePage
from page_objects.SGA.properties.autoriza_sco_locator import AutorizaLocators
from page_objects.MENU import menu


class AutorizaSco(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.menu = menu.MenuPageObject(self.driver)

    def mensaje_exito_autoriza(self):
        return self.find_element(AutorizaLocators.MENSAJE_EXITO).text
