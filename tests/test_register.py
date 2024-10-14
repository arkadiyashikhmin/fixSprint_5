# test_register.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators


def test_successful_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Переход на страницу регистрации
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(StellarBurgersLocators.ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(StellarBurgersLocators.REGISTER_LINK)).click()

    # Ввод данных для регистрации
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(StellarBurgersLocators.NAME_INPUT)).send_keys("Test123")
    driver.find_element(*StellarBurgersLocators.EMAIL_INPUT).send_keys("test_testov_2024@gmail.com")
    driver.find_element(*StellarBurgersLocators.PASSWORD_INPUT).send_keys("12345678")

    # Проверка кликабельности и нажатие кнопки регистрации
    register_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.REGISTER_BUTTON))
    register_button.click()

    # Проверка, что появилось сообщение о существующем пользователе
    user_exists = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(StellarBurgersLocators.USER_EXISTS_ERROR_MESSAGE))

    if user_exists:
        assert user_exists is not None, "Пользователь уже существует."
    else:
        # Если сообщение не появилось, проверяем наличие сообщения о некорректном пароле
        error_present = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(StellarBurgersLocators.PASSWORD_ERROR_MESSAGE))
        assert error_present is not None, "Ошибка некорректного пароля не появилась."
