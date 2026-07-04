from selenium.webdriver.common.by import By

class CheckoutInformationPage:
    def __init__(self, driver):
        self.driver = driver

        # Localizadores
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.btn_continue = (By.ID, "continue")
        self.btn_cancel = (By.ID, "cancel")

    def completar_formulario(self, nombre, apellido, cp):
        self.driver.find_element(*self.first_name_input).send_keys(nombre)
        self.driver.find_element(*self.last_name_input).send_keys(apellido)
        self.driver.find_element(*self.postal_code_input).send_keys(cp)

    def continuar_a_overview(self):
        self.driver.find_element(*self.btn_continue).click()

    def cancelar_checkout(self):
        self.driver.find_element(*self.btn_cancel).click()