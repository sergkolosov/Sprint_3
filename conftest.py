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


@pytest.fixture
def random_email():
    """генератор email"""
    length_email = 6
    return f"{secrets.token_hex(length_email)}@yandex.ru"


@pytest.fixture
def random_password():
    """генератор password"""
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length_password = 6
    password = ''
    for i in range(length_password):
        password += random.choice(chars)
    return password