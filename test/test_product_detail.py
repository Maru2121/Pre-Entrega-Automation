import pytest
from selenium.webdriver.common.by import By


@pytest.mark.tc("TC-025")
def test_product_detail(login_in_driver):

    driver = login_in_driver

    # Guardar nombre del producto
    producto = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0]
    nombre = producto.text

    # Click producto
    producto.click()

    # Validar que el detalle es visible
    detalle = driver.find_element(By.CLASS_NAME, "inventory_details_name")

    assert detalle.is_displayed()

    # Validar que es el mismo producto
    assert detalle.text == nombre