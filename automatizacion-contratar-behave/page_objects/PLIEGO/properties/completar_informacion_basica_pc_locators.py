from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class CompletarInfoBasicaPcLocators:
    @staticmethod
    def etapa(tipo_etapa):
        return Locator(By.ID, "ctl00_CPH1_rblTipoEtapa_{0}".format(tipo_etapa))

    @staticmethod
    def sistemaDeContratacion(sistema):
        return Locator(By.ID, "ctl00_CPH1_cbSC{0}".format(sistema))

    @staticmethod
    def tipoDeAdjudicacion(tipo_adjudicacion):
        return Locator(By.ID, "ctl00_CPH1_rblTipoCotizRenglonAdjudicacion_{0}".format(tipo_adjudicacion))

    @staticmethod
    def tipoDeCotizacion(tipo_cotizacion):
        return Locator(By.ID, "ctl00_CPH1_rblTipoCotizRenglonOferta_{0}".format(tipo_cotizacion))

    TIPO_MONEDA = Locator(By.ID, "ctl00_CPH1_lstMonedas")
    BUTTON_AGREGAR_MONEDA = Locator(By.ID, "ctl00_CPH1_imgAgregarMoneda")
    @staticmethod
    def tipo_moneda_seleccionada(moneda):
        return Locator(By.XPATH, "//select[@id='ctl00_CPH1_lstMonedasSel']//option[contains(text(), {0})]".format(moneda))

    CANTIDAD_DIAS = Locator(By.ID, "ctl00_CPH1_txtCantidadDiasOferta")
    PLAZO_MANTENIMIENTO_PROPUESTA = Locator(By.ID, "ctl00_CPH1_ddlTipoDuracionOferta")
    RECEPCION_DOCUMENTACION_FISICA = Locator(By.ID, "ctl00_CPH1_ddlDirDoctoFisica")
    GUARDAR_Y_VOLVER = Locator(By.ID, "ctl00_CPH1_lnkGuardarYVolver")
