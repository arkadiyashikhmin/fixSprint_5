from selenium.webdriver.common.by import By

class StellarBurgersLocators:
    NACHINKI_TAB = (By.XPATH, "//span[text()='Начинки']")
    SOUSI_TAB = (By.XPATH, "//span[text()='Соусы']")
    BULKI_TAB = (By.XPATH, "//span[text()='Булки']")
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx')]")
    PASSWORD_ERROR_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти" на странице
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Локатор для кнопки на главной
    LOGIN_BUTTON_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")  # Локатор для текста "Личный Кабинет"
    LOGIN_BUTTON_REGISTER = (By.XPATH, "//a[@href='/register']")  # Локатор для кнопки в форме регистрации
    LOGIN_BUTTON_FORGOT_PASSWORD = (By.XPATH, "//a[@href='/forgot-password']")  # Локатор для кнопки в форме восстановления пароля
    EMAIL_INPUT_LOGIN = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Локатор для поля ввода email
    PASSWORD_INPUT_LOGIN = (By.XPATH, "//input[@type='password']")  # Локатор для поля ввода пароля
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Локатор для кнопки "Войти"
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']")
    USER_EXISTS_ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Такой пользователь уже существует')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and text()='Войти']")  # Новый локатор для ссылки "Войти"
