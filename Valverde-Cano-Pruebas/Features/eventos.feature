Feature: Visualización de eventos en la página de eventos

  @chrome
  Scenario: El usuario puede ver los eventos después de filtrar en la página de eventos en Chrome
    Given I am on the "Eventos" page
    When I select "Facultad de Ingeniería" from the filter dropdown
    Then I should see a list of events displayed
    And each event should have a valid faculty

  @firefox
  Scenario: El usuario puede ver los eventos después de filtrar en la página de eventos en Firefox
    Given I am on the "Eventos" page
    When I select "Facultad de Ingeniería" from the filter dropdown
    Then I should see a list of events displayed
    And each event should have a valid faculty

  @edge
  Scenario: El usuario puede ver los eventos después de filtrar en la página de eventos en Edge
    Given I am on the "Eventos" page
    When I select "Facultad de Ingeniería" from the filter dropdown
    Then I should see a list of events displayed
    And each event should have a valid faculty

  @chrome
  Scenario Outline: El usuario puede filtrar eventos por "<faculty>" en Chrome
    Given I am on the "Eventos" page
    When I select "<faculty>" from the filter dropdown
    Then I should see events filtered by "<faculty>"

    Examples:
      | faculty                                                                      |
      | Facultad de Ingeniería                                                       |
      | Facultad de Educación, Ciencias de la Comunicación y Humanidades             |
      | Facultad de Derecho y Ciencias Políticas                                     |
      | Facultad de Ciencias de la Salud                                             |
      | Facultad de Ciencias Empresariales                                           |
      | Facultad de Arquitectura y Urbanismo                                         |
      | Todas                                                                        |

  @firefox
  Scenario Outline: El usuario puede filtrar eventos por "<faculty>" en Firefox
    Given I am on the "Eventos" page
    When I select "<faculty>" from the filter dropdown
    Then I should see events filtered by "<faculty>"

    Examples:
      | faculty                                                                      |
      | Facultad de Ingeniería                                                       |
      | Facultad de Educación, Ciencias de la Comunicación y Humanidades             |
      | Facultad de Derecho y Ciencias Políticas                                     |
      | Facultad de Ciencias de la Salud                                             |
      | Facultad de Ciencias Empresariales                                           |
      | Facultad de Arquitectura y Urbanismo                                         |
      | Todas                                                                        |

  @edge
  Scenario Outline: El usuario puede filtrar eventos por "<faculty>" en Edge
    Given I am on the "Eventos" page
    When I select "<faculty>" from the filter dropdown
    Then I should see events filtered by "<faculty>"

    Examples:
      | faculty                                                                      |
      | Facultad de Ingeniería                                                       |
      | Facultad de Educación, Ciencias de la Comunicación y Humanidades             |
      | Facultad de Derecho y Ciencias Políticas                                     |
      | Facultad de Ciencias de la Salud                                             |
      | Facultad de Ciencias Empresariales                                           |
      | Facultad de Arquitectura y Urbanismo                                         |
      | Todas                                                                        |

  @chrome
  Scenario: No hay eventos disponibles para una facultad seleccionada en Chrome
    Given I am on the "Eventos" page
    When I select "Facultad de Ciencias de la Salud" from the filter dropdown
    Then I should see a message that says "No hay eventos disponibles en este momento."

  @firefox
  Scenario: No hay eventos disponibles para una facultad seleccionada en Firefox
    Given I am on the "Eventos" page
    When I select "Facultad de Ciencias de la Salud" from the filter dropdown
    Then I should see a message that says "No hay eventos disponibles en este momento."

  @edge
  Scenario: No hay eventos disponibles para una facultad seleccionada en Edge
    Given I am on the "Eventos" page
    When I select "Facultad de Ciencias de la Salud" from the filter dropdown
    Then I should see a message that says "No hay eventos disponibles en este momento."
