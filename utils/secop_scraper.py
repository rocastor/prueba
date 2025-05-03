import requests
from bs4 import BeautifulSoup
import csv

def buscar_licitaciones(palabras_clave, nombre_archivo):
    url_base = "https://www.contratos.gov.co/consultas/resultadosConsulta.do"
    resultados = []

    for palabra in palabras_clave:
        print(f"Buscando en SECOP I: {palabra}")
        try:
            params = {
                "tipoProceso": "1",
                "modalidad": "2",
                "estado": "2",
                "criterio": "Objeto",
                "palabraClave": palabra,
                "registros": "20"
            }
            response = requests.get(url_base, params=params, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            tabla = soup.find('table')
            if tabla:
                filas = tabla.find_all('tr')[1:]  # Omitir encabezado
                for fila in filas:
                    columnas = fila.find_all('td')
                    if len(columnas) >= 2:
                        entidad = columnas[0].text.strip()
                        objeto = columnas[1].text.strip()
                        resultados.append({"palabra": palabra, "entidad": entidad, "objeto": objeto})
        except Exception as e:
            print(f"⚠️  Error buscando '{palabra}' en SECOP I: {e}")

    if resultados:
        with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
            campos = ["palabra", "entidad", "objeto"]
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writeheader()
            writer.writerows(resultados)
    return resultados
