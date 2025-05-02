from utils.secop_scraper import buscar_licitaciones
from datetime import datetime
import smtplib
from email.message import EmailMessage
import os

# Parámetros de búsqueda
palabras_clave = ["papel", "computador", "resma", "silla", "mobiliario"]
archivo_salida = f"licitaciones_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"

# Ejecutar búsqueda
buscar_licitaciones(palabras_clave, archivo_salida)

# Configurar correo
remitente = "camilo.paezt@gmail.com"
destinatario = "roca.variedades2022@gmail.com"
asunto = "Licitaciones encontradas - Roca-Licitaciones"
cuerpo = "Adjunto encontrarás el archivo con las licitaciones encontradas hoy."

mensaje = EmailMessage()
mensaje["Subject"] = asunto
mensaje["From"] = remitente
mensaje["To"] = destinatario
mensaje.set_content(cuerpo)

# Adjuntar el archivo CSV
with open(archivo_salida, "rb") as f:
    contenido = f.read()
    mensaje.add_attachment(contenido, maintype="application", subtype="octet-stream", filename=archivo_salida)

# Enviar el correo
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # Cargada desde Render

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(remitente, EMAIL_PASSWORD)
    smtp.send_message(mensaje)
