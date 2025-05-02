
import smtplib
import os
from email.message import EmailMessage
import csv

def enviar_resultados_por_correo(nombre_archivo, destinatario, remitente):
    try:
        # Verificar si el archivo tiene contenido útil
        with open(nombre_archivo, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            if len(rows) <= 1:
                print("⚠️ No se enviará correo. No hay resultados en el archivo.")
                return

        asunto = "📄 Licitaciones encontradas - Roca-Licitaciones"
        cuerpo = "Adjunto encontrarás el archivo con las licitaciones encontradas hoy desde SECOP I y II."

        mensaje = EmailMessage()
        mensaje["Subject"] = asunto
        mensaje["From"] = remitente
        mensaje["To"] = destinatario
        mensaje.set_content(cuerpo)

        with open(nombre_archivo, "rb") as f:
            mensaje.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=nombre_archivo)

        EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(remitente, EMAIL_PASSWORD)
            smtp.send_message(mensaje)

        print(f"✅ Correo enviado a {destinatario}")

    except Exception as e:
        print(f"❌ Error al enviar el correo: {e}")
