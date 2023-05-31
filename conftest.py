import random
import secrets

import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def creds():
    """URL используемых страниц и креды к тестам авторизации"""
    creds = {
        'project_stand_main': 'https://stellarburgers.nomoreparties.site/',  # Главная страница стенда
        'project_stand_register': 'https://stellarburgers.nomoreparties.site/register',  # Страница регистрации стенда
        'project_stand_forgot_password': 'https://stellarburgers.nomoreparties.site/forgot-password',  # Страница регистрации стенда
        'user_name': 'Serg',
        'user_login': 'sergkolosov1071@yandex.ru',
        'user_password': 'mypassword1071'
    }
    return creds


@pytest.fixture
def locators():
    """Библиотека локаторов"""
    locators = {
        "registration_name": "//fieldset[1]/div/div/input",   # поле "Имя" на странице регистрации
        "registration_email": "//fieldset[2]/div/div/input",   # поле "Email" на странице регистрации
        "registration_password": "//fieldset[3]/div/div/input",   # поле "пароль" на странице регистрации
        "email_field": "//input[@name='name']",   # поле "Email" на странице авторизации
        "password_field": "//input[@name='Пароль']",  # поле "пароль" на странице авторизации
        "password_error": "//p[@class='input__error text_type_main-default']",  # сообщение об ошибке
        "registration_button": "//button[contains(text(),'Зарегистрироваться')]",  # кнопка "Зарегистрироваться"
        "login_account_button": "//button[contains(text(),'Войти в аккаунт')]",  # кнопка "Войти в аккаунт"
        "login_button": "//button[contains(text(),'Войти')]",  # кнопка "Войти" на странице регистрации
        "personal_cabinet": "//p[contains(text(),'Личный Кабинет')]",  # кнопка "Личный кабинет"
        "authorization_form": "//form",  # форма авторизации / регистрации
        "authorization_link": "//a[contains(text(),'Войти')]",  # ссылка для авторизации
        "registration_link": "//a[contains(text(),'Зарегистрироваться')]",  # ссылка для регистрации
        "title_input": "//h2[contains(text(),'Вход')]",  # заголовок Вход в Личном кабинете
        "logout_button": "//button[contains(text(),'Выход')]",  # кнопка Выход в Личном кабинете
        "constructor_button": "//p[contains(text(),'Конструктор')]",  # кнопка Конструктор
        "logo_button": "//header/nav/div/a",  # лого
        "buns_button": "//span[contains(text(),'Булки')]",  # кнопка Булки
        "sauces_button": "//span[contains(text(),'Соусы')]",  # кнопка Соусы
        "fillings_button": "//span[contains(text(),'Начинки')]"  # кнопка Начинки
    }

    return locators


@pytest.fixture
def driver(creds):
    """фикстура запуска браузера"""
    driver = webdriver.Chrome()
    driver.maximize_window()  # полноэкранный режим

    return driver


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