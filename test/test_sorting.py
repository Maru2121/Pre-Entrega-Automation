import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def obtener_nombres(driver):

    items = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item_name"
    )

    return [item.text for item in items]


def obtener_precios(driver):

    precios = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item_price"
    )

    return [
        float(p.text.replace("$", ""))
        for p in precios
    ]


@pytest.mark.tc("TC-012")
def test_sort_az(login_in_driver):

    driver = login_in_driver

    dropdown = Select(
        driver.find_element(
            By.CLASS_NAME,
            "product_sort_container"
        )
    )

    dropdown.select_by_value("az")

    productos = obtener_nombres(driver)

    assert productos == sorted(productos)


@pytest.mark.tc("TC-013")
def test_sort_za(login_in_driver):

    driver = login_in_driver

    dropdown = Select(
        driver.find_element(
            By.CLASS_NAME,
            "product_sort_container"
        )
    )

    dropdown.select_by_value("za")

    productos = obtener_nombres(driver)

    assert productos == sorted(productos, reverse=True)


@pytest.mark.tc("TC-014")
def test_sort_low_high(login_in_driver):

    driver = login_in_driver

    dropdown = Select(
        driver.find_element(
            By.CLASS_NAME,
            "product_sort_container"
        )
    )

    dropdown.select_by_value("lohi")

    precios = obtener_precios(driver)

    assert precios == sorted(precios)


@pytest.mark.tc("TC-015")
def test_sort_high_low(login_in_driver):

    driver = login_in_driver

    dropdown = Select(
        driver.find_element(
            By.CLASS_NAME,
            "product_sort_container"
        )
    )

    dropdown.select_by_value("hilo")

    precios = obtener_precios(driver)

    assert precios == sorted(precios, reverse=True)