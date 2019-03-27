@proyectoej
Feature: Crear proyecto ejecutivo
  Como usuario comprador crear proyecto ejecutivo

   Scenario: Crear proyecto ejecutivo
    Given el usuario se encuentra en el home
    When inicia sesion con usuario solicitante solicitanteSCO
    And va a crear proyecto ejectuivo desde bandeja de entrada
    And crea un proyecto ejecutivo

