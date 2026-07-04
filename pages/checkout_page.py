from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

        # Localizadores
        self.btn_checkout = (By.ID, "checkout")
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.btn_continue = (By.ID, "continue")
        self.btn_finish = (By.ID, "finish")
        self.btn_cancel = (By.ID, "cancel")
        self.success_header = (By.CLASS_NAME, "complete-header")

    def iniciar_checkout(self):
        self.driver.find_element(*self.btn_checkout).click()

    def completar_formulario(self, nombre, apellido, cp):
        self.driver.find_element(*self.first_name_input).send_keys(nombre)
        self.driver.find_element(*self.last_name_input).send_keys(apellido)
        self.driver.find_element(*self.postal_code_input).send_keys(cp)

    def continuar(self):
        self.driver.find_element(*self.btn_continue).click()

    def finalizar_compra(self):
        self.driver.find_element(*self.btn_finish).click()

    def cancelar(self):
        self.driver.find_element(*self.btn_cancel).click()

    def obtener_mensaje_exito(self):
        return self.driver.find_element(*self.success_header).text