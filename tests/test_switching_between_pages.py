from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locator import Locators
from data import Urls


class TestSwitchingBetweenPages:
    def test_go_to_personal_account_page(self, driver):
        """Проверяем переход по клику на «Личный кабинет»"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON)).click()

        assert driver.current_url == Urls.MAIN_PAGE, f'Ожидалось URL: "{Urls.LOGIN_PAGE}", получено "{driver.current_url}"'

    def test_go_to_constructor_page_from_personal_account_page_on_click_button_constructor(self, driver):
        """Проверяем переход по клику на «Конструктор»"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)).click()

        assert driver.current_url == Urls.MAIN_PAGE, f'Ожидалось URL: "{Urls.MAIN_PAGE}", получено "{driver.current_url}"'


    def test_go_to_constructor_page_from_personal_account_page_on_click_logo(self, driver):
        """Проверяем переход по клику на логотип Stellar Burgers"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGO_BUTTON)).click()

        assert driver.current_url == Urls.MAIN_PAGE, f'Ожидалось URL: "{Urls.MAIN_PAGE}", получено "{driver.current_url}"'
