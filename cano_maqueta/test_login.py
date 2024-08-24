import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("file:///C:/Users/HP/pruebaSelenium/login.html")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_success(self):
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")

        username_field.send_keys("testuser")
        password_field.send_keys("password123")
        password_field.send_keys(Keys.RETURN)

        time.sleep(2)
        success_text = self.driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(success_text, "Success!")

if __name__ == "__main__":
    unittest.main(verbosity=2)
