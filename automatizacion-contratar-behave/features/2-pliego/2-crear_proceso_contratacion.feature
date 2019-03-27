@pliego
Feature: Crear y supervisar proceso de contratacion
  Como usuario gestor de compra crear proceso de contratacion y enviarlo al supervisor
  Como usuario supervisor autorizar proceso

  Scenario: Crear proceso de contratacion
    Given el usuario se encuentra en el home
    When inicia sesion con usuario gestor gestorPliego
    And crea un proceso de contratacion
    And completa indices del pliego
    # And envia el proceso de compra al supervisor
    # Then el proceso de compra queda en estado pendienteSupervision