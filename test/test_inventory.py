import pytest
from selenium.webdriver.common.by import By


@pytest.mark.tc("TC-004")
def test_inventory_title(login_in_driver):

    driver = login_in_driver

    assert "Swag Labs" in driver.title
    assert "inventory" in driver.current_url


@pytest.mark.tc("TC-005")
def test_productos_visibles(login_in_driver):

    driver = login_in_driver

    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    assert len(productos) >= 5


@pytest.mark.tc("TC-006")
def test_ui_elements(login_in_driver):

    driver = login_in_driver

    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

    assert menu.is_displayed()
    assert filtro.is_displayed()


@pytest.mark.tc("TC-007")
def test_footer_redes(login_in_driver):

    driver = login_in_driver

    footer = driver.find_element(By.CLASS_NAME, "footer")

    twitter = driver.find_element(By.CSS_SELECTOR, "[data-test='social-twitter']")
    facebook = driver.find_element(By.CSS_SELECTOR, "[data-test='social-facebook']")
    linkedin = driver.find_element(By.CSS_SELECTOR, "[data-test='social-linkedin']")

    assert footer.is_displayed()
    assert twitter.is_displayed()
    assert facebook.is_displayed()
    assert linkedin.is_displayed()


@pytest.mark.tc("TC-008")
def test_imagenes_productos(login_in_driver):

    driver = login_in_driver

    imagenes = driver.find_elements(By.CSS_SELECTOR, ".inventory_item img")

    assert len(imagenes) > 0

    for imagen in imagenes:
        assert imagen.is_displayed()

        src = imagen.get_attribute("src")

        assert src is not None
        assert src != ""


@pytest.mark.tc("TC-025")
def test_detalle_producto(login_in_driver):

    driver = login_in_driver

    producto = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0]

    nombre_producto = producto.text

    producto.click()

    detalle = driver.find_element(By.CLASS_NAME, "inventory_details_name")

    assert detalle.text.strip().lower() == nombre_producto.strip().lower()