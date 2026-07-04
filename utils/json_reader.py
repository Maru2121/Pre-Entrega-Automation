import json
import os
from utils.logger import logger

def cargar_json(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        logger.error(f"❌ Archivo JSON no encontrado en: {ruta_archivo}")
        return {}

    try:
        with open(ruta_archivo, "or", encoding="utf-8") as f:
            data = json.load(f)
            logger.info(f"📂 Archivo JSON cargado exitosamente: {ruta_archivo}")
            return data
    except Exception as e:
        logger.error(f"❌ Error al leer el archivo JSON: {e}")
        return {}