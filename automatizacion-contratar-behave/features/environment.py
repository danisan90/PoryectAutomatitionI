from selenium import webdriver
from config.parameters import Parameters


def before_all(context):
    context.driver = webdriver.Chrome()
    Parameters.execute_file("sin_modalidad.py")
    context.ambiente = Parameters.get_ambiente()
    context.usuarios = Parameters.get_usuarios()
    context.sco = Parameters.get_sco()
    context.pliego = Parameters.get_pliego()
