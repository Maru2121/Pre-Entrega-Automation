import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from utils.LoginPage import login

from page.login_page import LoginPage

#def test_login_validation(driver):
def test_login_ok(driver):
    login_page = LoginPage(driver)

    login_page.login("standard_user","secret_sauce")

    assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"

def test_login_invalid_password(driver):
    login_page = LoginPage(driver)

    login_page.login("standard_user","123456")

    error = login_page.get_error_password_message()

    assert "Epic sadface: Username and password do not match any user in this service" in error

@pytest.mark.tc("TC-001")
def test_login_validation(login_in_driver):

    driver = login_in_driver

    assert "/inventory.html" in driver.current_url


@pytest.mark.tc("TC-002")
def test_login_invalido(driver):

    # OLD IMPLEMENTATION - pending migration to POM login(driver, "standard_user", "wrong_password")

    error = driver.find_element(
        By.CSS_SELECTOR,
        "[data-test='error']"
    )

    assert "epic sadface" in error.text.lower()


@pytest.mark.tc("TC-003")
def test_usuario_bloqueado(driver):

   # OLD IMPLEMENTATION - pending migration to POM login(driver, "locked_out_user", "secret_sauce")

    error = driver.find_element(
        By.CSS_SELECTOR,
        "[data-test='error']"
    )

    assert "locked out" in error.text.lower()