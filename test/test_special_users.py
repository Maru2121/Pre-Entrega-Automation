import pytest
from pages.login_page import LoginPage

@pytest.mark.tc("TC-020")
def test_performance_user(driver):
    login_page = LoginPage(driver)
    # Usamos el método estructurado del Page Object pasando usuario y clave estándar
    login_page.login("performance_glitch_user", "secret_sauce")
    assert "inventory.html" in driver.current_url


@pytest.mark.tc("TC-021")
def test_visual_user(driver):
    login_page = LoginPage(driver)
    login_page.login("visual_user", "secret_sauce")
    assert "inventory.html" in driver.current_url


@pytest.mark.tc("TC-022")
def test_error_user(driver):
    login_page = LoginPage(driver)
    login_page.login("error_user", "secret_sauce")
    assert "inventory.html" in driver.current_url


@pytest.mark.tc("TC-023")
def test_problem_user(driver):
    login_page = LoginPage(driver)
    login_page.login("problem_user", "secret_sauce")
    assert "inventory.html" in driver.current_url