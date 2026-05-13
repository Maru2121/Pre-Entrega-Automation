import pytest
from utils.LoginPage import login


@pytest.mark.tc("TC-020")
def test_performance_user(driver):

    login(driver, "performance_glitch_user")

    assert "inventory.html" in driver.current_url


@pytest.mark.tc("TC-021")
def test_visual_user(driver):

    login(driver, "visual_user")

    assert "inventory.html" in driver.current_url


@pytest.mark.tc("TC-022")
def test_error_user(driver):

    login(driver, "error_user")

    assert "inventory.html" in driver.current_url


@pytest.mark.tc("TC-023")
def test_problem_user(driver):

    login(driver, "problem_user")

    assert "inventory.html" in driver.current_url