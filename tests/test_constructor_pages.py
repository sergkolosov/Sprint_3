from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locator import Locators

flag_selected_tab = 'tab_tab_type_current__2BEPc'


class TestConstructorPages:

    def test_go_to_sauces_partition(self, driver):
        """Проверяем что работает переход к разделу «Соусы»"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.SAUCES_BUTTON)).click()

        tab_classes = driver.find_element(*Locators.SAUCES_BUTTON_SELECT).get_attribute('class')
        assert flag_selected_tab in tab_classes, f'Ожидалось, что флаг "{flag_selected_tab}" содержится в выделенном табе, получено: "{tab_classes}"'

    def test_go_to_fillings_partition(self, driver):
        """Проверяем что работает переход к разделу «Начинки»"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.FILLINGS_BUTTON)).click()

        tab_classes = driver.find_element(*Locators.FILLINGS_BUTTON_SELECT).get_attribute('class')
        assert flag_selected_tab in tab_classes, f'Ожидалось, что флаг "{flag_selected_tab}" содержится в выделенном табе, получено: "{tab_classes}"'

    def test_go_to_buns_partition(self, driver):
        """Проверяем что работает переход к разделу «Булки»"""
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.SAUCES_BUTTON)).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()

        tab_classes = driver.find_element(*Locators.BUNS_BUTTON_SELECT).get_attribute('class')
        assert flag_selected_tab in tab_classes, f'Ожидалось, что флаг "{flag_selected_tab}" содержится в выделенном табе, получено: "{tab_classes}"'
