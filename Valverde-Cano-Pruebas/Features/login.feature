Feature: Funcionalidad del login

  Scenario: Inicio de Sesion existoso con Microsoft
    Given I am on the homepage
    When I click the "Iniciar con Microsoft" button
    Then I should see an alert with the message "Iniciar sesión con Microsoft"