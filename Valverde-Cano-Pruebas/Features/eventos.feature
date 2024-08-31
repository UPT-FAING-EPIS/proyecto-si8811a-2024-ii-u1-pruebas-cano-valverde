Feature: Visualizacion de eventos

  Scenario: El usuario puede ver los eventos después de hacer clic en el botón
    Given I am on the "Eventos" page
    When I click the "Ver Eventos" button
    Then I should see the events section
    And I should see at least one event listed