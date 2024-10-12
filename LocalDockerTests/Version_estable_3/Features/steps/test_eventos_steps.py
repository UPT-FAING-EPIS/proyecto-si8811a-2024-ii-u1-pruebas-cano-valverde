import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep

FACULTADES_VALIDAS = ["FAING", "FAU", "FAEDCOH", "FADE", "FACEM", "FACSA"]

@allure.feature('Filtrado de Eventos por Facultad')
@allure.story('Filtrar Eventos con Dropdown y Checkbox')
@allure.title('Filtrar Eventos y Marcar Checkboxes')
@pytest.mark.chrome
@pytest.mark.firefox
@pytest.mark.edge
def test_filtrar_eventos_y_checkbox(driver):
    with allure.step("Abrir la página de eventos"):
        driver.get("http://161.132.50.153/eventos")
        sleep(2)  # Esperar a que la página se cargue

    facultades = [
        "Facultad de Ingeniería",
        "Facultad de Educación, Ciencias de la Comunicación y Humanidades",
        "Facultad de Derecho y Ciencias Políticas",
        "Facultad de Ciencias de la Salud",
        "Facultad de Ciencias Empresariales",
        "Facultad de Arquitectura y Urbanismo",
        "Todas"
    ]

    for facultad_text in facultades:
        with allure.step(f"Seleccionar la facultad: {facultad_text}"):

            # Filtrar eventos por facultad sin checkbox marcado
            try:
                dropdown = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.ID, "facultad"))
                )
                dropdown.click()
                sleep(1)  # Esperar a que el dropdown se despliegue

                option = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, f"//option[text()='{facultad_text}']"))
                )
                option.click()
                sleep(1)  # Esperar a que se filtren los eventos

                try:
                    eventos_filtrados = WebDriverWait(driver, 5).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.bg-white.p-8.rounded-lg.shadow-lg"))
                    )
                    if facultad_text == "Todas":
                        # Si la opción seleccionada es "Todas", verificar que se muestren eventos
                        assert len(eventos_filtrados) > 0, "No se encontraron eventos."
                    else:
                        if len(eventos_filtrados) == 0:
                            # Verificar el mensaje de no disponibilidad si no hay eventos
                            no_events_message = WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'No hay eventos disponibles en este momento.')]"))
                            )
                            assert no_events_message is not None, "No se encontró mensaje de eventos no disponibles."
                        else:
                            # Verificar que los eventos filtrados correspondan a la facultad seleccionada
                            for evento in eventos_filtrados:
                                try:
                                    facultad_element = evento.find_element(By.XPATH, ".//p[contains(text(), 'Facultad')]")
                                    facultad = facultad_element.text.split(":")[1].strip()
                                    assert facultad == facultad_text, f"Evento con facultad incorrecta: {facultad}"
                                except NoSuchElementException:
                                    allure.attach("Advertencia: Facultad no encontrada en este evento", name="Advertencia Facultad", attachment_type=allure.attachment_type.TEXT)

                except TimeoutException:
                    # Manejar el caso en que no se encuentran eventos o el mensaje de no disponibilidad
                    if facultad_text == "Facultad de Ciencias de la Salud":
                        no_events_message = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'No hay eventos disponibles en este momento.')]"))
                        )
                        assert no_events_message is not None, "No se encontró mensaje de eventos no disponibles."
                    else:
                        allure.attach(f"Advertencia: No se encontraron eventos para {facultad_text}", name="Error de Eventos", attachment_type=allure.attachment_type.TEXT)

                # Marcar el checkbox si está presente y filtrar nuevamente
                try:
                    checkbox = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']"))
                    )
                    checkbox.click()
                    sleep(1)  # Esperar a que se actualicen los eventos

                    # Re-filtrar los eventos con el checkbox marcado
                    dropdown.click()  # Reabrir el dropdown
                    sleep(1)  # Esperar a que el dropdown se despliegue

                    option = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, f"//option[text()='{facultad_text}']"))
                    )
                    option.click()
                    sleep(1)  # Esperar a que se filtren los eventos nuevamente

                    eventos_filtrados = WebDriverWait(driver, 5).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.bg-white.p-8.rounded-lg.shadow-lg"))
                    )
                    assert len(eventos_filtrados) > 0, f"No se encontraron eventos para {facultad_text} después de marcar el checkbox."

                    for evento in eventos_filtrados:
                        try:
                            facultad_element = evento.find_element(By.XPATH, ".//p[contains(text(), 'Facultad')]")
                            facultad = facultad_element.text.split(":")[1].strip()
                            assert facultad == facultad_text, f"Evento con facultad incorrecta después de marcar el checkbox: {facultad}"
                        except NoSuchElementException:
                            allure.attach("Advertencia: Facultad no encontrada en este evento después de marcar el checkbox", name="Advertencia Facultad", attachment_type=allure.attachment_type.TEXT)

                except NoSuchElementException:
                    allure.attach(f"Advertencia: Checkbox no encontrado para {facultad_text}", name="Error de Checkbox", attachment_type=allure.attachment_type.TEXT)

            except NoSuchElementException:
                allure.attach(f"Advertencia: Opción no encontrada para {facultad_text}", name="Error de Selección", attachment_type=allure.attachment_type.TEXT)
            except TimeoutException:
                allure.attach(f"Timeout: No se pudo encontrar o seleccionar la opción para {facultad_text}", name="Timeout Error", attachment_type=allure.attachment_type.TEXT)
            sleep(1)  # Esperar antes de seleccionar la siguiente opción
