from selenium.webdriver.common.by import By


class Locators:
    REGISTRATION_NAME = (By.XPATH, "//label[text() = 'Имя']/parent::div/input")
    REGISTRATION_EMAIL = (By.XPATH, "//label[text() = 'Email']/parent::div/input")
    REGISTRATION_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/parent::div/input")
    EMAIL_FIELD = (By.XPATH, "//input[@name='name'")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль'")
    PASSWORD_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default']")
    REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    PERSONAL_CABINET = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    AUTHORIZATION_FORM = (By.XPATH, "//form")
    AUTHORIZATION_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")
    REGISTRATION_LINK = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    TITLE_INPUT = (By.XPATH, "//h2[contains(text(),'Вход')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    LOGO_BUTTON = (By.XPATH, "//header/nav/div/a")
    BUNS_BUTTON = (By.XPATH, "//span[contains(text(),'Булки')]")
    SAUCES_BUTTON = (By.XPATH, "//span[contains(text(),'Соусы')]")
    FILLINGS_BUTTON = (By.XPATH, "//span[contains(text(),'Начинки')]")

