from selenium.webdriver.common.by import By

URL = "https://www.saucedemo.com/"

def login(driver, username="standard_user", password=None):

    driver.get(URL)

    driver.find_element(By.ID, "user-name").send_keys(username)

    if password is None:
        password = "secret_sauce"

    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()