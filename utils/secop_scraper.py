import requests
from bs4 import BeautifulSoup
import csv

def buscar_licitaciones(palabras_clave, nombre_archivo):
    url_base = "https://www.contratos.gov.co/consultas/inicioConsulta.do"
    resultados = []

    for palabra in palabras_clave:
        print(f"Buscando licitaciones con: {palabra}")
        resultados.append({
            "palabra": palabra,
            "resultado": "Simulado - prueba de robot"
        })

    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["palabra", "resultado"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(resultados)
