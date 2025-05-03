import requests
from bs4 import BeautifulSoup
import csv
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def buscar_licitaciones(palabras_clave, nombre_archivo):
    url_base = "https://www.contratos.gov.co/consultas/resultadosConsulta.do"
    resultados = []

    for palabra in palabras_clave:
        print(f"🔍 Buscando en SECOP I: {palabra}")
        try:
            response = requests.get(
                f"{url_base}?tipoProceso=1&modalidad=2&estado=2&criterio=Objeto&palabraClave={palabra}&registros=20",
                verify=False,
                timeout=10
            )
            soup = BeautifulSoup(response.text, "html.parser")
            registros = soup.find_all("tr", class_="listado2") + soup.find_all("tr", class_="listado1")
            resultados.append({
                "palabra": palabra,
                "resultados_encontrados": len(registros)
            })
        except Exception as e:
            print(f"⚠️  Error buscando '{palabra}' en SECOP I: {e}")
            resultados.append({
                "palabra": palabra,
                "resultados_encontrados": "error"
            })

    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["palabra", "resultados_encontrados"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(resultados)
