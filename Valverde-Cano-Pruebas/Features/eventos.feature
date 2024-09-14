Feature: Visualización de eventos

  Scenario: El usuario puede ver los eventos después de hacer clic en el botón "Ver Eventos"
    Given I am on the "Eventos" page
    When I click the "Ver Eventos" button
    Then I should see the events section
    And I should see at least one event listed

  Scenario Outline: El usuario puede filtrar eventos por "<faculty>"
    Given I am on the "Eventos" page
    When I select the "<faculty>" from the filter dropdown
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

  Scenario: El usuario puede activar el filtro de eventos vigentes
    Given I am on the "Eventos" page
    When I check the "Mostrar solo eventos vigentes" checkbox
    Then I should see only ongoing or future events
