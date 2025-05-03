
from utils.secop_scraper import buscar_licitaciones as buscar_licitaciones_secop1
from utils.secop2_scraper import buscar_licitaciones as buscar_licitaciones_secop2
from utils.mailer import enviar_resultados_por_correo
from utils.drive_uploader import subir_a_drive_si_hay_resultados
from datetime import datetime

# Palabras clave a buscar
palabras_clave = ["papel", "computador", "resma", "silla", "mobiliario"]

# Nombres de archivos
fecha_hora = datetime.now().strftime('%Y-%m-%d_%H-%M')
archivo_secop1 = f"licitaciones_secop1_{fecha_hora}.csv"
archivo_secop2 = f"licitaciones_secop2_{fecha_hora}.csv"

# Carpeta de Drive (ID de tu carpeta en Google Drive)
carpeta_drive_id = "1JWAw2wEy_NjI7bMrBdjIkS30jByO7Pyd"

# Buscar licitaciones en SECOP I y II
resultados_secop1 = buscar_licitaciones_secop1(palabras_clave, archivo_secop1)
resultados_secop2 = buscar_licitaciones_secop2(palabras_clave, archivo_secop2)

# Subir a Drive solo si hay resultados
subir_a_drive_si_hay_resultados(archivo_secop1, carpeta_drive_id)
subir_a_drive_si_hay_resultados(archivo_secop2, carpeta_drive_id)

# Enviar por correo si hay resultados
enviar_resultados_por_correo(archivo_secop1)
enviar_resultados_por_correo(archivo_secop2)
