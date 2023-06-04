from selenium.webdriver.common.by import By


class Locators:
    LOGO_BUTTON = (By.XPATH, "//header/nav/div/a")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    BUNS_BUTTON = (By.XPATH, "//span[contains(text(),'Булки')]")
    SAUCES_BUTTON = (By.XPATH, "//span[contains(text(),'Соусы')]")
    FILLINGS_BUTTON = (By.XPATH, "//span[contains(text(),'Начинки')]")
    BUNS_BUTTON_SELECT = (By.XPATH, "//span[contains(text(),'Булки')]/parent::div")
    SAUCES_BUTTON_SELECT = (By.XPATH, "//span[contains(text(),'Соусы')]/parent::div")
    FILLINGS_BUTTON_SELECT = (By.XPATH, "//span[contains(text(),'Начинки')]/parent::div")

    LOGIN_ACCOUNT_OR_PLACE_ORDER_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")

    REGISTRATION_LINK = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    REGISTRATION_NAME_FIELD = (By.XPATH, "//label[text() = 'Имя']/parent::div/input")
    REGISTRATION_EMAIL_FIELD = (By.XPATH, "//label[text() = 'Email']/parent::div/input")
    REGISTRATION_PASSWORD_FIELD = (By.XPATH, "//label[text() = 'Пароль']/parent::div/input")
    REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    PASSWORD_ERROR_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default']")

    PERSONAL_CABINET_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    INPUT_TITLE_PERSONAL_CABINET = (By.XPATH, "//h2[contains(text(),'Вход')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")
    LOGIN_EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
