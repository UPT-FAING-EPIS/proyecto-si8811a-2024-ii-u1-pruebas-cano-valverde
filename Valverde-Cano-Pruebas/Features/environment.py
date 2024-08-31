from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def before_all(context):
    # Configura el WebDriver de Chrome utilizando webdriver_manager y Service
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)

def after_all(context):
    # Verifica que el driver esté definido antes de intentar cerrarlo
    if hasattr(context, 'driver'):
        context.driver.quit()
