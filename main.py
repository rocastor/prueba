from utils.secop_scraper import buscar_licitaciones
from datetime import datetime

# Parámetros
palabras_clave = ["papel", "computador", "resma", "silla", "mobiliario"]
archivo_salida = f"licitaciones_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"

# Ejecutar búsqueda
buscar_licitaciones(palabras_clave, archivo_salida)


