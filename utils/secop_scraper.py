
import requests
from bs4 import BeautifulSoup
import csv
import time

def buscar_licitaciones(palabras_clave, nombre_archivo):
    url_base = "https://www.contratos.gov.co/consultas/resultadosConsulta.do"
    headers = {"User-Agent": "Mozilla/5.0"}
    resultados = []

    for palabra in palabras_clave:
        print(f"🔍 Buscando: {palabra}")
        params = {
            "tipoBusqueda": "AVANZADA",
            "idEstado": "2",
            "codigo": "",
            "nombre": palabra,
            "registros": "10"
        }

        try:
            response = requests.get(url_base, params=params, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            filas = soup.select("table.tablaResultados tr")[1:]

            for fila in filas:
                columnas = fila.find_all("td")
                if len(columnas) >= 6:
                    resultados.append({
                        "palabra": palabra,
                        "proceso": columnas[0].text.strip(),
                        "entidad": columnas[1].text.strip(),
                        "objeto": columnas[2].text.strip(),
                        "estado": columnas[3].text.strip(),
                        "valor": columnas[4].text.strip(),
                        "fecha_cierre": columnas[5].text.strip()
                    })

            time.sleep(1)

        except Exception as e:
            print(f"⚠️ Error con '{palabra}': {e}")

    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        campos = ["palabra", "proceso", "entidad", "objeto", "estado", "valor", "fecha_cierre"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(resultados)

    print(f"✅ Guardado: {nombre_archivo}")
