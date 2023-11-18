import pytest
from base.network_settings import NetworkSettings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def get_chrome_options():
    options = Options()
    options.add_argument('headless')  # headless / chrome
    options.add_argument('--window-size=1920,1080')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


@pytest.fixture(scope='function')
def setup(get_webdriver, request):
    driver = get_webdriver
    url = 'https://example.com/'
    NetworkSettings.fast_wifi(driver)
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
