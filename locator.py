from selenium.webdriver.common.by import By


class Locators:
    AUTHORIZATION_FORM = (By.XPATH, "//form")
    AUTHORIZATION_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")
    BUNS_BUTTON = (By.XPATH, "//span[contains(text(),'Булки')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    EMAIL_FIELD = (By.XPATH, "//input[@name='name'")
    FILLINGS_BUTTON = (By.XPATH, "//span[contains(text(),'Начинки')]")
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    LOGO_BUTTON = (By.XPATH, "//header/nav/div/a")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    PASSWORD_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль'")
    PERSONAL_CABINET = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    REGISTRATION_EMAIL = (By.XPATH, "//label[text() = 'Email']/parent::div/input")
    REGISTRATION_LINK = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    REGISTRATION_NAME = (By.XPATH, "//label[text() = 'Имя']/parent::div/input")
    REGISTRATION_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/parent::div/input")
    SAUCES_BUTTON = (By.XPATH, "//span[contains(text(),'Соусы')]")
    TITLE_INPUT = (By.XPATH, "//h2[contains(text(),'Вход')]")
