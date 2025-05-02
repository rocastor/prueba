
import requests
from bs4 import BeautifulSoup
import json

def buscar_licitaciones_secop2(palabras_clave):
    url_base = "https://www.secop.gov.co/secop/buscadorAvanzado/buscarProcesos"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }

    resultados = []

    for palabra in palabras_clave:
        print(f"🔍 Buscando en SECOP II: {palabra}")

        body = {
            "palabraClave": palabra,
            "estadoProceso": ["Publicacion"]  # Solo procesos activos
        }

        try:
            response = requests.post(url_base, headers=headers, data=json.dumps(body), timeout=10)
            if response.status_code == 200:
                datos = response.json()
                procesos = datos.get("procesos", [])

                for proceso in procesos:
                    resultado = {
                        "Entidad": proceso.get("entidad", {}).get("nombreEntidad", ""),
                        "Número del proceso": proceso.get("numeroProceso", ""),
                        "Objeto": proceso.get("objetoProceso", ""),
                        "Cuantía": proceso.get("cuantiaProceso", ""),
                        "Fecha de cierre": proceso.get("fechaCierreProceso", ""),
                        "Fuente": "SECOP II",
                        "Palabra clave": palabra
                    }
                    resultados.append(resultado)
        except Exception as e:
            print(f"Error buscando '{palabra}' en SECOP II: {e}")

    return resultados
