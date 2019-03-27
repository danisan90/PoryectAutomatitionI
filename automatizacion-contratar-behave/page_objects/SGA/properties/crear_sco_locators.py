from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class CrearSolicitudContratacionLocators():
    def analista_radio(username):
        xpath = '//*[contains(@id, "GridAnalistas")]/tbody/tr[2]/td[3]/p[contains(.,\"{}\")]/parent::*/parent::*/td[4]/input[contains(@id,"radioAnalistas")]'.format(
            username)
        return Locator(By.XPATH, xpath)

    NOMBRE = Locator(By.XPATH, '// input[contains( @ id, "NombreSolicitud")]')
    OBJETO = Locator(By.XPATH, '//textarea[contains(@id,"ObjetoSolicitud")]')
    TIPO = Locator(By.XPATH, '// select[contains( @ id, "TipoSolicitud")]')
    ABRIR_MODAL_BUTTON = Locator(By.XPATH, '//a[contains(@id,"AbrirModalBuscarAnalista")]')
    MODAL_FRAME = Locator(By.XPATH, '//div[contains(@id,"ModalBuscarAnalista")]')
    ANALISTA_USERNAME = Locator(By.ID, "ctl00_CPH1_txtUserNameAnalista")
    BUSCAR_ANALISTA_USERNAME = Locator(By.ID, "ctl00_CPH1_btnBuscarAnalistaPorUsername")
    TABLA_ANALISTAS = Locator(By.ID, "ctl00_CPH1_GridAnalistas")
    # ANALISTA_USERNAME = Locator(By.XPATH, '//input[contains(@id,"UserNameAnalista")]')
    # BUSCAR_ANALISTA_USERNAME = Locator(By.XPATH, '//a[contains(@id,"BuscarAnalistaPorUsername")]')
    ANALISTA_RADIO =  analista_radio
    INGRESAR_ANALISTA = Locator(By.XPATH, '// a[contains( @ id, "SeleccionarAnalista")]')
    SIGUIENTE = Locator(By.XPATH, '//a[contains(@id,"SiguientePaso")]')
