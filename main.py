
from utils.secop_scraper import buscar_licitaciones as buscar_licitaciones_secop1
from utils.secop2_scraper import buscar_licitaciones as buscar_licitaciones_secop2
from utils.mailer import enviar_resultados_por_correo
from utils.drive_uploader import subir_a_drive_si_hay_resultados
from datetime import datetime

# Parámetros
palabras_clave = ["papel", "computador", "resma", "silla", "mobiliario"]
fecha_hora = datetime.now().strftime("%Y-%m-%d_%H-%M")
archivo_secop1 = f"resultados_secop1_{fecha_hora}.csv"
archivo_secop2 = f"resultados_secop2_{fecha_hora}.csv"
carpeta_drive_id = "1kU0OaECALZVfBaRw3RPSbzNNrVHDwJj9"

# Ejecutar búsqueda en SECOP I
print("🔍 Buscando en SECOP I...")
resultados_secop1 = buscar_licitaciones_secop1(palabras_clave, archivo_secop1)

# Ejecutar búsqueda en SECOP II
print("🔍 Buscando en SECOP II...")
resultados_secop2 = buscar_licitaciones_secop2(palabras_clave, archivo_secop2)

# Subir a Drive si hay resultados
subir_a_drive_si_hay_resultados(archivo_secop1, carpeta_drive_id)
subir_a_drive_si_hay_resultados(archivo_secop2, carpeta_drive_id)

# Enviar correo si hay resultados
enviar_resultados_por_correo([archivo_secop1, archivo_secop2])
