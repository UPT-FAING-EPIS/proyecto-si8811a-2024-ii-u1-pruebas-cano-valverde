import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException

class ButtonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://localhost:5173/")  # Asegúrate de que la URL sea correcta para tu entorno local

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_button_click(self):
        # Encuentra el botón por su ID
        button = self.driver.find_element(By.ID, "myButton")
        
        # Haz clic en el botón
        button.click()

        try:
            # Espera hasta que la alerta esté presente
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()  # Cierra la alerta

            # Verifica que el texto de la alerta sea el esperado
            self.assertEqual(alert_text, "Iniciar sesión con Microsoft")

        except NoAlertPresentException:
            self.fail("No se encontró una alerta cuando se esperaba una.")
        except TimeoutException:
            self.fail("La alerta no apareció a tiempo.")
        except Exception as e:
            self.fail(f"Error durante la prueba: {e}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
