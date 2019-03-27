from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class CompletarImputacionLocators:
    OBJETOS_DE_GASTO = Locator(By.XPATH,
                                   '//table[@id="ctl00_CPH1_grillaTotalImputado_gvImputaciones"]//tbody//tr//td[1]//p')
    COLUMNA_TOTAL = Locator(By.XPATH,
                                '//table[@id="ctl00_CPH1_grillaTotalImputado_gvImputaciones"]//tbody//tr//td[4]//p')
    OBJETO_PARTIDAS = Locator(By.ID, 'ctl00_CPH1_UCBuscadorPartidas_ddlObjetoGasto')
    BUSCAR_PARTIDAS = Locator(By.ID, 'ctl00_CPH1_UCBuscadorPartidas_lnkBuscarPartida')
    COMPLETAR_MONTO = Locator(By.ID,
                                  'ctl00_CPH1_UCBuscadorPartidas_GrillaResultadosPartida_gvPartidas_ctl02_txtMonto_txtTextBox_txtTextBox')
    CHECKBOX_PARTIDA = Locator(By.ID,
                                   'ctl00_CPH1_UCBuscadorPartidas_GrillaResultadosPartida_gvPartidas_ctl02_chkPartida')
    INGRESAR_IMPUTACION = Locator(By.ID, 'ctl00_CPH1_UCBuscadorPartidas_lnkIngresarImputacion')
    GUARDAR_Y_VOLVER = Locator(By.ID, 'ctl00_CPH1_lnkGuardarVolver')

