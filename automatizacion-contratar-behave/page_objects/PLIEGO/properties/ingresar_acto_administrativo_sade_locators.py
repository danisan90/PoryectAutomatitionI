from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class IngresarActoAdministrativoSadeLocators:
        TIPO_DOCUMENTO = Locator(By.ID, 'ctl00_CPH1_ucIngresarActo_ddlTipoDocumento')
        ANIO = Locator(By.ID, 'ctl00_CPH1_ucIngresarActo_DropDownAnio')
        REPARTICION = Locator(By.ID, 'ctl00_CPH1_ucIngresarActo_txtReparticion')
        NUMERO = Locator(By.ID, 'ctl00_CPH1_ucIngresarActo_txtNumero')
        BUTTON_BUSCAR = Locator(By.ID, 'ctl00_CPH1_ucIngresarActo_btnBuscar')
        VINCULACION = Locator(By.ID, 'ctl00_CPH1_ucIngresarActo_rptActoAdministrativo_ctl01_divBddAcciones')
        VINCULAR = Locator(By.ID, 'ctl00_CPH1_ucIngresarActo_rptActoAdministrativo_ctl01_btnVincular')
        GUARDAR_Y_VOLVER = Locator(By.ID, 'ctl00_CPH1_ucIngresarActo_btnIngresarActo')
