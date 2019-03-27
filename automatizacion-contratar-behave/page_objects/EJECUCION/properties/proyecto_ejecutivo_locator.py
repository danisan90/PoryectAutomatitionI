from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class ProyectoDeObraLocators:
    COPIAR_PROYECTO = Locator(By.XPATH, "//p[contains(text(),'PROYECTO CERO')]/parent::td//parent::tr//a[contains(@id, 'Copiar')]")
    INPUT_NOMBRE_PROYECTO = Locator(By.ID, 'ctl00_CPH1_UC_ModalCopiaProyectoEjecutivo_tbNombreProyectoEjecutivo')
    CLICK_AUXILIAR = Locator(By.ID, 'ctl00_CPH1_UC_ModalCopiaProyectoEjecutivo_TituloModal')
    COPIAR_BUTTON = Locator(By.ID, "ctl00_CPH1_UC_ModalCopiaProyectoEjecutivo_lbCopiarProyectoEjecutivo")

    @staticmethod
    def editar_button(nombre_po):
        return Locator(By.XPATH,
                       "//p[text() = '{0}']/parent::td//parent::tr//a[contains(@id, 'pencil')]".format(nombre_po))

    PAG_PROYECTO_OBRA = Locator(By.ID, 'ctl00_CPH1_Navegador_rptUbicaciones_ctl01_ubicacionPagina')
    NUEVO_PROYECTO = Locator(By.ID, 'ctl00_CPH1_lnkAgregarNuevoPE')
    INGRESAR_NOMBRE_NUEVO_PROYECTO = Locator(By.ID, 'ctl00_CPH1_txtNombre')
    GUARDAR_NP = Locator(By.ID, 'ctl00_CPH1_lnkModalGuardarPE')
