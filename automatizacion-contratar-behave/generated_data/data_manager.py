import os
import json


class DataManager:

    @staticmethod
    def load_json():
        try:
            with open(os.path.join(os.path.dirname(__file__), 'data.json'), encoding='utf-8') as file:
                return json.load(file)
        except Exception as e:
            print("Error al intentar leer 'data.json':", e)

    @staticmethod
    def save_json(data):
        try:
            with open(os.path.join(os.path.dirname(__file__), 'data.json'), 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        except Exception as e:
            print("Error al intentar guardar en 'data.json':", e)

    @staticmethod
    def set_numero_sco(numero):
        data = DataManager.load_json()
        data['numeroSCO'] = numero
        DataManager.save_json(data)

    @staticmethod
    def get_numero_sco():
        data = DataManager.load_json()
        return data['numeroSCO']


    @staticmethod
    def set_numero_pc(numeropc):
        data = DataManager.load_json()
        data['numeroPC'] = numeropc
        DataManager.save_json(data)

    @staticmethod
    def get_numero_pc():
        data = DataManager.load_json()
        return data['numeroPC']
