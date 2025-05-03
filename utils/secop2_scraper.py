
import requests
from bs4 import BeautifulSoup
import csv

def buscar_licitaciones_secop2(palabras_clave, nombre_archivo):
    base_url = "https://www.contratos.gov.co/consultas/resultadosConsulta.do"
    resultados = []

    for palabra in palabras_clave:
        print(f"🔍 Buscando en SECOP II: {palabra}")
        try:
            params = {
                "tipoProceso": "1",
                "modalidad": "2",
                "estado": "2",
                "criterio": "Objeto",
                "palabraClave": palabra,
                "registros": 20
            }

            response = requests.get(base_url, params=params, verify=False, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            filas = soup.select("table.tabla_borde tr")
            if len(filas) > 1:
                resultados.append({"palabra": palabra, "resultado": f"{len(filas)-1} resultados encontrados"})
            else:
                print(f"⚠️  No se encontraron resultados para: {palabra}")

        except Exception as e:
            print(f"❌ Error buscando '{palabra}' en SECOP II: {e}")

    # Guardar resultados
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["palabra", "resultado"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(resultados)
