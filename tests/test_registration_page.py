from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locator import Locators


class TestRegistrationPage:
    user_email = Faker().email()
    correct_user_password = '123456'
    incorrect_user_password = '12345'

    def test_success_registration(self, driver):
        """Проверяем Успешную регистрацию"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.REGISTRATION_LINK)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REGISTRATION_NAME_FIELD)).send_keys('User')
        driver.find_element(*Locators.REGISTRATION_EMAIL_FIELD).send_keys(self.user_email)
        driver.find_element(*Locators.REGISTRATION_PASSWORD_FIELD).send_keys(self.correct_user_password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()  # Зарегистрировались

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys(self.user_email)
        driver.find_element(*Locators.LOGIN_PASSWORD_FIELD).send_keys(self.correct_user_password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()  # Вошли

        actually_value = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_OR_PLACE_ORDER_BUTTON)).text
        expected_value = 'Оформить заказ'
        assert actually_value == expected_value, f'Ожидалось текст на кнопке: "{expected_value}", получено "{actually_value}"'

    def test_registration_invalid_password(self, driver):
        """Проверяем Ошибку для некорректного пароля"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.REGISTRATION_LINK)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REGISTRATION_NAME_FIELD)).send_keys('User')
        driver.find_element(*Locators.REGISTRATION_EMAIL_FIELD).send_keys(self.user_email)
        driver.find_element(*Locators.REGISTRATION_PASSWORD_FIELD).send_keys(self.incorrect_user_password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        actually_value = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PASSWORD_ERROR_MESSAGE)).text
        expected_value = 'Некорректный пароль'
        assert actually_value == expected_value, f'Ожидалось сообщение об ошибке: "{expected_value}", получено "{actually_value}"'
