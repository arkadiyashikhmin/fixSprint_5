# test_login_register_button.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators

def test_login_via_register_button(driver):
    # Переход на страницу регистрации
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Нажатие кнопки "Войти" на странице регистрации
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(StellarBurgersLocators.LOGIN_LINK)).click()

    # Ввод email и пароля
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(StellarBurgersLocators.EMAIL_INPUT_LOGIN)).send_keys("test_testov_2024@gmail.com")
    driver.find_element(*StellarBurgersLocators.PASSWORD_INPUT_LOGIN).send_keys("12345678")

    # Нажатие кнопки "Войти"
    driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BUTTON).click()

    # Закрытие браузера
    driver.quit()
