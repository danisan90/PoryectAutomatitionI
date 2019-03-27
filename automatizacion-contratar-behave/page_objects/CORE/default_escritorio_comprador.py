from page_objects.base_page import BasePage
from page_objects.MENU.menu import MenuPageObject
from page_objects.CORE.properties.locators import EnvioSolicitudLocators


class DefaultEscritorioComprador(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.menu = MenuPageObject(self.driver)

    def ir_escritorio(self):
        self.wait_until_element_clickable(EnvioSolicitudLocators.IR_AL_ESCRITORIO).click()
        return self


