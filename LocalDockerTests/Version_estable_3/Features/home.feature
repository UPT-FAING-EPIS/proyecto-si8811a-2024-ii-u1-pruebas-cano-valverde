Feature: Visualización y filtrado de eventos destacados en la página principal

  @chrome
  Scenario: El usuario puede ver los eventos destacados al ingresar a la página principal en Chrome
    Given I am on the "Home" page
    Then I should see the list of featured events displayed automatically
    And each event should have a valid faculty or display a warning if the faculty is invalid

  @firefox
  Scenario: El usuario puede ver los eventos destacados al ingresar a la página principal en Firefox
    Given I am on the "Home" page
    Then I should see the list of featured events displayed automatically
    And each event should have a valid faculty or display a warning if the faculty is invalid

  @edge
  Scenario: El usuario puede ver los eventos destacados al ingresar a la página principal en Edge
    Given I am on the "Home" page
    Then I should see the list of featured events displayed automatically
    And each event should have a valid faculty or display a warning if the faculty is invalid

  @chrome
  Scenario Outline: El usuario puede filtrar eventos destacados por "<faculty>" en Chrome
    Given I am on the "Home" page
    When I select the "<faculty>" from the filter dropdown on the Home page
    Then I should see featured events filtered by "<faculty>"
    And each event should have a valid faculty or display a warning if the faculty is invalid

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
  Scenario Outline: El usuario puede filtrar eventos destacados por "<faculty>" en Firefox
    Given I am on the "Home" page
    When I select the "<faculty>" from the filter dropdown on the Home page
    Then I should see featured events filtered by "<faculty>"
    And each event should have a valid faculty or display a warning if the faculty is invalid

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
  Scenario Outline: El usuario puede filtrar eventos destacados por "<faculty>" en Edge
    Given I am on the "Home" page
    When I select the "<faculty>" from the filter dropdown on the Home page
    Then I should see featured events filtered by "<faculty>"
    And each event should have a valid faculty or display a warning if the faculty is invalid

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
  Scenario: No hay eventos disponibles para una facultad seleccionada en la página principal en Chrome
    Given I am on the "Home" page
    When I select the "Facultad de Ciencias de la Salud" from the filter dropdown
    Then I should see a message that says "No hay eventos disponibles en este momento." on the Home page

  @firefox
  Scenario: No hay eventos disponibles para una facultad seleccionada en la página principal en Firefox
    Given I am on the "Home" page
    When I select the "Facultad de Ciencias de la Salud" from the filter dropdown
    Then I should see a message that says "No hay eventos disponibles en este momento." on the Home page

  @edge
  Scenario: No hay eventos disponibles para una facultad seleccionada en la página principal en Edge
    Given I am on the "Home" page
    When I select the "Facultad de Ciencias de la Salud" from the filter dropdown
    Then I should see a message that says "No hay eventos disponibles en este momento." on the Home page
