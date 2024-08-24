from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Firefox()  # Asegúrate de tener el WebDriver correspondiente
    yield driver
    driver.quit()

def test_page_title(driver):
    driver.get('http://www.google.com')
    assert 'Google' in driver.title
