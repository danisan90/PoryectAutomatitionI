from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class CompletarDatosObraLocators:
    SELECCIONAR_PLAN = Locator(By.ID, 'ctl00_CPH1_ddlPlanObra')
    SELECCIONAR_PROGRAMA = Locator(By.ID, 'ctl00_CPH1_ddlProgramaObra')
    SELECCIONAR_GRUPO = Locator(By.ID, 'ctl00_CPH1_ddlGrupoObra')
    SELECCIONAR_SUBGRUPO = Locator(By.ID, 'ctl00_CPH1_ddlSubGrupoObra')
    SELECCIONAR_TIPO_PROYECTO = Locator(By.ID, 'ctl00_CPH1_ddlTipoProyecto')
    #inicia modal ubicacion geografica
    #INGRESAR_UBICACION_GEOGRAFICA = Locator(By.ID, 'ctl00_CPH1_UC_ListadoFrentesObra_gvFrentesObra_ctl02_ibGeoInfo')
    @staticmethod
    def ingresar_ubicacion(nombre_fo):
        return Locator(By.XPATH, "//span[text()= '{0}']/parent::td//parent::tr//a[contains(@id, 'GeoInfo')]".format(nombre_fo))

    SELECCIONAR_PROVINCIA = Locator(By.ID, 'ctl00_CPH1_UC_ListadoFrentesObra_ddlProvincia')
    AGREGAR_UBICACION = Locator(By.ID, 'ctl00_CPH1_UC_ListadoFrentesObra_lnkAgregarUbicacion')
    INGRESAR_LATITUD = Locator(By.ID, 'ctl00_CPH1_UC_ListadoFrentesObra_txtLatitud')
    INGRESAR_LONGITUD = Locator(By.ID, 'ctl00_CPH1_UC_ListadoFrentesObra_txtLongitud')
    GUARDAR_DATOS = Locator(By.ID, 'ctl00_CPH1_UC_ListadoFrentesObra_lnkGuardarDatosFrente')
    #Fin modal
    GUARDAR_DATOS_OBRA = Locator(By.ID, 'ctl00_CPH1_lnkGuardarYVolver')