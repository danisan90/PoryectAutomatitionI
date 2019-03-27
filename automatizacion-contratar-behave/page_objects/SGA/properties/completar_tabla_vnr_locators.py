from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class CompletarTablaVNRLocators:
    NUEVA_TABLA = Locator(By.ID, 'ctl00_CPH1_btnNuevaTabla1')
    #cargar tabla
    NOMBRE_TABLA = Locator(By.ID, 'ctl00_CPH1_UCCrearTabla1_tbNombre')
    SELECCIONAR_INSUMO = Locator(By.ID, 'select2-ctl00_CPH1_UCCrearTabla1_rptPonderacionIndice_ctl00_ddlIndice-container')
    SELECCIONAR_PRODUCTO = Locator(By.XPATH, "//li[contains(@id, 'select2-ctl00_CPH1_UCCrearTabla1_rptPonderacionIndice_ctl00_ddlIndice-result')]")
    PORCENTAJE = Locator(By.ID, 'ctl00_CPH1_UCCrearTabla1_rptPonderacionIndice_ctl00_tbPorcentaje')
    GUARDAR_TABLA = Locator(By.ID, 'ctl00_CPH1_UCCrearTabla1_lnkGuardar')
    #termina carga tabla
    #selecciona tabla
    @staticmethod
    def seleccionar_tabla(nombre_fo):
        return Locator(By.XPATH,"//p[text()='{0}']/parent::td//parent::td//parent::tr//select[contains(@id, 'Tablas1')]".format(nombre_fo))
    #SELECCIONAR_TABLA = Locator(By.XPATH, "//select[@id='ctl00_CPH1_rptFrentesDeObra_ctl00_ddlTablas1']")
    SELECCIONAR_TABLA_CREADA = Locator(By.XPATH, "//select[@id='ctl00_CPH1_rptFrentesDeObra_ctl00_ddlTablas1']//option[contains(.,'Tabla 1')]")

    #guardar tabla
    RANDOM_CLICK = Locator(By.ID, 'ctl00_CPH1_UCCrearTabla1_upModalTabla1')
    GUARDAR_TABLA_VOLVER = Locator(By.ID, 'ctl00_CPH1_lnkGuardarYVolver')
