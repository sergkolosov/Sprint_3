from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locator import Locators


class TestSwitchingBetweenPages:
    def test_go_to_personal_account_page(self, driver):
        """Проверяем переход по клику на «Личный кабинет»"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON)).click()

        actually_value = driver.current_url
        expected_value = 'https://stellarburgers.nomoreparties.site/login'
        assert actually_value == expected_value, f'Ожидалось URL: "{expected_value}", получено "{actually_value}"'

    def test_go_to_constructor_page_from_personal_account_page_on_click_button_constructor(self, driver):
        """Проверяем переход по клику на «Конструктор»"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)).click()

        actually_value = driver.current_url
        expected_value = 'https://stellarburgers.nomoreparties.site/'
        assert actually_value == expected_value, f'Ожидалось URL: "{expected_value}", получено "{actually_value}"'

    def test_go_to_constructor_page_from_personal_account_page_on_click_logo(self, driver):
        """Проверяем переход по клику на логотип Stellar Burgers"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGO_BUTTON)).click()

        actually_value = driver.current_url
        expected_value = 'https://stellarburgers.nomoreparties.site/'
        assert actually_value == expected_value, f'Ожидалось URL: "{expected_value}", получено "{actually_value}"'
