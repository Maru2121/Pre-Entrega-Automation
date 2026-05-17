from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver): #constructor es una funcion que ejecuta todo lo que esta adentro,
        self.driver = driver # los objetos del constructor se ejecutan en el momento

        # selectores
        self.username_input = (By.ID,"user-name")
        self.password_input = (By.ID,"login-button")
        self.login_button = (By.ID,"login-button")
        self.error_password = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self): #funcion
        self.driver.get("https://www.saucedemo.com/")

    def ingresar_usuario(self, usuario):
        self.driver.find_element(*self.username_input).send_keys(usuario) #puntero me devuelve el valor que esta guardado me lo va a traer

    def ingresar_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self,usuario,password):
        self.open()
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.click_login()

    def get_error_password_message(self):
        return self.driver.find_element(*self.error_password).text
