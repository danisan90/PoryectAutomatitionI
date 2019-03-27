import json
import os


class Parameters:

    __json_file = None

    @classmethod
    def execute_file(cls, filename):
        """Si filename coincide con algún generador, lo ejecuta.
        filename -- nombre del archivo .py
        """
        try:
            cls.__json_file = None
            file = open(os.path.join(os.path.dirname(__file__), "generators\{}".format(filename)))
            exec(file.read())
            file.close()
            print("El archivo '{}.json' cargado correctamente.".format(os.path.splitext(filename)[0]))
        except FileExistsError:
            print("No se encontró el archivo {} en 'configs/generators/'" .format(filename))

    @classmethod
    def __load_json(cls):
        """Carga la variable si está vacía y la devuelve, sino sólo la devuelte."""
        if cls.__json_file is None:
            with open(os.path.join(os.path.dirname(__file__), 'JSONS\sin_modalidad.json'), encoding='utf-8') as file:
                cls.__json_file = json.load(file)
        return cls.__json_file

    @staticmethod
    def get_ambiente():
        """Devuelve los parametros de ambiente."""
        data = Parameters.__load_json()
        return data['ambiente']

    @staticmethod
    def get_usuarios():
        """Devuelve los parametros de usuarios."""
        data = Parameters.__load_json()
        return data['usuarios']

    #@staticmethod
    #def get_anexos():
        #    """Devuelve los parametros de anexos."""
        # data = Parameters.__load_json()
    # return data['anexos']

    @staticmethod
    def get_sco():
        """Devuelve los parametros de Solicitud de Gasto."""
        data = Parameters.__load_json()
        return data['sco']

    @staticmethod
    def get_nombres_po():
        """Devuelve los parametros de Solicitud de Gasto."""
        data = Parameters.__load_json()
        return data['nombres_po']

    @staticmethod
    def get_pliego():
        """Devuelve los parametros de Proceso de Compra."""
        data = Parameters.__load_json()
        return data['pliego']

    @staticmethod
    def get_proyectoEjecutivo():
        """Devuelve los parametros de Proceso de Compra."""
        data = Parameters.__load_json()
        return data['proyectoEjecutivo']

    # @staticmethod
        # def get_evaluacion():
        #   """Devuelve los parametros de Evaluación."""
        #  data = Parameters.__load_json()
    #  return data['EVALUACION']

    # @staticmethod
        # def get_orden_compra():
        #    """Devuelve los parametros de Orden de Compra."""
        #  data = Parameters.__load_json()
    #   return data['OC']
