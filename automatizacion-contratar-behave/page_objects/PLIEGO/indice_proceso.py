from page_objects.base_page import BasePage
from page_objects.PLIEGO.properties.indice_proceso_locators import IndicesDelPliegoLocators
from page_objects.PLIEGO.informacion_basica_pliego import CompletarInfoBasicaPC
from page_objects.PLIEGO.seleccion_sco_pc import SeleccionSolicitudGastoPliego
from page_objects.PLIEGO.ingresar_acto_administrativoSADE import IngresarActoAdministrativoSade
from page_objects.PLIEGO.requisitos_minimos_participacion import RequisitosMinimosParticipacion
from page_objects.PLIEGO.garantias import Garantias
from page_objects.PLIEGO.informacion_contrato import InformacionContrato
from page_objects.PLIEGO.ingresar_supervisor import IngresarSupervisor


class CompletarIndicesProceso(BasePage):
    def obtener_numero_pc(self):
        self.wait_for_element(IndicesDelPliegoLocators.NUMERO_PC)
        return self.find_element(IndicesDelPliegoLocators.NUMERO_PC).text

    def indice_info_basica_pc(self):
        self.wait_until_element_clickable(IndicesDelPliegoLocators.INFO_BASICA_PC).click()
        return CompletarInfoBasicaPC(self.driver)

    def solicitud_de_contratacion(self):
        self.wait_until_element_clickable(IndicesDelPliegoLocators.SCO).click()
        return SeleccionSolicitudGastoPliego(self.driver)

    def pliego_de_bases_condiciones(self):
        self.wait_until_element_clickable(IndicesDelPliegoLocators.PLIEGO_BASES_CONDICIONES).click()
        return IngresarActoAdministrativoSade(self.driver)

    def requisitos_minimos_participacion(self):
        self.wait_until_element_clickable(IndicesDelPliegoLocators.REQUISITOS_MINIMOS_DE_PARTICIPACION).click()
        return RequisitosMinimosParticipacion(self.driver)

    def garantias(self):
        self.wait_until_element_clickable(IndicesDelPliegoLocators.INDICE_GARANTIAS).click()
        return Garantias(self.driver)

    def montos_plazos_contratacion(self):
        self.wait_until_element_clickable(IndicesDelPliegoLocators.MONTOS_Y_PLAZOS_CONTRATACION).click()
        return InformacionContrato(self.driver)

    def supervisor(self):
        self.wait_until_element_clickable(IndicesDelPliegoLocators.SEPERVISOR).click()
        return IngresarSupervisor(self.driver)
