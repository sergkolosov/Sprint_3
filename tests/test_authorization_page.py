import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_us_login_button_on_main_page(driver, creds, locators):
    """Проверяем вход по кнопке «Войти в аккаунт» на главной"""
    driver.get(creds.get("project_stand_main"))  # запускаем стенд на главной странице
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.get("login_account_button"))))  # Добавь явное ожидание загрузки кнопки "Войти в аккаунт"
    driver.find_element(By.XPATH, locators.get("login_account_button")).click()  # Найди кнопку "Войти в аккаунт" и кликни по ней
    driver.find_element(By.XPATH, locators.get("email_field")).send_keys(creds.get('user_login'))  # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, locators.get("password_field")).send_keys(creds.get('user_password'))  # Найди поле "Пароль" и заполни его
    driver.find_element(By.XPATH, locators.get("login_button")).click()  # Найди кнопку "Войти" и кликни по ней
    driver.find_element(By.XPATH, locators.get("personal_cabinet")).click()  # Найди кнопку "Личный кабинет" и кликни по ней
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.get("logout_button"))))  # Добавь явное ожидание загрузки кнопки Выхода

    assert driver.find_element(By.XPATH, locators.get("logout_button")).text == "Выход"  # Найди кнопку Выход и проверь его текстовое значение

    driver.quit()


def test_login_us_personal_cabinet_button(driver, creds, locators):
    """Проверяем вход через кнопку «Личный кабинет»"""
    driver.get(creds.get("project_stand_main"))  # запускаем стенд на главной странице
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.get("personal_cabinet"))))  # Добавь явное ожидание загрузки кнопки Личный кабинет
    driver.find_element(By.XPATH, locators.get("personal_cabinet")).click()  # Найди кнопку "Личный кабинет" и кликни по ней
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.get("authorization_form"))))  # Добавь явное ожидание загрузки формы авторизации
    driver.find_element(By.XPATH, locators.get("email_field")).send_keys(creds.get('user_login'))  # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, locators.get("password_field")).send_keys(creds.get('user_password'))  # Найди поле "Пароль" и заполни его
    driver.find_element(By.XPATH, locators.get("login_button")).click()  # Найди кнопку "Войти" и кликни по ней
    time.sleep(1)  # Костыль. Иначе не работает. Почему - не понимаю.
    driver.find_element(By.XPATH, locators.get("personal_cabinet")).click()  # Найди кнопку "Личный кабинет" и кликни по ней
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.get("logout_button"))))  # Добавь явное ожидание загрузки кнопки Выхода

    assert driver.find_element(By.XPATH, locators.get("logout_button")).text == "Выход"  # Найди кнопку Выход и проверь его текстовое значение

    driver.quit()


def test_login_us_login_link_on_registration_page(driver, creds, locators):
    """Проверяем вход через кнопку в форме регистрации"""
    driver.get(creds.get("project_stand_register"))  # запускаем стенд на странице регистрации
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.get("authorization_link"))))  # Добавь явное ожидание загрузки ссылки Войти
    driver.find_element(By.XPATH, locators.get("authorization_link")).click()  # Найди кнопку "Войти" и кликни по ней
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.get("authorization_form"))))  # Добавь явное ожидание загрузки формы авторизации
    driver.find_element(By.XPATH, locators.get("email_field")).send_keys(creds.get('user_login'))  # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, locators.get("password_field")).send_keys(creds.get('user_password'))  # Найди поле "Пароль" и заполни его
    driver.find_element(By.XPATH, locators.get("login_button")).click()  # Найди кнопку "Войти" и кликни по ней
    driver.find_element(By.XPATH, locators.get("personal_cabinet")).click()  # Найди кнопку "Личный кабинет" и кликни по ней
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.get("logout_button"))))  # Добавь явное ожидание загрузки кнопки Выхода

    assert driver.find_element(By.XPATH, locators.get("logout_button")).text == "Выход"  # Найди кнопку Выход и проверь его текстовое значение

    driver.quit()


def test_login_us_login_link_on_forgot_password_page(driver, creds, locators):
    """Проверяем вход через кнопку в форме восстановления пароля"""
    driver.get(creds.get("project_stand_forgot_password"))  # запускаем стенд на странице восстановления пароля
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.get("authorization_link"))))  # Добавь явное ожидание загрузки ссылки Войти
    driver.find_element(By.XPATH, locators.get("authorization_link")).click()  # Найди кнопку "Войти" и кликни по ней
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.get("authorization_form"))))  # Добавь явное ожидание загрузки формы авторизации
    driver.find_element(By.XPATH, locators.get("email_field")).send_keys(creds.get('user_login'))  # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, locators.get("password_field")).send_keys(creds.get('user_password'))  # Найди поле "Пароль" и заполни его
    driver.find_element(By.XPATH, locators.get("login_button")).click()  # Найди кнопку "Войти" и кликни по ней
    driver.find_element(By.XPATH, locators.get("personal_cabinet")).click()  # Найди кнопку "Личный кабинет" и кликни по ней
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.get("logout_button"))))  # Добавь явное ожидание загрузки кнопки Выхода

    assert driver.find_element(By.XPATH, locators.get("logout_button")).text == "Выход"  # Найди кнопку Выход и проверь его текстовое значение

    driver.quit()


def test_log_out(driver, creds, locators):
    """Проверяем выход из аккаунта по кнопке «Выйти» в личном кабинете"""
    driver.get(creds.get("project_stand_main"))  # запускаем стенд на главной странице
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.get("login_account_button"))))  # Добавь явное ожидание загрузки кнопки "Войти в аккаунт"
    driver.find_element(By.XPATH, locators.get("login_account_button")).click()  # Найди кнопку "Войти в аккаунт" и кликни по ней
    driver.find_element(By.XPATH, locators.get("email_field")).send_keys(creds.get('user_login'))  # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, locators.get("password_field")).send_keys(creds.get('user_password'))  # Найди поле "Пароль" и заполни его
    driver.find_element(By.XPATH, locators.get("login_button")).click()  # Найди кнопку "Войти" и кликни по ней
    driver.find_element(By.XPATH, locators.get("personal_cabinet")).click()  # Найди кнопку "Личный кабинет" и кликни по ней
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.get("logout_button"))))  # Добавь явное ожидание загрузки кнопки Выхода
    driver.find_element(By.XPATH, locators.get("logout_button")).click()  # Найди кнопку "Выход" и кликни по ней
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.get("title_input"))))  # Добавь явное ожидание загрузки заголовка Входа

    assert driver.find_element(By.XPATH, locators.get("title_input")).text == "Вход"  # Найди заголовок Вход и проверь его текстовое значение

    driver.quit()
