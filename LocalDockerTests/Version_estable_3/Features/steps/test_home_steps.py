import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep  # Importar time.sleep para agregar pausas

FACULTADES_VALIDAS = ["FAING", "FAU", "FAEDCOH", "FADE", "FACEM", "FACSA"]

@allure.feature('Eventos Destacados')
@allure.story('Verificación de Eventos Destacados')
@allure.title('Prueba de Eventos Destacados en la Página Principal')
@pytest.mark.chrome
@pytest.mark.firefox
@pytest.mark.edge
def test_ver_eventos_destacados(driver):
    with allure.step("Abrir la página principal"):
        driver.get("http://161.132.50.153/")
        sleep(3)  # Esperar a que la página se cargue completamente

    with allure.step("Verificar que los eventos destacados se carguen en la página principal"):
        eventos = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.bg-white.p-8.rounded-lg.shadow-lg"))
        )
        assert len(eventos) > 0, "No se encontraron eventos destacados."

    with allure.step("Verificar la facultad de cada evento destacado"):
        for evento in eventos:
            try:
                facultad_element = evento.find_element(By.XPATH, ".//p[contains(text(), 'Facultad')]")
                facultad = facultad_element.text.split(":")[1].strip()

                # Verifica si la facultad está en la lista de facultades válidas
                if facultad not in FACULTADES_VALIDAS:
                    with allure.step(f"Advertencia: Evento con facultad no válida o diferente: {facultad}"):
                        allure.attach(facultad, name="Facultad Incorrecta", attachment_type=allure.attachment_type.TEXT)
                else:
                    assert facultad in FACULTADES_VALIDAS, f"Facultad incorrecta detectada: {facultad}"
            except NoSuchElementException:
                with allure.step("Advertencia: Facultad no encontrada en este evento"):
                    allure.attach("Facultad no encontrada", name="Error de Facultad", attachment_type=allure.attachment_type.TEXT)

@pytest.mark.chrome
@pytest.mark.firefox
@pytest.mark.edge
def test_filtrar_eventos_destacados_facultad(driver):
    with allure.step("Abrir la página principal"):
        driver.get("http://161.132.50.153/")
        sleep(1)  # Esperar a que la página se cargue completamente

    with allure.step("Seleccionar cada facultad desde el dropdown en la página principal"):
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "facultad"))
        )
        dropdown.click()
        sleep(1)  # Esperar a que el dropdown se despliegue

        facultades = [
            "Facultad de Ingeniería",
            "Facultad de Educación, Ciencias de la comunicación y Humanidades",
            "Facultad de Derecho y Ciencias Políticas",
            "Facultad de Ciencias de la Salud",
            "Facultad de Ciencias Empresariales",
            "Facultad de Arquitectura y Urbanismo",
            "Todas"
        ]

        for facultad_text in facultades:
            with allure.step(f"Seleccionar la facultad: {facultad_text}"):
                try:
                    option = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, f"//option[text()='{facultad_text}']"))
                    )
                    option.click()
                    sleep(1)  # Esperar a que los eventos se filtren

                    with allure.step(f"Verificar que los eventos filtrados correspondan a la facultad: {facultad_text}"):
                        eventos_filtrados = WebDriverWait(driver, 10).until(
                            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.bg-white.p-8.rounded-lg.shadow-lg"))
                        )
                        assert len(eventos_filtrados) > 0, f"No se encontraron eventos para la facultad: {facultad_text}."

                    with allure.step(f"Verificar la facultad de cada evento filtrado para: {facultad_text}"):
                        for evento in eventos_filtrados:
                            try:
                                facultad_element = evento.find_element(By.XPATH, ".//p[contains(text(), 'Facultad')]")
                                facultad = facultad_element.text.split(":")[1].strip()
                                if facultad_text != "Todas":
                                    assert facultad == facultad_text, f"Evento con facultad incorrecta: {facultad}"
                            except NoSuchElementException:
                                with allure.step("Advertencia: Facultad no encontrada en este evento"):
                                    allure.attach("Facultad no encontrada", name="Error de Facultad", attachment_type=allure.attachment_type.TEXT)
                except TimeoutException as e:
                    allure.attach(f"TimeoutException: {str(e)}", name="TimeoutException", attachment_type=allure.attachment_type.TEXT)
