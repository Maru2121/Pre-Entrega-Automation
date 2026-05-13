import pytest
from selenium.webdriver.common.by import By


@pytest.mark.tc("TC-016")
def test_logout(login_in_driver):

    driver = login_in_driver

    driver.find_element(By.ID, "react-burger-menu-btn").click()

    driver.find_element(By.ID, "logout_sidebar_link").click()

    # Validación real de logout
    assert driver.find_element(By.ID, "login-button").is_displayed()