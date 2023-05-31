from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_go_to_personal_account_page(driver, creds, locators):
    """Проверяем переход по клику на «Личный кабинет»"""
    driver.get(creds.get("project_stand_main"))  # запускаем стенд на главной странице
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.get("personal_cabinet"))))  # Добавь явное ожидание загрузки кнопки Личный кабинет
    driver.find_element(By.XPATH, locators.get("personal_cabinet")).click()  # Найди кнопку "Личный кабинет" и кликни по ней

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"  # Проверяем текущий URL

    driver.quit()


def test_go_to_constructor_page_from_personal_account_page_on_click_button_constructor(driver, creds, locators):
    """Проверяем переход по клику на «Конструктор»"""
    driver.get(creds.get("project_stand_main"))  # запускаем стенд на главной странице
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.get("personal_cabinet"))))  # Добавь явное ожидание загрузки кнопки Личный кабинет
    driver.find_element(By.XPATH, locators.get("personal_cabinet")).click()  # Найди кнопку "Личный кабинет" и кликни по ней
    driver.find_element(By.XPATH, locators.get("constructor_button")).click()  # Найди кнопку Конструктор и кликни по ней

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"  # Проверяем текущий URL

    driver.quit()


def test_go_to_constructor_page_from_personal_account_page_on_click_logo(driver, creds, locators):
    """Проверяем переход по клику на логотип Stellar Burgers"""
    driver.get(creds.get("project_stand_main"))  # запускаем стенд на главной странице
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.get("personal_cabinet"))))  # Добавь явное ожидание загрузки кнопки Личный кабинет
    driver.find_element(By.XPATH, locators.get("personal_cabinet")).click()  # Найди кнопку "Личный кабинет" и кликни по ней
    driver.find_element(By.XPATH, locators.get("logo_button")).click()  # Найди лого и кликни по нему

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"  # Проверяем текущий URL

    driver.quit()
