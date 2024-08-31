from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger()

@given('I am on the homepage')
def step_given_on_homepage(context):
    context.driver.get('http://localhost:5173')
    logger.info("Página principal cargada.")

@when('I click the "Iniciar con Microsoft" button')
def step_when_click_login_button(context):
    login_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-blue-600"))
    )
    login_button.click()
    logger.info("Botón 'Iniciar con Microsoft' clickeado.")

@then('I should see an alert with the message "Iniciar sesión con Microsoft"')
def step_then_verify_alert(context):
    WebDriverWait(context.driver, 10).until(EC.alert_is_present())
    alert = context.driver.switch_to.alert
    assert alert.text == "Iniciar sesión con Microsoft", "El mensaje de alerta no es el esperado."
    logger.info("Mensaje de alerta verificado.")
    alert.accept()
    logger.info("Alerta aceptada.")
