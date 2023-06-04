import pytest

from selenium import webdriver
from data import Urls


@pytest.fixture
def driver():
    """Запуск и закрытие браузера"""
    browser = webdriver.Chrome()
    browser.get(Urls.MAIN_PAGE)
    yield browser
    browser.quit()
