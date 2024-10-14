from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators

def test_login_via_account_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Вход через кнопку «Войти в аккаунт» на главной
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(StellarBurgersLocators.LOGIN_BUTTON_MAIN)).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(StellarBurgersLocators.EMAIL_INPUT_LOGIN)).send_keys(
        "test_testov_2024@gmail.com")
    driver.find_element(*StellarBurgersLocators.PASSWORD_INPUT_LOGIN).send_keys("12345678")
    driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BUTTON).click()

    # Переход в «Личный кабинет»
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(StellarBurgersLocators.LOGIN_BUTTON_ACCOUNT)).click()

    # Выход из аккаунта
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(StellarBurgersLocators.LOGOUT_BUTTON)).click()

    # Повторный вход
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarBurgersLocators.EMAIL_INPUT_LOGIN)).send_keys(
        "test_testov_2024@gmail.com")
    driver.find_element(*StellarBurgersLocators.PASSWORD_INPUT_LOGIN).send_keys("12345678")
    driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BUTTON).click()

    # Закрытие браузера
    driver.quit()
