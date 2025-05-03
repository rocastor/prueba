from utils.secop_scraper import buscar_licitaciones as buscar_licitaciones_secop1
from utils.secop2_scraper import buscar_licitaciones as buscar_licitaciones_secop2
from utils.mailer import enviar_resultados_por_correo
from utils.drive_uploader import subir_a_drive_si_hay_resultados
from datetime import datetime

# Parámetros
palabras_clave = ["papel", "computador", "resma", "silla", "mobiliario"]
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M')
archivo_secop1 = f"licitaciones_secop1_{timestamp}.csv"
archivo_secop2 = f"licitaciones_secop2_{timestamp}.csv"

# Ejecutar búsqueda
resultados_secop1 = buscar_licitaciones_secop1(palabras_clave, archivo_secop1)
resultados_secop2 = buscar_licitaciones_secop2(palabras_clave, archivo_secop2)

# Subir a Google Drive (si hay resultados)
carpeta_drive_id = "1mDXUO0tYyIAYAgfpUctnhWvXZyG1aTff"
subir_a_drive_si_hay_resultados(archivo_secop1, carpeta_drive_id)
subir_a_drive_si_hay_resultados(archivo_secop2, carpeta_drive_id)

# Enviar por correo (si hay resultados)
enviar_resultados_por_correo([archivo_secop1, archivo_secop2])
