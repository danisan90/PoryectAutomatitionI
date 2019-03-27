from behave import *
from generated_data.data_manager import DataManager
from config.parameters import Parameters

#from config.bac_data import success_messages


@when('va a editar proceso de contratacion desde bandeja de entrada')
def step_imp(context):
    context.page = context.page.buscar_proceso_compra_bandeja()


@when('crea un proceso de contratacion')
def step_imp(context):
    context.page = context.page.menu.menu_crear_pliego()
    context.page = context.page.crear_pc()
    DataManager.set_numero_pc(context.page.obtener_numero_pc())


@when('completa indices del pliego')
def step_imp(context):
    context.page = context.page.indice_info_basica_pc()
    context.page = context.page.completar_informacion_basica()
    context.page = context.page.solicitud_de_contratacion()
    context.page = context.page.solicitudes_de_contratacion()
    context.page = context.page.pliego_de_bases_condiciones()
    context.page = context.page.pliego_bases_condiciones_generales()
    context.page = context.page.requisitos_minimos_participacion()
    context.page = context.page.requisitos_participacion()
    context.page = context.page.garantias()
    context.page = context.page.garantias_pco()
    context.page = context.page.montos_plazos_contratacion()
    context.page = context.page.monto_y_plazos_de_la_contratacion()
    context.page = context.page.supervisor()




