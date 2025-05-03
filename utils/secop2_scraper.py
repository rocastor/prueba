import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def buscar_licitaciones(palabras_clave, nombre_archivo):
    opciones = Options()
    opciones.add_argument("--headless")
    opciones.add_argument("--no-sandbox")
    opciones.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opciones)

    resultados = []

    for palabra in palabras_clave:
        print(f"🔍 Buscando en SECOP II: {palabra}")
        try:
            driver.get("https://www.contratos.gov.co/consultas/inicioConsulta.do")
            time.sleep(2)
            search_box = driver.find_element(By.NAME, "palabraClave")
            search_box.clear()
            search_box.send_keys(palabra)
            search_box.submit()
            time.sleep(4)
            resultados.append({"palabra": palabra, "resultado": "Simulado SECOP II - búsqueda ejecutada"})
        except Exception as e:
            print(f"❌ Error en SECOP II con '{palabra}': {e}")
            resultados.append({"palabra": palabra, "resultado": "Error"})

    driver.quit()

    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["palabra", "resultado"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(resultados)
