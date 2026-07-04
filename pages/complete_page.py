from selenium.webdriver.common.by import By

class CompletePage:
    def __init__(self, driver):
        self.driver = driver

        # Localizadores
        self.success_header = (By.CLASS_NAME, "complete-header")
        self.btn_back_home = (By.ID, "back-to-products")

    def obtener_mensaje_exito(self):
        return self.driver.find_element(*self.success_header).text

    def volver_a_home(self):
        self.driver.find_element(*self.btn_back_home).click()