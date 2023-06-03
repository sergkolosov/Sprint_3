import random
import secrets

import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from data import Urls
from data import Creds
from locator import Locators


@pytest.fixture
def driver():
    """Запуск и закрытие браузера"""
    browser = webdriver.Chrome()
    browser.get(Urls.MAIN_PAGE)
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    """Авторизация"""
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(*Creds.USER_EMAIL)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(*Creds.USER_PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
