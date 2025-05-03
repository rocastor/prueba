from datetime import datetime
from utils.secop_scraper import buscar_licitaciones as buscar_licitaciones_secop1
from utils.secop2_scraper import buscar_licitaciones as buscar_licitaciones_secop2
from utils.mailer import enviar_resultados_por_correo
from utils.drive_uploader import subir_a_drive

# Parámetros
palabras_clave = ["papel", "computador", "resma", "silla", "mobiliario"]
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
archivo_secop1 = f"secop1_{timestamp}.csv"
archivo_secop2 = f"secop2_{timestamp}.csv"

# Buscar en SECOP I
resultados_secop1 = buscar_licitaciones_secop1(palabras_clave, archivo_secop1)

# Buscar en SECOP II
resultados_secop2 = buscar_licitaciones_secop2(palabras_clave, archivo_secop2)

# Si hay resultados, enviarlos por correo y subir a Drive
archivos_enviar = []

if resultados_secop1:
    archivos_enviar.append(archivo_secop1)

if resultados_secop2:
    archivos_enviar.append(archivo_secop2)

if archivos_enviar:
    enviar_resultados_por_correo(archivos_enviar)
    subir_a_drive(archivos_enviar)
else:
    print("No se encontraron licitaciones para enviar.")
