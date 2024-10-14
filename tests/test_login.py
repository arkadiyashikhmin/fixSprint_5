# test_login_main_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators

def test_login_via_main_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Вход через кнопку «Войти в аккаунт» на главной
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(StellarBurgersLocators.LOGIN_BUTTON_MAIN)).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(StellarBurgersLocators.EMAIL_INPUT_LOGIN)).send_keys(
        "test_testov_2024@gmail.com")
    driver.find_element(*StellarBurgersLocators.PASSWORD_INPUT_LOGIN).send_keys("12345678")
    driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BUTTON).click()

    # Выход после успешного входа
    driver.quit()
