from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class ItemizadoPELocators:
    AGREGAR_RUBRO = Locator(By.ID, 'ctl00_CPH1_uc_TablaItemizado_lbAgregarRubro')
    DESCRIPCION_RUBRO = Locator(By.ID, 'ctl00_CPH1_uc_TablaItemizado_uc_ModalRubro_tbAgregarRubro')
    AGREGAR_NUEVO_RUBRO = Locator(By.ID, 'ctl00_CPH1_uc_TablaItemizado_uc_ModalRubro_lbAgregarRubro')
    CERRAR_MODAL = Locator(By.XPATH, '//div[@id="ctl00_CPH1_uc_TablaItemizado_uc_ModalRubro_upTituloModal"]//button')

    @staticmethod
    def ingreso_items(indice):
        return Locator(By.ID, "ctl00_CPH1_uc_TablaItemizado_rptRubro_ctl{0}_lbAcciones".format(generate_index(indice)))

    @staticmethod
    def agregar_item(indice):
        return Locator(By.ID, "ctl00_CPH1_uc_TablaItemizado_rptRubro_ctl{0}_lbAgregarItem".format(generate_index(indice)))
    NOMBRE_ITEM = Locator(By.ID, 'ctl00_CPH1_uc_TablaItemizado_uc_ModalItem_tbAgregar')
    AGREGAR_ITEM = Locator(By.ID, 'ctl00_CPH1_uc_TablaItemizado_uc_ModalItem_lbAgregar')
    CERRAR_MODAL_ITEM = Locator(By.XPATH, '//div[@id="ctl00_CPH1_uc_TablaItemizado_uc_ModalItem_TituloModal"]//button')
    RANDOM_CLICK = Locator(By.ID, 'modalItem')
    COMPUTO_Y_PRESUPUESTO = Locator(By.ID, 'ctl00_CPH1_EncabezadoItemizado_lbComputoPresupuesto')
    TABLA_DE_INSUMOS = Locator(By.ID, 'ctl00_CPH1_uc_TablaItemizado_btnTablaInsumos')

def generate_index(index):
    if index < 10:
        return str(0)+str(index)
    return str(index)
