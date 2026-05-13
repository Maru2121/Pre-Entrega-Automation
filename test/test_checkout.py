import pytest
from selenium.webdriver.common.by import By


def agregar_producto(driver):

    driver.find_element(
        By.CSS_SELECTOR,
        ".inventory_item:first-child button"
    ).click()

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()


@pytest.mark.tc("TC-017")
def test_checkout_basico(login_in_driver):

    driver = login_in_driver

    agregar_producto(driver)

    driver.find_element(By.ID, "checkout").click()

    assert "checkout-step-one" in driver.current_url


@pytest.mark.tc("TC-018")
def test_checkout_complete(login_in_driver):

    driver = login_in_driver

    agregar_producto(driver)

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Juan")
    driver.find_element(By.ID, "last-name").send_keys("Perez")
    driver.find_element(By.ID, "postal-code").send_keys("1000")

    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()

    success = driver.find_element(By.CLASS_NAME, "complete-header")

    assert success.is_displayed()
    assert success.text.lower() == "thank you for your order!"


@pytest.mark.tc("TC-019")
def test_cancel_checkout(login_in_driver):

    driver = login_in_driver

    agregar_producto(driver)

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "cancel").click()

    assert "cart" in driver.current_url