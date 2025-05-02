
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import csv
import os

def subir_a_drive_si_hay_resultados(nombre_archivo, carpeta_drive_id):
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            if len(rows) <= 1:
                print("⚠️ No se subirá a Drive. El archivo no tiene resultados.")
                return

        # Autenticación con Google Drive
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)

        # Subir archivo
        archivo = drive.CreateFile({'title': nombre_archivo, 'parents': [{'id': carpeta_drive_id}]})
        archivo.SetContentFile(nombre_archivo)
        archivo.Upload()
        print(f"✅ Archivo subido a Google Drive: {nombre_archivo}")

    except Exception as e:
        print(f"❌ Error al subir a Google Drive: {e}")
