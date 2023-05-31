from selenium.webdriver.common.by import By



def test_go_to_sauces_partition(driver, creds, locators):
    """Проверяем что работает переход к разделу «Соусы»"""
    driver.get(creds.get("project_stand_main"))  # запускаем стенд на главной странице (она же Конструктор)
    driver.find_element(By.XPATH, locators.get("sauces_button")).click()  # Найди кнопку "Соусы" и кликни по ней

    assert 'tab_tab_type_current__2BEPc' in driver.find_element(By.XPATH, locators.get("sauces_button") + "/parent::div").get_attribute('class')  # Проверяем что класс, идентифицирующий активный таб, содержится в классах родителя кнопки "Соусы"

    driver.quit()


def test_go_to_fillings_partition(driver, creds, locators):
    """Проверяем что работает переход к разделу «Начинки»"""
    driver.get(creds.get("project_stand_main"))  # запускаем стенд на главной странице (она же Конструктор)
    driver.find_element(By.XPATH, locators.get("fillings_button")).click()  # Найди кнопку "Начинки" и кликни по ней

    assert 'tab_tab_type_current__2BEPc' in driver.find_element(By.XPATH, locators.get("fillings_button") + "/parent::div").get_attribute('class')  # Проверяем что класс, идентифицирующий активный таб, содержится в классах родителя кнопки "Начинки"

    driver.quit()


def test_go_to_buns_partition(driver, creds, locators):
    """Проверяем что работает переход к разделу «Булки»"""
    driver.get(creds.get("project_stand_main"))  # запускаем стенд на главной странице (она же Конструктор)
    driver.find_element(By.XPATH, locators.get("sauces_button")).click()  # Найди кнопку "Соусы" и кликни по ней
    driver.find_element(By.XPATH, locators.get("buns_button")).click()  # Найди кнопку "Булки" и кликни по ней

    assert 'tab_tab_type_current__2BEPc' in driver.find_element(By.XPATH, locators.get("buns_button") + "/parent::div").get_attribute('class')  # Проверяем что класс, идентифицирующий активный таб, содержится в классах родителя кнопки "Булки"

    driver.quit()