# test_nachinki_sousi_bulki.py
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators

def test_nachinki_sousi_bulki(driver):
    # Переход на главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Нажатие на вкладку "Начинки"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.NACHINKI_TAB)).click()
    # Нажатие на вкладку "Соусы"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.SOUSI_TAB)).click()
    # Нажатие на вкладку "Булки"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.BULKI_TAB)).click()
    # Закрытие браузера
    driver.quit()
