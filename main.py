from utils.secop_scraper import buscar_licitaciones
from datetime import datetime
import smtplib
from email.message import EmailMessage

# Parámetros de búsqueda
palabras_clave = ["papel", "computador", "resma", "silla", "mobiliario"]
archivo_salida = f"licitaciones_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"

# Ejecutar búsqueda simulada
buscar_licitaciones(palabras_clave, archivo_salida)

# Crear mensaje de correo
msg = EmailMessage()
msg["Subject"] = "Licitaciones encontradas - Roca-Licitaciones"
msg["From"] = "camilo.paezt@gmail.com"
msg["To"] = "roca.variedades2022@gmail.com"
msg.set_content("Adjunto archivo con las licitaciones encontradas hoy.")

# Adjuntar archivo CSV
with open(archivo_salida, "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=archivo_salida)

# Enviar correo usando SMTP de Gmail
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("camilo.paezt@gmail.com", "ikea cdbt qowb dalr")
    smtp.send_message(msg)

