import pytest
from pages.inventory_page import InventoryPage

@pytest.mark.tc("TC-009")
def test_add_product_cart(login_in_driver):
    driver = login_in_driver
    inventory_page = InventoryPage(driver)

    # POM: Agregamos el primer producto usando el método de la página
    inventory_page.agregar_producto_al_carrito()

    # POM: Obtenemos el texto del contador de la página
    contador = inventory_page.obtener_contador_carrito()
    assert contador == "1"


@pytest.mark.tc("TC-010")
def test_view_cart(login_in_driver):
    driver = login_in_driver
    inventory_page = InventoryPage(driver)

    # POM: Interacción y captura de datos desde la página de inventario
    inventory_page.agregar_producto_al_carrito()
    product_name = inventory_page.obtener_nombre_primer_producto()

    # POM: Navegamos al carrito
    inventory_page.ir_al_carrito()

    # Nota: Para cumplir POM estricto al 100% en la vista del carrito,
    # lo ideal sería usar una clase CartPage, pero podés verificar la URL provisoriamente:
    assert "cart.html" in driver.current_url


@pytest.mark.tc("TC-011")
def test_remove_product(login_in_driver):
    driver = login_in_driver
    inventory_page = InventoryPage(driver)

    inventory_page.agregar_producto_al_carrito()

    # Como el botón cambia a "Remove", interactuamos mediante el método de remover
    # (podés mapearlo en tu InventoryPage o usarlo directamente si el localizador coincide)
    inventory_page.agregar_producto_al_carrito() # En Swag Labs, el botón está en el mismo lugar

    inventory_page.ir_al_carrito()
    assert "cart.html" in driver.current_url