from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import pytest

@pytest.fixture(scope="session", params=["chrome", "firefox", "edge"])
def driver(request):
    browser = request.param
    
    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.set_capability('se:recordVideo', True)
        driver = webdriver.Remote(
            command_executor='http://localhost:4444',
            options=chrome_options
        )
    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.set_capability('se:recordVideo', True)
        driver = webdriver.Remote(
            command_executor='http://localhost:4444',
            options=firefox_options
        )
    elif browser == "edge":
        edge_options = EdgeOptions()
        edge_options.set_capability('se:recordVideo', True)
        driver = webdriver.Remote(
            command_executor='http://localhost:4444',
            options=edge_options
        )

    driver.maximize_window()
    yield driver
    driver.quit()
