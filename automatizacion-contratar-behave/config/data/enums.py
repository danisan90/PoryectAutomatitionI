from enum import Enum


class TipoUsuario(Enum):
    comprador = 'solicitante'
    proveedor = 'proveedor'


class EtapaInformacionBasica(Enum):
    etapaUnica = 0
    etapaMultiple = 1


class SistemaDeContratacion(Enum):
    porUnidadDeMedida = "UnidadMedida"
    porAjusteAlzado = "AjusteAlzado"
    porCosteYCostas = "CosteCostas"
    porOtrosSistemas = "Otros"


class TipoDeAdjudicacion(Enum):
    parcial = 0
    total = 1


class TipoDeCotizacion(Enum):
    parcial = 0
    total = 1


class Moneda(Enum):
    dolarEstadounidense = "Dolar Estadounidense"
    real = "Real"
    euro = "Euro"
    pesoArgentino = "Peso Argentino"
    libraEsterlina = "Libra Esterlina"


class TipoDeDias(Enum):
    diasHabiles = "Días hábiles"



class Lugarderecepciondedocumentacionfisica(Enum):
    direccion = "25 de Mayo 101. 2do Piso Oficina 228. Ciudad Autónoma de Buenos Aires"


class TipodeDocumento(Enum):
    resolucion = "Resolución"
    circular = "Circular CONTRAT.AR"
    pliego = "Pliego"


class UnidaddeTiempo(Enum):
    diasHabiles = "Días hábiles"
    diasCorridos = "Días corridos"
    anios = "Años"
    meses = "Meses"
