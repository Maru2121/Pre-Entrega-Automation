import pytest
from selenium.webdriver.common.by import By


@pytest.mark.tc("TC-009")
def test_add_product_cart(login_in_driver):

    driver = login_in_driver

    driver.find_element(By.CSS_SELECTOR, ".inventory_item:first-child button").click()

    contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert contador.text == "1"


@pytest.mark.tc("TC-010")
def test_view_cart(login_in_driver):

    driver = login_in_driver

    driver.find_element(By.CSS_SELECTOR, ".inventory_item:first-child button").click()

    product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    assert cart_item == product_name


@pytest.mark.tc("TC-011")
def test_remove_product(login_in_driver):

    driver = login_in_driver

    driver.find_element(By.CSS_SELECTOR, ".inventory_item:first-child button").click()

    driver.find_element(By.CLASS_NAME, "btn_secondary").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    assert len(driver.find_elements(By.CLASS_NAME, "cart_item")) == 0