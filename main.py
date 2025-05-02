from utils.secop_scraper import buscar_licitaciones
from datetime import datetime
import smtplib
from email.message import EmailMessage

# Parámetros
palabras_clave = ["papel", "computador", "resma", "silla", "mobiliario"]
archivo_salida = f"licitaciones_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"

# Ejecutar búsqueda
buscar_licitaciones(palabras_clave, archivo_salida)

# Enviar correo
msg = EmailMessage()
msg["Subject"] = "Licitaciones encontradas - Roca-Licitaciones"
msg["From"] = "camilo.paezt@gmail.com"
msg["To"] = "roca.variedades2022@gmail.com"
msg.set_content("Adjunto archivo con las licitaciones encontradas hoy.")

with open(archivo_salida, "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=archivo_salida)

# Autenticación Gmail (usa tu clave de app)
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("camilo.paezt@gmail.com", "AQUI_TU_CLAVE_DE_APP")
    smtp.send_message(msg)
