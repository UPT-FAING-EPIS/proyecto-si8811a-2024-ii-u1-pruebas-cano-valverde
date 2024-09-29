import pytest
from webdriver_config import get_driver  # Asegúrate de que la importación esté correcta

@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption("browser")
    driver = get_driver(browser)
    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")
