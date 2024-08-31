import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException

class ButtonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://localhost:5173/eventos")  # Asegúrate de que la URL sea correcta para tu entorno local

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_url_and_link(self):
        try:
            # Encuentra el enlace por su texto
            link = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Ver Eventos"))
            )
            
            # Guarda la URL original para verificar el cambio
            original_url = self.driver.current_url

            # Haz clic en el enlace
            link.click()

            # Verifica que la URL haya cambiado
            WebDriverWait(self.driver, 10).until(
                lambda d: d.current_url == "http://localhost:5173/eventos#events"
            )

            # Verifica la presencia de los textos en la nueva página
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Eventos Destacados")
            )
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Concurso de Poesía")
            )

        except UnexpectedAlertPresentException:
            self.fail("Se mostró una alerta inesperada.")
        except TimeoutException:
            self.fail("Tiempo de espera agotado.")
        except Exception as e:
            self.fail(f"Error durante la prueba: {e}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
