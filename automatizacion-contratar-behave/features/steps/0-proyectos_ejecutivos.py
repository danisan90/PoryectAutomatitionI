from behave import *
from page_objects.MENU.menu_ciudadano import MenuCiudadano
from config.parameters import Parameters
from generated_data.data_manager import DataManager
from page_objects.MENU.menu import MenuPageObject


@when('va a crear proyecto ejectuivo desde bandeja de entrada')
def step_imp(context):
    context.page = context.page.menu.menu_proyecto_obra()
    context.page = context.page.nuevo_proyecto()


@when('crea un proyecto ejecutivo')
def step_imp(context):
    context.page = context.page.ingresar_items()
