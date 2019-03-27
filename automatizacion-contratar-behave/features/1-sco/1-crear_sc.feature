@sco
Feature: Crear solicitud de contratacion
  Como usuario solicitante UE ir a crear solicitud de gasto

  Scenario: Crear solicitud de contratacion
    Given existe un proyecto de obra
    And el usuario se encuentra en el home
    When inicia sesion con usuario solicitante solicitanteSCO
    And va a crear solicitud de contratacion desde bandeja de entrada
    And crea la solicitud de contratacion
    And completa indices de solicitud de contratacion
    And envia la solicitud de contratacion al analista
    Then la solicitud de contratacion queda en estado Pendiente Análisis

  @analista
  Scenario: Analizar solicitud de contratacion
    Given el usuario se encuentra en el home
    When inicia sesion con usuario analista analistaSCO
    And va a editar solicitud de contratacion desde bandeja de entrada
    And completa autorizadores
    And envia la solicitud de contratacion a autorizar
    Then la solicitud de contratacion queda en estado pendienteAutorizacion

  @autoriza
  Scenario: Autorizar solicitud de contratacion
    Given el usuario se encuentra en el home
    When inicia sesion con usuario autorizador autorizadorSCO
    When busca la solicitud de contratacion
    And autoriza la solicitud de contratacion
    Then la solicitud de contratacion queda en estado autorizada