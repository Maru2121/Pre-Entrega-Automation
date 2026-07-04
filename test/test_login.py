import pytest
from pages.login_page import LoginPage
from data.users import USERS  # Fuente externa de datos

# Convertimos el diccionario USERS en una lista de tuplas (usuario, password) para parametrizar
lista_usuarios = [(user, pwd) for user, pwd in USERS.items()]

@pytest.mark.tc("TC-001")
@pytest.mark.parametrize("usuario, password", lista_usuarios)
def test_login_multiples_usuarios(driver, usuario, password):
    """Prueba el comportamiento de login con todos los usuarios registrados en data/users.py"""
    login_page = LoginPage(driver)
    login_page.login(usuario, password)

    if usuario == "locked_out_user":
        # Escenario Negativo obligatorio
        error = login_page.get_error_message()
        assert "locked out" in error.lower()
    else:
        # Escenarios Exitosos
        assert "/inventory.html" in driver.current_url