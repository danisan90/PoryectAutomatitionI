import os
import json

from config.data.enums import EtapaInformacionBasica, SistemaDeContratacion, TipoDeAdjudicacion, TipoDeCotizacion,\
                                Moneda,TipoDeDias, Lugarderecepciondedocumentacionfisica, TipodeDocumento, UnidaddeTiempo

"""configuracion para sco"""

__data = {

    "ambiente":
        {
            "url": "http://10.2.1.86:8190"
        },
    "usuarios":
        {

            "solicitante": {
                "solicitanteSCO": "EMICHELENA"
            },
            "analista": {
                "analistaSCO": "EMICHELENA"
            },
            "autorizador": {
                "autorizadorSCO": "EMICHELENA"
            },
             "gestor": {
                "gestorPliego": "EMICHELENA"
            },
            "contrasena": "12345678"
        },
    "proyectoEjecutivo":
        {
            "NOMBREPROYECTOEJECUTIVO": "PROYECTO DE AUTOMATIZACION",
            #ACA ES DONDE TENES QUE DEFINIR LA CANTIDAD DE RUBROS QUE QUERES QUE EL PE TENGA :)
            "nombrerubro": ["rubro uno", "rubro 2", "rubro 3", "rubro 4", "rubro 5", "rubro 6"],
            "NOMBREITEM": "UN ITEM"
        },
    "sco":
        {
            "NOMBRE": "Marzo 8/3",
            "OBJETO": "Objeto de la solicitud de contratacion269",
            "TIPO": "Obra",  # Puede tener los valores: Obra, Consultoría Más Obra,
            "ANALISTA_USERNAME": "EMICHELENA",
            "UNIDAD_SOLICITANTE": "Organismo solicitante",
            "PORCENTAJE_AF": "10",
            "RUTA_ANEXO": "T:\SEAC\Verificar caracteres.doc",

            "tieneAnticipoFinanciero": True,
            "CODIGO_ITEMS": ["2.1.1-2124.6", "2.1.1-2124.7", "2.1.1-2124.5", "2.1.1-2124.1"],
            "NOMBRE_FO": ["FO uno", "FO dos", "FO tres", "FO cuatro"],
            "CANTIDAD": "1",
            "PRECIO_UNITARIO": "100",
            "FECHA_PREP_OFIC": "04/01/2019",
            "LATITUD": "-25.321456",
            "LONGITUD": "-11.254123",
            "NOMBRE_TABLA": "Tabla 1",
            "PRODUCTO": "Productos químicos",
            "PORCENTAJE": "100"

        },
    "pliego": {
            # Crear Pliego
            "NOMBREOBRA": "Pliego automatizado marzo12-7oBRA",
            "TIPODECONTRATACION": "Obra",
            # Completar Info Basica Pliego
            "tipoEtapa": EtapaInformacionBasica.etapaUnica.value,
            "sistemaDeContratacion": [SistemaDeContratacion.porUnidadDeMedida.value],
            "tipoadjudicacion": TipoDeAdjudicacion.total.value,
            "tipodecotizacion": TipoDeCotizacion.total.value,
            "moneda": Moneda.pesoArgentino.value,
            "plazoMantenimientoDePropuesta":
                                            {"CANTIDADDEDIAS":"30", "tipodedias":TipoDeDias.diasHabiles.value},
            "direccion": Lugarderecepciondedocumentacionfisica.direccion.value,
            "actoadministrativosade": TipodeDocumento.pliego.value,
            "anio": "2019",
            "reparticion": "ONC#JGM",
            "numero": "53829205",
            #requisitos minimos"
            "requisitoseconomicos": "Requisitos económicos y financieros",
            "requisitostecnicos": "Requisitos técnicos",
            "requisitosadministrativos": "Requisitos administrativos",
            "garantiadecumplimientodecontrato": "6",
            "cantidaddias":  "10",
            "diasduracionobra": "1",
            "unidaddetiempo": UnidaddeTiempo.anios.value,
            # Supervisor
            "supervisor": "EMICHELENA",
            # Evaluadores
            "evaluadores": ["EV Uno Proceso de Compras",
                            "EV Dos Proceso de Compras",
                            "EV Tres Proceso de Compras"],
            "anoDeclaracionJurada": "2015",
            "numeroDeclaracionJurada": "1",
            "reparticionDeclaracionJurada": "1",

        },

    "nombres_po":
        ["Proyecto uno", "Proyecto dos", "Proyecto tres", "Proyecto cuatro"]

}

try:
    with open(os.path.join(os.path.dirname(__file__), r'JSONS\sin_modalidad.json'), 'w', encoding='utf-8') as file:
        json.dump(__data, file, indent=4, ensure_ascii=False)
        print("El archivo 'sin_modalidad.json' generado correctamente.")
except Exception as e:
    print("Error al intentar ejectuar 'sin_modalidad.py':", e)
