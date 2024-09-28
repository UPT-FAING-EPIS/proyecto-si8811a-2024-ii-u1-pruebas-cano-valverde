from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def get_driver(browser_name):
    options = None
    if browser_name == "chrome":
        options = ChromeOptions()
        options.set_capability('se:name', 'chrome')
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_capability('se:name', 'firefox')
    elif browser_name == "edge":
        options = EdgeOptions()
        options.set_capability('se:name', 'edge')

    return webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',  # Asegúrate de usar el endpoint correcto
        options=options
    )
