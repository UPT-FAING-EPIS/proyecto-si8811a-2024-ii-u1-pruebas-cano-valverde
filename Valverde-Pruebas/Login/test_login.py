# test_login.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger()

def test_login_functionality(driver):
    driver.get('http://localhost:5173')
    
    # Espera a que el botón de login esté presente y sea clickeable
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-blue-600")))
    logger.info("Botón 'Iniciar con Microsoft' encontrado y clickeable.")
    
    # Haz clic en el botón y verifica que la acción de login se realiza correctamente
    login_button.click()
    logger.info("Botón 'Iniciar con Microsoft' clickeado.")
    
    # Verifica que el mensaje de alerta aparece
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == "Iniciar sesión con Microsoft", "El mensaje de alerta no es el esperado."
    logger.info("Mensaje de alerta verificado.")
    
    alert.accept()
    logger.info("Alerta aceptada.")
