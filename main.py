
from utils.secop_scraper import buscar_licitaciones_secop1
from utils.secop2_scraper import buscar_licitaciones_secop2
from utils.mailer import enviar_resultados_por_correo
from utils.drive_uploader import subir_a_drive_si_hay_resultados
from datetime import datetime
import csv

# Parámetros
palabras_clave = ["papel", "computador", "resma", "silla", "mobiliario"]
archivo_salida = f"licitaciones_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"
carpeta_drive_id = "TU_ID_DE_CARPETA_AQUI"  # <- Reemplaza con tu carpeta real
correo_destinatario = "roca.variedades2022@gmail.com"
correo_remitente = "camilo.paezt@gmail.com"

# Ejecutar búsquedas
resultados_secop1 = buscar_licitaciones_secop1(palabras_clave)
resultados_secop2 = buscar_licitaciones_secop2(palabras_clave)

# Unir resultados
todos_los_resultados = resultados_secop1 + resultados_secop2

# Guardar en CSV si hay resultados
if todos_los_resultados:
    with open(archivo_salida, mode="w", newline="", encoding="utf-8") as archivo:
        campos = list(todos_los_resultados[0].keys())
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(todos_los_resultados)

    print(f"✅ Archivo CSV generado: {archivo_salida}")

    # Enviar por correo
    enviar_resultados_por_correo(archivo_salida, correo_destinatario, correo_remitente)

    # Subir a Google Drive
    subir_a_drive_si_hay_resultados(archivo_salida, carpeta_drive_id)
else:
    print("⚠️ No se encontraron licitaciones. No se generó archivo.")
