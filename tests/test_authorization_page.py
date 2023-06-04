from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import Creds
from locator import Locators


class TestAuthorization:
    user_email = Creds.USER_EMAIL
    user_password = Creds.USER_PASSWORD

    def test_login_us_login_button_on_main_page(self, driver):
        """Проверяем вход по кнопке «Войти в аккаунт» на главной"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGIN_ACCOUNT_OR_PLACE_ORDER_BUTTON)).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys(self.user_email)
        driver.find_element(*Locators.LOGIN_PASSWORD_FIELD).send_keys(self.user_password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        actually_value = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_OR_PLACE_ORDER_BUTTON)).text
        expected_value = 'Оформить заказ'
        assert actually_value == expected_value, f'Ожидалось текст на кнопке: "{expected_value}", получено "{actually_value}"'

    def test_login_us_personal_cabinet_button(self, driver):
        """Проверяем вход через кнопку «Личный кабинет»"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON)).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys(self.user_email)
        driver.find_element(*Locators.LOGIN_PASSWORD_FIELD).send_keys(self.user_password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        actually_value = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_OR_PLACE_ORDER_BUTTON)).text
        expected_value = 'Оформить заказ'
        assert actually_value == expected_value, f'Ожидалось текст на кнопке: "{expected_value}", получено "{actually_value}"'

    def test_login_us_login_link_on_registration_page(self, driver):
        """Проверяем вход через кнопку в форме регистрации"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.REGISTRATION_LINK)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGIN_LINK)).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys(self.user_email)
        driver.find_element(*Locators.LOGIN_PASSWORD_FIELD).send_keys(self.user_password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        actually_value = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_OR_PLACE_ORDER_BUTTON)).text
        expected_value = 'Оформить заказ'
        assert actually_value == expected_value, f'Ожидалось текст на кнопке: "{expected_value}", получено "{actually_value}"'

    def test_login_us_login_link_on_forgot_password_page(self, driver):
        """Проверяем вход через кнопку в форме восстановления пароля"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.RECOVER_PASSWORD_LINK)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGIN_LINK)).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys(self.user_email)
        driver.find_element(*Locators.LOGIN_PASSWORD_FIELD).send_keys(self.user_password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        actually_value = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_OR_PLACE_ORDER_BUTTON)).text
        expected_value = 'Оформить заказ'
        assert actually_value == expected_value, f'Ожидалось текст на кнопке: "{expected_value}", получено "{actually_value}"'

    def test_log_out(self, driver):
        """Проверяем выход из аккаунта по кнопке «Выйти» в личном кабинете"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGIN_ACCOUNT_OR_PLACE_ORDER_BUTTON)).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys(self.user_email)
        driver.find_element(*Locators.LOGIN_PASSWORD_FIELD).send_keys(self.user_password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGO_BUTTON)).click()

        actually_value = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_OR_PLACE_ORDER_BUTTON)).text
        expected_value = 'Войти в аккаунт'
        assert actually_value == expected_value, f'Ожидалось текст на кнопке: "{expected_value}", получено "{actually_value}"'
