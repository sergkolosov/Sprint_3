from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locator import Locators


class TestConstructorPages:
    def test_go_to_sauces_partition(self, driver):
        """Проверяем что работает переход к разделу «Соусы»"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.SAUCES_BUTTON)).click()

        flag_selected_tab = 'tab_tab_type_current__2BEPc'
        actually_value = flag_selected_tab in driver.find_element(*Locators.SAUCES_BUTTON_SELECT).get_attribute('class')
        expected_value = True
        assert actually_value == expected_value, f'Ожидалось, что содержание "{flag_selected_tab}" в выделенном табе: "{expected_value}", получено "{actually_value}"'

    def test_go_to_fillings_partition(self, driver):
        """Проверяем что работает переход к разделу «Начинки»"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.FILLINGS_BUTTON)).click()

        flag_selected_tab = 'tab_tab_type_current__2BEPc'
        actually_value = flag_selected_tab in driver.find_element(*Locators.FILLINGS_BUTTON_SELECT).get_attribute('class')
        expected_value = True
        assert actually_value == expected_value, f'Ожидалось, что содержание "{flag_selected_tab}" в выделенном табе: "{expected_value}", получено "{actually_value}"'

    def test_go_to_buns_partition(self, driver):
        """Проверяем что работает переход к разделу «Булки»"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.SAUCES_BUTTON)).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()

        flag_selected_tab = 'tab_tab_type_current__2BEPc'
        actually_value = flag_selected_tab in driver.find_element(*Locators.BUNS_BUTTON_SELECT).get_attribute('class')
        expected_value = True
        assert actually_value == expected_value, f'Ожидалось, что содержание "{flag_selected_tab}" в выделенном табе: "{expected_value}", получено "{actually_value}"'
