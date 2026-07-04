from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

        # Localizadores
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.item_name = (By.CLASS_NAME, "inventory_item_name")
        self.btn_remove = (By.CLASS_NAME, "btn_secondary")
        self.btn_checkout = (By.ID, "checkout")

    def obtener_cantidad_items(self):
        return len(self.driver.find_elements(*self.cart_items))

    def obtener_nombre_item(self):
        return self.driver.find_element(*self.item_name).text

    def remover_primer_producto(self):
        self.driver.find_element(*self.btn_remove).click()

    def ir_a_la_informacion_checkout(self):
        self.driver.find_element(*self.btn_checkout).click()