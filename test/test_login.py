import pytest
from selenium.webdriver.common.by import By
from utils.LoginPage import login


@pytest.mark.tc("TC-001")
def test_login_validation(login_in_driver):

    driver = login_in_driver

    assert "/inventory.html" in driver.current_url


@pytest.mark.tc("TC-002")
def test_login_invalido(driver):

    login(driver, "standard_user", "wrong_password")

    error = driver.find_element(
        By.CSS_SELECTOR,
        "[data-test='error']"
    )

    assert "epic sadface" in error.text.lower()


@pytest.mark.tc("TC-003")
def test_usuario_bloqueado(driver):

    login(driver, "locked_out_user", "secret_sauce")

    error = driver.find_element(
        By.CSS_SELECTOR,
        "[data-test='error']"
    )

    assert "locked out" in error.text.lower()