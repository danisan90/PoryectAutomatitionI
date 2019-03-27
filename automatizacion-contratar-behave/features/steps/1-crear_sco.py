from behave import *
from page_objects.MENU.menu_ciudadano import MenuCiudadano
from config.parameters import Parameters
from config.data import mensajes_exito
from generated_data.data_manager import DataManager
from page_objects.MENU.menu import MenuPageObject


@given('el usuario se encuentra en el home')
def step_imp(context):
    context.driver.get(context.ambiente['url'])
    context.page = MenuCiudadano(context.driver)


@given('existe un proyecto de obra')
def step_imp(context):
    context.nombres_po = Parameters.get_nombres_po()
    context.execute_steps("""Given el usuario se encuentra en el home
                            When inicia sesion con usuario solicitante solicitanteSCO""")
    context.page = context.page.menu.menu_proyecto_obra()
    for nombre_po in context.nombres_po:
        context.page = context.page.copiar_proyecto_obra(nombre_po)


@when('inicia sesion con usuario {tipo_usuario} {usuario}')
def step_imp(context, tipo_usuario ,usuario):
    context.page = context.page.iniciar_sesion(context.usuarios[tipo_usuario][usuario], context.usuarios['contrasena'])


@when('va a crear solicitud de contratacion desde bandeja de entrada')
def step_imp(context):
    context.page = context.page.menu.menu_crear_solicitud_contratacion()


@when('crea la solicitud de contratacion')
def step_imp(context):
    context.page = context.page.crear_solicitud_contratacion()
    DataManager.set_numero_sco(context.page.obtener_numero_sco())


@when('completa indices de solicitud de contratacion')
def step_imp(context):
    context.page = context.page.indice_informacion_basica()
    context.page = context.page.completar_informacion_basica()
    context.page = context.page.indice_items()
    context.page = context.page.completar_items()
    context.page = context.page.datos_obra()
    context.page = context.page.plan_de_obra()
    context.page = context.page.tabla_vnr()
    context.page = context.page.tabla_vnr_po()


@when('envia la solicitud de contratacion al analista')
def step_imp(context):
    context.page = context.page.enviar_analista()
    assert mensajes_exito.SCO_ENVIAR_ANALISTA == context.page.get_mensaje_exito(), context.page.get_mensaje_exito()
 # hasta aca es con el solicitante


@when('va a editar solicitud de contratacion desde bandeja de entrada')
def step_imp(context):
    context.page = context.page.menu.menu_buscar_solicitud_contratacion()
    context.page.buscar_solicitud_por_numero()
    context.page = context.page.editar_sco()
    context.page = context.page.informacion_presupuestaria_fuentes_internas()
    context.page = context.page.completar_imputaciones()


@when('completa autorizadores')
def step_imp(context):
    context.page = context.page.lista_autorizadores()
    context.page = context.page.seleccionar_autorizadores()


@when('envia la solicitud de contratacion a autorizar')
def step_imp(context):
    context.page = context.page.enviar_autorizar()
    assert mensajes_exito.SG_ENVIAR_AUTORIZADOR == context.page.mensaje_exito_envio_autorizar()


@when('busca la solicitud de contratacion')
def step_imp(context):
    context.page = context.page.menu.menu_buscar_solicitud_contratacion()
    context.page.buscar_solicitud_por_numero()


@when('autoriza la solicitud de contratacion')
def step_imp(context):
    context.page = context.page.autorizar_sco()
    assert mensajes_exito.SG_AUTORIZADA == context.page. mensaje_exito_autoriza()


@then('la solicitud de contratacion queda en estado {estado}')
def step_imp(context, estado):
    context.page = context.page.menu.menu_buscar_solicitud_contratacion()
    context.page.buscar_solicitud_por_numero()
    assert (context.page.get_estado() == estado), "Se esperaba {}, fue {}".format(estado, context.page.estado_sg())
