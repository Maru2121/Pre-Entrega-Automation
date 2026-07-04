import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.complete_page import CompletePage
from utils.faker_data import generar_datos_checkout  # ¡Faker en acción!

@pytest.mark.tc("TC-018")
def test_checkout_complete(login_in_driver):
    driver = login_in_driver

    # 1. Flujo en el Inventario
    inventory_page = InventoryPage(driver)
    inventory_page.agregar_producto_al_carrito()
    inventory_page.ir_al_carrito()

    # 2. Flujo en el Carrito
    cart_page = CartPage(driver)
    cart_page.ir_a_la_informacion_checkout()

    # 3. Flujo en Información (Usando Faker)
    info_page = CheckoutInformationPage(driver)
    datos = generar_datos_checkout()
    info_page.completar_formulario(datos["nombre"], datos["apellido"], datos["codigo_postal"])
    info_page.continuar_a_overview()

    # 4. Flujo en Overview
    overview_page = CheckoutOverviewPage(driver)
    overview_page.finalizar_compra()

    # 5. Validación en la página final
    complete_page = CompletePage(driver)
    mensaje = complete_page.obtener_mensaje_exito()

    assert mensaje.lower() == "thank you for your order!"