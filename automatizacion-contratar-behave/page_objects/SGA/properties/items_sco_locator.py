from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class CompletarItems:
    INGRESAR_ITEM = Locator(By.ID, 'ctl00_CPH1_UC_IngresarItems_txtCodigoItem')
    BOTON_CARGAR = Locator(By.ID, 'ctl00_CPH1_UC_IngresarItems_btnCargarItem')
    MODAL_BUSCADOR = Locator(By.XPATH, '//div[contains(@id,"IngresarItems")')
    INGRESAR_BUSQUEDA_ITEM = Locator(By.ID, 'ctl00_CPH1_UC_IngresarItems_txtBuscadorItem')
    BUSQUEDA_ITEM = Locator(By.ID,'ctl00_CPH1_UC_IngresarItems_btnBuscarItemFiltro')
    INGRESAR_NOMBRE_FO = Locator(By.ID, 'ctl00_CPH1_UC_EditarItem_tbNombreObra')
    INGRESAR_CANTIDAD = Locator(By.ID, 'ctl00_CPH1_UC_EditarItem_txtCantidad')
    INGRESAR_PRECIO = Locator(By.ID, 'ctl00_CPH1_UC_EditarItem_txtPrecioUnitario')
    INGRESAR_FECHA = Locator(By.ID, 'ctl00_CPH1_UC_EditarItem_txtFechaPresupuestoOficial')
    SELECCIONAR_PO = Locator(By.ID, 'select2-ctl00_CPH1_UC_EditarItem_UC_PrototipoProyectoEjecutivo_ddlVinculacionArchivos-container')
    INGRESAR_NOMBRE_PO = Locator(By.XPATH, "//li[contains(@id, 'select2-ctl00_CPH1_UC_EditarItem_UC_PrototipoProyectoEjecutivo_ddlVinculacionArchivos')]")
    INGRESAR_ITEM_BUTTON = Locator(By.ID, 'ctl00_CPH1_btnIngresar')
    GUARDAR_VOLVER = Locator(By.ID, 'ctl00_CPH1_btnGuardaVolver')

