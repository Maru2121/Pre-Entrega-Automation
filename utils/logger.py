import logging
import os

# Crear carpeta de logs si no existe
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/automation.log", mode="a", encoding="utf-8"),
        logging.StreamHandler()  # Muestra también en la consola
    ]
)

logger = logging.getLogger("AutomationFramework")