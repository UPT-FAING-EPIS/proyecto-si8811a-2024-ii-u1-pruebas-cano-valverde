import time
import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Elimina cualquier importación de ScreenRecorder

# No necesitas importar ScreenRecorder aquí


logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

@given('I am on the "Eventos" page')
def step_given_on_eventos_page(context):
    context.driver.get('http://localhost:5173/eventos')
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.bg-yellow-500'))
    )
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
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "events"))
    )
    logger.info("Sección de eventos visible.")

@then('I should see at least one event listed')
def step_then_verify_events_listed(context):
    events = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.bg-white"))
    )
    assert len(events) > 0, "No se encontraron eventos en la página tras hacer clic en 'Ver Eventos'."
    logger.info(f"Se encontraron {len(events)} eventos.")

@when('I select the "{faculty}" from the filter dropdown')
def step_when_select_faculty(context, faculty):
    facultad_dropdown = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "facultad"))
    )
    facultad_dropdown.click()

    # Selecciona la opción de la facultad
    option = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//option[text()='{faculty}']"))
    )
    option.click()
    logger.info(f"Facultad seleccionada: {faculty}")

@then('I should see events filtered by "{faculty}"')
def step_then_verify_filtered_events(context, faculty):
    # Mapeamos las facultades a sus abreviaturas
    faculty_map = {
        'Facultad de Ingeniería': 'FAING',
        'Facultad de Educación, Ciencias de la Comunicación y Humanidades': 'FAEDCOH',
        'Facultad de Derecho y Ciencias Políticas': 'FADE',
        'Facultad de Ciencias de la Salud': 'FACSA',
        'Facultad de Ciencias Empresariales': 'FACEM',
        'Facultad de Arquitectura y Urbanismo': 'FAU',
        'Todas': 'Todas'
    }
    faculty_abbr = faculty_map.get(faculty)
    assert faculty_abbr, f"No se encontró la abreviación para la facultad: {faculty}"

    events = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.bg-white"))
    )

    found = False
    for event in events:
        try:
            facultad_element = event.find_element(By.XPATH, ".//p[strong[contains(text(), 'Facultad:')]]")
            facultad_text = facultad_element.text.strip()
            # Extraemos la abreviatura de la facultad
            facultad_nombre = facultad_text.replace('Facultad:', '').strip()
            logger.info(f"Facultad del evento: {facultad_nombre}")
            if facultad_nombre == faculty_abbr or faculty_abbr == "Todas":
                found = True
                continue
            else:
                # Si encontramos un evento que no pertenece a la facultad seleccionada, fallamos la prueba
                assert False, f"Se encontró un evento que no pertenece a la facultad seleccionada: {facultad_nombre}"
        except Exception as e:
            logger.error(f"Error al obtener la facultad del evento: {e}")
            assert False, "No se pudo obtener la facultad del evento."

    assert found, f"No se encontraron eventos para la facultad seleccionada: {faculty}"
    logger.info(f"Todos los eventos pertenecen a la facultad: {faculty}")

@when('I check the "Mostrar solo eventos vigentes" checkbox')
def step_when_check_vigentes(context):
    vigentes_checkbox = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "vigentes"))
    )
    vigentes_checkbox.click()
    logger.info("Checkbox de eventos vigentes activado.")

@then('I should see only ongoing or future events')
def step_then_verify_vigentes(context):
    current_date = time.strptime(time.strftime("%d/%m/%Y"), "%d/%m/%Y")
    events = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.bg-white"))
    )

    found_future_events = False
    for event in events:
        try:
            fecha_termino_element = event.find_element(By.XPATH, ".//p[strong[contains(text(), 'Fecha Termino:')]]")
            fecha_termino_text = fecha_termino_element.text.strip()
            # Extraemos la fecha de término
            event_end_date_str = fecha_termino_text.replace('Fecha Termino:', '').strip()
            event_end_date = time.strptime(event_end_date_str, "%d/%m/%Y")
            logger.info(f"Fecha Término del evento: {event_end_date_str}")
            # Comparamos la fecha de término con la fecha actual
            if event_end_date >= current_date:
                found_future_events = True
                continue
            else:
                # Si encontramos un evento que ya terminó, fallamos la prueba
                assert False, f"Se encontró un evento que ya terminó: {event_end_date_str}"
        except Exception as e:
            logger.error(f"Error al obtener la fecha de término del evento: {e}")
            assert False, "No se pudo obtener la fecha de término del evento."

    assert found_future_events, "No se encontraron eventos futuros o en curso."
    logger.info("Todos los eventos son vigentes o futuros.")
