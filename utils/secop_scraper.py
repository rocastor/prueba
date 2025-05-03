
import requests
from bs4 import BeautifulSoup
import csv
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def buscar_licitaciones_secop1(palabras_clave, nombre_archivo):
    url_base = "https://www.contratos.gov.co/consultas/resultadosConsulta.do"
    resultados = []

    for palabra in palabras_clave:
        print(f"🔍 Buscando en SECOP I: {palabra}")
        try:
            params = {
                "tipoProceso": "",
                "modalidad": "",
                "estado": "2",
                "criterio": "Objeto",
                "palabraClave": palabra,
                "registros": 20
            }
            response = requests.get(url_base, params=params, verify=False, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            tabla = soup.find("table", {"class": "tablas"})
            filas = tabla.find_all("tr")[1:] if tabla else []
            resultados.append({
                "palabra": palabra,
                "resultados": len(filas)
            })
        except Exception as e:
            print(f"❌ Error buscando '{palabra}' en SECOP I:", e)
            resultados.append({
                "palabra": palabra,
                "resultados": "error"
            })

    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["palabra", "resultados"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(resultados)
