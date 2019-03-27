from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class InformacionContratoLocators:
    CANTIDAD_DIAS = Locator(By.ID, 'ctl00_CPH1_UcDatosInfoContrato_txtDiasActaInicio')

    @staticmethod
    def duracion_de_la_obra(nombre_fo):
        return Locator(By.XPATH, "//span[text()= '{0}']//parent::td//parent::tr//a[contains(@id, 'DuracionObra')]".format(nombre_fo))

    DIAS_DURACION_OBRA = Locator(By.ID, 'ctl00$CPH1$UcDatosInfoContrato$UC_ListadoFrentesObra$txtCantidadDuracion')
    UNIDAD_DE_TIEMPO = Locator(By.ID, 'ctl00_CPH1_UcDatosInfoContrato_UC_ListadoFrentesObra_ddlUnidadTiempoDuracion')
    GUARDAR = Locator(By.ID, 'ctl00_CPH1_UcDatosInfoContrato_UC_ListadoFrentesObra_btnGuardarDuracion')
    GUARDAR_Y_VOLVER = Locator(By.ID, 'ctl00_CPH1_lnkGuardarVolver')


