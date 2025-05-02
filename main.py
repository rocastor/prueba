from utils.secop_scraper import buscar_licitaciones
from datetime import datetime
import smtplib
from email.message import EmailMessage
import os

# Parámetros
palabras_clave = ["papel", "computador", "resma", "silla", "mobiliario"]
archivo_salida = f"licitaciones_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"

# Ejecutar búsqueda
buscar_licitaciones(palabras_clave, archivo_salida)

# Enviar por correo
mensaje = EmailMessage()
mensaje["Subject"] = "📄 Licitaciones encontradas - Roca-Licitaciones"
mensaje["From"] = "camilo.paezt@gmail.com"
mensaje["To"] = "roca.variedades2022@gmail.com"
mensaje.set_content("Adjunto el archivo con los resultados de la búsqueda de licitaciones más recientes.")

with open(archivo_salida, "rb") as adjunto:
    mensaje.add_attachment(adjunto.read(), maintype="application", subtype="octet-stream", filename=archivo_salida)

# Autenticación usando variable de entorno
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("camilo.paezt@gmail.com", EMAIL_PASSWORD)
    smtp.send_message(mensaje)

print("✅ Correo enviado con éxito a roca.variedades2022@gmail.com")
