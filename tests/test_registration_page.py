import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_success_registration(driver, creds, random_email, random_password, locators):
    """Проверяем Успешную регистрацию"""
    driver.get(creds.get("project_stand_register"))  # запускаем стенд на странице регистрации
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.get("authorization_form"))))  # Добавь явное ожидание загрузки формы авторизации
    driver.find_element(By.XPATH, locators.get("registration_name")).send_keys('User')  # Найди поле "Имя" и заполни его
    driver.find_element(By.XPATH, locators.get("registration_email")).send_keys(random_email)  # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, locators.get("registration_password")).send_keys(random_password)  # Найди поле "Пароль" и заполни его
    driver.find_element(By.XPATH, locators.get("registration_button")).click()  # Найди кнопку "Зарегистрироваться" и кликни по ней
    time.sleep(1)  # Костыль. Иначе не работает. Почему - не понимаю.
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.get("authorization_form"))))  # Добавь явное ожидание загрузки формы авторизации
    driver.find_element(By.XPATH, locators.get("email_field")).send_keys(random_email)  # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, locators.get("password_field")).send_keys(random_password)  # Найди поле "Пароль" и заполни его
    driver.find_element(By.XPATH, locators.get("login_button")).click()  # Найди кнопку "Войти" и кликни по ней
    driver.find_element(By.XPATH,locators.get("personal_cabinet")).click()  # Найди кнопку "Личный кабинет" и кликни по ней
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.get("logout_button"))))  # Добавь явное ожидание загрузки кнопки Выхода

    assert driver.find_element(By.XPATH, locators.get("logout_button")).text == "Выход"  # Найди кнопку Выход и проверь его текстовое значение

    driver.quit()


def test_registration_invalid_password(driver, creds, random_email, locators):
    """Проверяем Ошибку для некорректного пароля"""
    driver.get(creds.get("project_stand_register"))  # запускаем стенд на странице регистрации
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.get("authorization_form"))))  # Добавь явное ожидание загрузки формы авторизации
    driver.find_element(By.XPATH, locators.get("registration_name")).send_keys('User')  # Найди поле "Имя" и заполни его
    driver.find_element(By.XPATH, locators.get("registration_email")).send_keys(random_email)  # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, locators.get("registration_password")).send_keys('12345')  # Найди поле "Пароль" и заполни его невалидным значением (менее 6 знаков)
    driver.find_element(By.XPATH, locators.get("registration_button")).click()  # Найди кнопку "Зарегистрироваться" и кликни по ней

    assert driver.find_element(By.XPATH, locators.get("password_error")).text == "Некорректный пароль"  # Найди сообщение об ошибке и проверь его текстовое значение

    driver.quit()
