from selenium.webdriver.common.by import By

class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

        # Localizadores
        self.btn_finish = (By.ID, "finish")
        self.btn_cancel = (By.ID, "cancel")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def obtener_total(self):
        return self.driver.find_element(*self.total_label).text

    def finalizar_compra(self):
        self.driver.find_element(*self.btn_finish).click()

    def cancelar_compra(self):
        self.driver.find_element(*self.btn_cancel).click()