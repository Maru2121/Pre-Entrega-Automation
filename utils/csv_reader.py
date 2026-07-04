import csv
import os
from utils.logger import logger

def cargar_csv(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        logger.error(f"❌ Archivo CSV no encontrado en: {ruta_archivo}")
        return []

    filas = []
    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as f:
            lector = csv.reader(f)
            next(lector, None)  # Omitir la cabecera si la tiene
            for fila in lector:
                filas.append(fila)
        logger.info(f"📂 Archivo CSV cargado exitosamente: {ruta_archivo}")
        return filas
    except Exception as e:
        logger.error(f"❌ Error al leer el archivo CSV: {e}")
        return []