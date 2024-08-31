from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger()

@given('I am on the "Eventos" page')
def step_given_on_eventos_page(context):
    context.driver.get('http://localhost:5173/Eventos')
    logger.info("Página de Eventos cargada.")

@when('I click the "Ver Eventos" button')
def step_when_click_view_events_button(context):
    view_events_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.bg-yellow-500"))
    )
    view_events_button.click()
    logger.info("Botón 'Ver Eventos' clickeado.")

@then('I should see the events section')
def step_then_verify_events_section(context):
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.ID, "events")))
    logger.info("Sección de eventos visible.")

@then('I should see at least one event listed')
def step_then_verify_events_listed(context):
    events = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.bg-white"))
    )
    assert len(events) > 0, "No se encontraron eventos en la página tras hacer clic en 'Ver Eventos'."
    logger.info(f"Se encontraron {len(events)} eventos.")
