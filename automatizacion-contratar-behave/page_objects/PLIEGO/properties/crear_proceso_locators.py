from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class CrearProcesoLocators:
    NOMBRE_PROCESO_CONTRATACION = Locator(By.ID,'ctl00_CPH1_txtNomProceso')
    LICITACION_PUBLICA = Locator(By.ID, 'ctl00_CPH1_rblLicitConcursoCont_0')
    TIPO_CONTRATACION = Locator(By.ID, 'ctl00_CPH1_ddlTipoContratacion')
    TIPO_CONTRATACION_OBRA = Locator(By.XPATH,'//option[@value="Obra"]')
    ENCUADRE_LEGAL = Locator(By.XPATH, '//option[@value="7"]')
    BUTTON_AGREGAR_ENCUADRE = Locator(By.ID, 'ctl00_CPH1_imgAgregarSeleccionado')
    SIGUIENTE_PASO = Locator(By.XPATH, '//a[@id="ctl00_CPH1_lnkSiguientePaso"]')
