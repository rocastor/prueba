
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

def buscar_licitaciones(palabras_clave, nombre_archivo):
    opciones = Options()
    opciones.add_argument("--headless")
    opciones.add_argument("--no-sandbox")
    opciones.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opciones)
    resultados = []

    for palabra in palabras_clave:
        print(f"Buscando '{palabra}' en SECOP II...")
        try:
            driver.get("https://www.colombiacompra.gov.co/secop/secop-ii")
            time.sleep(2)

            campo_busqueda = driver.find_element(By.NAME, "query")
            campo_busqueda.clear()
            campo_busqueda.send_keys(palabra)
            campo_busqueda.submit()
            time.sleep(3)

            titulos = driver.find_elements(By.CSS_SELECTOR, "div.result h3")
            for titulo in titulos:
                resultados.append({"palabra": palabra, "resultado": titulo.text})

        except Exception as e:
            print(f"Error buscando '{palabra}' en SECOP II: {e}")
            resultados.append({"palabra": palabra, "resultado": f"Error: {e}"})

    driver.quit()

    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["palabra", "resultado"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(resultados)
