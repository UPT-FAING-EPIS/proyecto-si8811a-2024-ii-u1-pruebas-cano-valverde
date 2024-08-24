# test_eventos.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger()

def test_view_events_button(driver):
    driver.get('http://localhost:5173/Eventos')
    
    # Espera a que el botón "Ver Eventos" esté presente y sea clickeable
    view_events_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.bg-yellow-500")))
    logger.info("Botón 'Ver Eventos' encontrado y clickeable.")
    
    # Haz clic en el botón y verifica que la página de eventos se carga correctamente
    view_events_button.click()
    logger.info("Botón 'Ver Eventos' clickeado.")
    
    # Verifica que la página se desplaza a la sección de eventos
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "events")))
    logger.info("Página de eventos cargada.")
    
    # Verifica la presencia de eventos
    events = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.bg-white")))
    assert len(events) > 0, "No se encontraron eventos en la página tras hacer clic en 'Ver Eventos'."
    logger.info(f"Se encontraron {len(events)} eventos.")
