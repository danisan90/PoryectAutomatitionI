from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class MenuPageLocators:
    MENU_CLICK = Locator(By.ID, 'ctl00_NavBar_CtrlmenubaseBastrap_rptMenu_ctl00_lblMenu')
    MENU = Locator(By.XPATH, '//span[contains(.,"Solicitud De Contratación")]')
    PROYECTO_OBRA = Locator(By.ID, 'ctl00_NavBar_CtrlmenubaseBastrap_IrPE')
    #ctl00_NavBar_CtrlmenubaseBastrap_IrPE // ctl00_NavBar_IrPE
    SUBMENU_CREAR = Locator(By.XPATH, '//a[contains(text(), "Crear Solicitud de Contratación")]')
    #SUBMENU_CREAR = Locator(By.XPATH, '//a[@href="/SGA/CrearSolicitudGasto.aspx"]')
    # MENU_DISTINTO = Locator(By.LINK_TEXT, 'Solicitud De Contratación')
    MENU_DISTINTO = Locator(By.XPATH, "//a[contains(text(),'Solicitud De Contratación')]/parent::li")
    SUBMENU_BUSCAR = Locator(By.XPATH, '//a[contains(@href,"/SGA/BuscarSolicitudGasto.aspx")]')
    #/SGA/BuscarSolicitudGasto.aspx?qs=YJJtSdEkeTg=
    # BOTON VOLVER DEL PASO CORRESPONDIETE A LA COPIA DEL PROYECTO DE OBRA
    VOLVER = Locator(By.ID, 'ctl00_CPH1_RegresarPaginaAnterior_lnkVolver')
    PROCESO_CONTRATACION = Locator(By.ID, 'ctl00_NavBar_CtrlmenubaseBastrap_rptMenu_ctl01_lblMenu')
    CREAR_PROCESO_CONTRATACION = Locator(By.XPATH, '//a[contains(@href,"/PLIEGO/CrearProceso.aspx")]')

