import random
import secrets

import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from data import Urls
from data import Creds


@pytest.fixture
def driver():
    """Запуск и закрытие браузера"""
    browser = webdriver.Chrome()
    browser.get(Urls.MAIN_PAGE)
    yield browser
    browser.quit()


@pytest.fixture
def authorization(driver, locators, creds):
    """фикстура авторизации"""
    driver.find_element(By.XPATH, locators.get("email_field")).send_keys(creds.get("user_login"))  # Найди поле "Email" и заполни его
    time.sleep(2)
    driver.find_element(By.XPATH, locators.get("password_field")).send_keys(creds.get("user_password"))  # Найди поле "Пароль" и заполни его
    time.sleep(2)
    driver.find_element(By.XPATH, locators.get("login_button")).click()  # Найди кнопку "Войти" и кликни по ней


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