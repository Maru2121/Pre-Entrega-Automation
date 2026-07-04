import os
from datetime import datetime
from utils.logger import logger

def tomar_captura(driver, nombre_test):
    os.makedirs("screenshots", exist_ok=True)
    fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta = f"screenshots/{nombre_test}_{fecha_hora}.png"

    try:
        driver.save_screenshot(ruta)
        logger.info(f"📸 Captura de pantalla guardada en: {ruta}")
        return ruta
    except Exception as e:
        logger.error(f"❌ No se pudo tomar la captura de pantalla: {e}")
        return None