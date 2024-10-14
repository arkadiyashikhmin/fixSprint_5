# test_login_recover_password.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators

def test_login_via_recover_password(driver):
    # Переход на страницу логина
    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Нажатие на ссылку "Восстановить пароль"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(StellarBurgersLocators.FORGOT_PASSWORD_LINK)).click()

    # Возврат на страницу логина
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(StellarBurgersLocators.LOGIN_LINK)).click()

    # Ввод email и пароля
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(StellarBurgersLocators.EMAIL_INPUT_LOGIN)).send_keys("test_testov_2024@gmail.com")
    driver.find_element(*StellarBurgersLocators.PASSWORD_INPUT_LOGIN).send_keys("12345678")

    # Нажатие кнопки "Войти"
    driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BUTTON).click()

    # Закрытие браузера
    driver.quit()
