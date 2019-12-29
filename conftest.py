import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language",
                     action="store",
                     default="es",
                     help="Choose language: es, fr etc")


@pytest.fixture()
def browser(request):
    language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option("prefs",
                                    {"intl.accept_languages": language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()