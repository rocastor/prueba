
from utils.secop_scraper import buscar_licitaciones as buscar_licitaciones_secop1
from utils.secop2_scraper import buscar_licitaciones as buscar_licitaciones_secop2
from utils.mailer import enviar_resultados_por_correo
from utils.drive_uploader import subir_a_drive_si_hay_resultados
from datetime import datetime

palabras_clave = ["papel", "computador", "resma", "silla", "mobiliario"]
carpeta_drive_id = "TU_CARPETA_ID_AQUI"

timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M')

# Buscar licitaciones en SECOP I
nombre_archivo_secop1 = f"secop1_resultados_{timestamp}.csv"
resultados_secop1 = buscar_licitaciones_secop1(palabras_clave, nombre_archivo_secop1)

# Buscar licitaciones en SECOP II
nombre_archivo_secop2 = f"secop2_resultados_{timestamp}.csv"
resultados_secop2 = buscar_licitaciones_secop2(palabras_clave, nombre_archivo_secop2)

# Enviar resultados por correo si hay
enviar_resultados_por_correo(nombre_archivo_secop1, resultados_secop1)
enviar_resultados_por_correo(nombre_archivo_secop2, resultados_secop2)

# Subir a Drive solo si hay resultados
subir_a_drive_si_hay_resultados(nombre_archivo_secop1, carpeta_drive_id)
subir_a_drive_si_hay_resultados(nombre_archivo_secop2, carpeta_drive_id)
